from __future__ import annotations

import csv
import time
from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st
import torch
from PIL import Image
from transformers import (
    BlipForConditionalGeneration,
    BlipForQuestionAnswering,
    BlipProcessor,
)


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "outputs"
RESULTS_FILE = OUTPUT_DIR / "results.csv"

CAPTION_MODEL_ID = "Salesforce/blip-image-captioning-base"
VQA_MODEL_ID = "Salesforce/blip-vqa-base"
ALLOWED_IMAGE_NAMES = {
    "sample_1_laptop.png": "Man sitting on a chair using a laptop",
    "sample_2_lion.png": "Lion standing in a forest",
    "sample_3_soccer.png": "Children playing soccer on a field",
}


def get_device() -> str:
    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


DEVICE = get_device()


def prepare_results_file() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    if RESULTS_FILE.exists():
        return

    with RESULTS_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "timestamp",
                "image_name",
                "caption",
                "question",
                "predicted_answer",
                "expected_answer",
                "correct",
                "latency_seconds",
            ]
        )


@st.cache_resource(show_spinner="Loading image captioning model...")
def load_caption_model():
    processor = BlipProcessor.from_pretrained(CAPTION_MODEL_ID)
    model = BlipForConditionalGeneration.from_pretrained(CAPTION_MODEL_ID)
    model.to(DEVICE)
    model.eval()
    return processor, model


@st.cache_resource(show_spinner="Loading visual question answering model...")
def load_vqa_model():
    processor = BlipProcessor.from_pretrained(VQA_MODEL_ID)
    model = BlipForQuestionAnswering.from_pretrained(VQA_MODEL_ID)
    model.to(DEVICE)
    model.eval()
    return processor, model


def generate_caption(image: Image.Image) -> tuple[str, float]:
    processor, model = load_caption_model()
    start = time.perf_counter()

    inputs = processor(images=image, return_tensors="pt").to(DEVICE)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=35)

    caption = processor.decode(output[0], skip_special_tokens=True)
    latency = time.perf_counter() - start
    return caption, latency


def answer_question(image: Image.Image, question: str) -> tuple[str, float]:
    processor, model = load_vqa_model()
    start = time.perf_counter()

    inputs = processor(images=image, text=question, return_tensors="pt").to(DEVICE)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=20)

    answer = processor.decode(output[0], skip_special_tokens=True)
    latency = time.perf_counter() - start
    return answer, latency


def save_result(
    image_name: str,
    caption: str,
    question: str,
    predicted_answer: str,
    expected_answer: str,
    correct: bool | None,
    latency_seconds: float,
) -> None:
    prepare_results_file()
    with RESULTS_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                datetime.now().isoformat(timespec="seconds"),
                image_name,
                caption,
                question,
                predicted_answer,
                expected_answer,
                "" if correct is None else int(correct),
                round(latency_seconds, 3),
            ]
        )


def load_results() -> pd.DataFrame:
    prepare_results_file()
    return pd.read_csv(RESULTS_FILE)


def reset_session_for_new_image(image_name: str) -> None:
    if st.session_state.get("image_name") == image_name:
        return

    st.session_state.image_name = image_name
    st.session_state.caption = ""
    st.session_state.caption_latency = 0.0
    st.session_state.answer = ""
    st.session_state.answer_latency = 0.0
    st.session_state.last_question = ""


def main() -> None:
    st.set_page_config(
        page_title="Visual Insight Assistant",
        page_icon=":frame_with_picture:",
        layout="wide",
    )
    prepare_results_file()

    st.title("Visual Insight Assistant")
    st.caption("Image captioning and visual question answering using BLIP")

    with st.sidebar:
        st.header("Project")
        st.write("Roll No: `1024170154`")
        st.write("Topic: Vision-Language Models for Image Understanding")
        st.write(f"Device: `{DEVICE}`")
        st.write("Models:")
        st.code(f"{CAPTION_MODEL_ID}\n{VQA_MODEL_ID}")

    left, right = st.columns([1, 1], gap="large")

    with left:
        st.subheader("1. Add Image")
        st.write("Upload only one of the three selected demo images.")
        st.code("\n".join(ALLOWED_IMAGE_NAMES.keys()))
        image_file = st.file_uploader(
            "Upload selected image",
            type=["png"],
        )

        if image_file is None:
            st.info("Save the three provided images in sample_images/ and upload one.")
            return

        image_name = getattr(image_file, "name", "camera_image.png")
        if image_name not in ALLOWED_IMAGE_NAMES:
            st.warning(
                "This project demo uses only the three provided images. "
                f"Please upload one of: {', '.join(ALLOWED_IMAGE_NAMES)}"
            )
            return

        image = Image.open(image_file).convert("RGB")
        reset_session_for_new_image(image_name)
        st.image(image, caption=image_name, use_container_width=True)

    with right:
        st.subheader("2. Generate Caption")
        if st.button("Generate caption", type="primary", use_container_width=True):
            caption, latency = generate_caption(image)
            st.session_state.caption = caption
            st.session_state.caption_latency = latency

        if st.session_state.get("caption"):
            st.success(st.session_state.caption)
            st.write(
                f"Caption latency: `{st.session_state.caption_latency:.2f}` seconds"
            )

        st.divider()
        st.subheader("3. Ask About The Image")
        question = st.text_input(
            "Question",
            placeholder="Example: What object is visible in the image?",
        )

        if st.button("Answer question", use_container_width=True):
            if not question.strip():
                st.warning("Enter a question first.")
            else:
                answer, latency = answer_question(image, question.strip())
                st.session_state.answer = answer
                st.session_state.answer_latency = latency
                st.session_state.last_question = question.strip()

        if st.session_state.get("answer"):
            st.success(st.session_state.answer)
            st.write(f"Answer latency: `{st.session_state.answer_latency:.2f}` seconds")

            with st.form("save_result_form"):
                expected = st.text_input(
                    "Expected answer for evaluation",
                    placeholder="Optional, for example: bicycle",
                )
                correct = st.checkbox("Mark answer as correct")
                submitted = st.form_submit_button("Save result to CSV")

            if submitted:
                save_result(
                    image_name=st.session_state.image_name,
                    caption=st.session_state.get("caption", ""),
                    question=st.session_state.last_question,
                    predicted_answer=st.session_state.answer,
                    expected_answer=expected,
                    correct=correct if expected else None,
                    latency_seconds=st.session_state.answer_latency,
                )
                st.toast("Result saved.")

    st.divider()
    st.subheader("Evaluation Results")
    results = load_results()
    if results.empty:
        st.info("Saved answers will appear here.")
    else:
        st.dataframe(results.tail(10), use_container_width=True)

        evaluated = results[results["correct"].notna()]
        if not evaluated.empty:
            accuracy = evaluated["correct"].astype(int).mean() * 100
            average_latency = evaluated["latency_seconds"].mean()
            metric_left, metric_right = st.columns(2)
            metric_left.metric("VQA Accuracy", f"{accuracy:.1f}%")
            metric_right.metric("Average Latency", f"{average_latency:.2f}s")


if __name__ == "__main__":
    main()
