# Visual Insight Assistant

**Image Captioning and Visual Question Answering using BLIP**

**Roll Number:** 1024170154  
**ELC Topic:** Vision-Language Models for Image Understanding  
**Project Type:** Computer Vision and Multimodal AI Application

## Overview

Visual Insight Assistant is an interactive computer vision application that combines image understanding with natural-language interaction. The system uses pretrained BLIP vision-language models to generate captions for uploaded images and answer user questions about visual content.

The application supports JPG and PNG uploads. After uploading an image, the user can generate a caption and ask open-ended questions about that image.

## Problem Statement

Traditional image processing can detect simple patterns, colors, edges, or objects, but it cannot easily explain an image in natural language or answer questions about image content. This project addresses that limitation by using a vision-language model that processes both visual and textual information.

The objective is to build a user-friendly system that can:

- Understand uploaded image content
- Generate a meaningful image caption
- Answer natural-language questions about the image
- Record evaluation results such as correctness and response time

## Features

- JPG and PNG image upload
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
Upload a JPG or PNG image
        |
Display the uploaded image
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
  demo_assets/
    demo_script.md
    test_questions.csv
  outputs/
    results.csv
```

## Demo Images

For the final demo, use the three images prepared for this project:

```text
sample_images/sample_1_laptop.png
sample_images/sample_2_lion.png
sample_images/sample_3_soccer.png
```

The app can also process any other JPG or PNG image through the upload control.

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

1. Upload a JPG or PNG image.
2. Click **Generate caption**.
3. Read the generated image description.
4. Enter a question about the uploaded image.
5. Click **Answer question**.
6. Add the expected answer if evaluating the result.
7. Mark whether the answer is correct.
8. Save the result to CSV.

## Evaluation Plan

Evaluation can be performed using the three prepared demo images and predefined questions stored in:

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
- Uploading the laptop image
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

This project demonstrates how computer vision can be extended through vision-language models. Instead of only detecting objects, the system can describe uploaded images and answer questions about them. The result is a simple, interactive, and practical image understanding application suitable for demonstrating modern computer vision concepts.
