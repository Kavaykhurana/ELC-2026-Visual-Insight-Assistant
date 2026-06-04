# Visual Insight Assistant

**Image Captioning and Visual Question Answering using BLIP**

**Roll Number:** 1024170154  
**ELC Topic:** Vision-Language Models for Image Understanding  
**Project Type:** Computer Vision and Multimodal AI Application

## Overview

Visual Insight Assistant is an interactive computer vision application that combines image understanding with natural-language interaction. The system uses pretrained BLIP vision-language models to generate captions for images and answer user questions about visual content.

The project is built around three fixed demonstration images:

- A person using a laptop
- A lion in a forest
- Children playing soccer

The application reads only these three project images from the `sample_images/` folder. This keeps the demonstration focused, reproducible, and aligned with the evaluation examples.

## Problem Statement

Traditional image processing can detect simple patterns, colors, edges, or objects, but it cannot easily explain an image in natural language or answer questions about image content. This project addresses that limitation by using a vision-language model that processes both visual and textual information.

The objective is to build a user-friendly system that can:

- Understand selected image content
- Generate a meaningful image caption
- Answer natural-language questions about the image
- Record evaluation results such as correctness and response time

## Features

- Fixed three-image project dataset
- Automatic image caption generation
- Visual question answering
- Interactive Streamlit interface
- Result logging to CSV
- Basic evaluation with accuracy and latency
- Clear demo workflow for submission video

## Technology Stack

| Component | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| PyTorch | Model execution |
| Hugging Face Transformers | Loading pretrained BLIP models |
| Pillow | Image loading and conversion |
| Pandas | CSV result handling |

## Models Used

The project uses pretrained BLIP models:

```text
Salesforce/blip-image-captioning-base
Salesforce/blip-vqa-base
```

No custom training is performed. The focus of the project is implementation, interaction design, computer vision application flow, and evaluation.

## System Workflow

```text
Select one of the three project images
        |
Display the selected image
        |
Generate image caption using BLIP
        |
Ask a question about the image
        |
Generate answer using BLIP VQA
        |
Save result and show evaluation table
```

## Project Structure

```text
ELC_VLM_Image_Understanding/
  app.py
  requirements.txt
  README.md
  SUBMISSION_CHECKLIST.md
  sample_images/
    README.md
    sample_1_laptop.png
    sample_2_lion.png
    sample_3_soccer.png
  demo_assets/
    demo_script.md
    test_questions.csv
  outputs/
    results.csv
```

## Required Images

Before running the final demo, place only the three provided images inside `sample_images/` using these exact filenames:

```text
sample_images/sample_1_laptop.png
sample_images/sample_2_lion.png
sample_images/sample_3_soccer.png
```

The app will show missing-file warnings if any of these files are not present.

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

Open the Streamlit URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Usage

1. Select one of the available project images.
2. Click **Generate caption**.
3. Read the generated image description.
4. Enter a question about the selected image.
5. Click **Answer question**.
6. Add the expected answer if evaluating the result.
7. Mark whether the answer is correct.
8. Save the result to CSV.

## Evaluation Plan

Evaluation is performed using the three fixed project images and predefined questions stored in:

```text
demo_assets/test_questions.csv
```

Recommended questions:

| Image | Question | Expected Answer |
|---|---|---|
| `sample_1_laptop.png` | What is the person using? | laptop |
| `sample_1_laptop.png` | Where is the person sitting? | chair |
| `sample_2_lion.png` | What animal is shown? | lion |
| `sample_2_lion.png` | Where is the lion? | forest |
| `sample_3_soccer.png` | What sport are the children playing? | soccer |
| `sample_3_soccer.png` | What object is on the grass? | soccer ball |

Metrics used:

- **VQA Accuracy:** percentage of correctly answered questions
- **Average Latency:** average response time for answers
- **Caption Quality:** manual review of caption relevance

Results are saved in:

```text
outputs/results.csv
```

## Demo Video Guide

Use the prepared script:

```text
demo_assets/demo_script.md
```

The video should show:

- Project title and roll number
- Selection of the laptop image
- Caption generation
- Question answering
- Saving an evaluation result
- Evaluation table
- A quick example using the lion image
- A quick example using the soccer image

## Submission Checklist

Before creating the final zip file, confirm that the folder contains:

- `app.py`
- `requirements.txt`
- `README.md`
- `SUBMISSION_CHECKLIST.md`
- `sample_images/sample_1_laptop.png`
- `sample_images/sample_2_lion.png`
- `sample_images/sample_3_soccer.png`
- `outputs/results.csv`
- `demo_assets/demo_script.md`
- `demo_assets/test_questions.csv`
- `demo_video.mp4`

## Conclusion

This project demonstrates how computer vision can be extended through vision-language models. Instead of only detecting objects, the system can describe selected images and answer questions about them. The result is a simple, interactive, and practical image understanding application suitable for demonstrating modern computer vision concepts.

