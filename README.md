# Visual Insight Assistant

## Image Captioning and Visual Question Answering using BLIP

**Roll No:** 1024170154

**ELC Topic:** Vision-Language Models for Image Understanding

### 1. Introduction

Computer vision is an area of artificial intelligence that helps computers understand images and videos. Modern computer vision systems are no longer limited to detecting edges, colors, or objects. They can combine visual information with natural language to describe images and answer questions about them.

This project builds an interactive image understanding system using a pretrained vision-language model. The user uploads one of the three selected demo images, the system generates a caption, and the user can ask natural-language questions about the image. The app is restricted to the three project images only.

### 2. Problem Statement

Traditional image processing can identify simple visual patterns, but it cannot easily explain an image in human language or answer questions about it. The problem is to build a system that can understand image content and interact with the user through text.

The goal of this project is to create a vision-language image understanding assistant that performs:

- Image caption generation
- Visual question answering
- Basic evaluation using accuracy and latency

### 3. Methodology

The system uses pretrained BLIP models from Hugging Face Transformers:

- `Salesforce/blip-image-captioning-base`
- `Salesforce/blip-vqa-base`

The image captioning model generates a short textual description of the image. The visual question answering model takes both the image and a text question as input, then generates an answer.

The application is built using:

- Python
- Streamlit
- PyTorch
- Hugging Face Transformers
- Pillow
- Pandas

### 4. System Flow

```text
User uploads or captures image
        |
Image is displayed in the app
        |
BLIP captioning model generates a caption
        |
User asks a question about the image
        |
BLIP VQA model generates an answer
        |
Result is displayed and optionally saved
```

### 5. Implementation

The main file is `app.py`. It loads the pretrained models, accepts only the three selected image filenames, generates captions, answers questions, and logs results to `outputs/results.csv`.

The app uses Streamlit caching so the models load once and can be reused during the session.

### 6. Evaluation

The system is tested with the three selected demo images provided for this project. For each image, the user can ask 2 or 3 questions and manually mark whether the predicted answer is correct.

Metrics used:

- VQA accuracy
- Average answer latency
- Manual caption quality score

Example evaluation format:

```text
Image: sample_1_laptop.png
Caption: A man sitting in a chair using a laptop.
Question: What is the person using?
Predicted answer: laptop
Expected answer: laptop
Correct: yes
```

Demo image set:

```text
sample_1_laptop.png - man sitting on a chair using a laptop
sample_2_lion.png - lion standing in a forest
sample_3_soccer.png - children playing soccer on a field
```

The test questions are listed in `demo_assets/test_questions.csv`.

### 7. Conclusion

This project demonstrates how modern computer vision can be combined with natural language processing. The system uses a pretrained vision-language model to generate image captions and answer questions about images. It shows that multimodal AI can make image understanding more interactive and human-friendly.

## How To Run

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

Open the Streamlit URL shown in the terminal.

## Submission Checklist

Before submitting, confirm the final zip contains:

- Source code: `app.py`
- Dependency file: `requirements.txt`
- Write-up: `README.md`
- Sample images: the three provided images saved in `sample_images/`
- Results file: `outputs/results.csv`
- Demo video: `demo_video.mp4`

The demo video is mandatory according to the problem statement.
