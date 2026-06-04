# Demo Video Script

Target length: 60 to 90 seconds.

## What To Show And Speak

### 1. Project Introduction

Show the Streamlit app home screen.

Speak:

```text
My roll number is 1024170154. My ELC project is Visual Insight Assistant, based on the topic Vision-Language Models for Image Understanding.
```

### 2. Problem Explanation

Show the title and sidebar.

Speak:

```text
The goal of this project is to make a computer vision system that can understand an image, generate a caption, and answer questions about the image.
```

### 3. Image Input

Select `sample_1_laptop.png` from the image dropdown.

Speak:

```text
First, I select one of the fixed project images. The image is displayed in the interface for processing.
```

### 4. Caption Generation

Click the "Generate caption" button.

Speak:

```text
Now I click Generate caption. The pretrained BLIP image captioning model analyzes the image and produces a natural-language description.
```

Read the generated caption aloud.

### 5. Visual Question Answering

Type a question, for example:

```text
What is the person using?
```

or:

```text
Where is the person sitting?
```

Click "Answer question."

Speak:

```text
Now I ask a question about the same image. The BLIP visual question answering model uses both the image and my question to generate an answer.
```

Read the answer aloud.

### 6. Evaluation Logging

Fill expected answer if you know it, mark whether the answer is correct, and click "Save result to CSV."

Speak:

```text
For evaluation, I save the question, predicted answer, expected answer, correctness, and response time into a CSV file.
```

### 7. Show Results Table

Scroll to the evaluation table.

Speak:

```text
The saved results are shown in this table. The project calculates basic evaluation values such as answer accuracy and average response time.
```

### 8. Show The Other Two Provided Images

Select `sample_2_lion.png`.

Ask:

```text
What animal is shown?
```

Expected answer:

```text
lion
```

Speak:

```text
For the second image, the model identifies the animal as a lion.
```

Select `sample_3_soccer.png`.

Ask:

```text
What sport are the children playing?
```

Expected answer:

```text
soccer
```

Speak:

```text
For the third image, the model understands that the children are playing soccer.
```

### 9. Conclusion

Show the app with one completed example.

Speak:

```text
This project demonstrates how modern computer vision can combine image understanding and language understanding. It uses pretrained BLIP vision-language models for image captioning and visual question answering.
```

## Minimum Demo Checklist

- Show project title
- Mention roll number 1024170154
- Select image
- Generate caption
- Ask one question
- Show answer
- Save result
- Show evaluation table
- Show the lion image and soccer image
- State conclusion
