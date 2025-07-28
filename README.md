# 📝 Text Summarizer

An AI-powered web app that shortens long texts into clear, concise summaries using state-of-the-art NLP.

[![Live Demo](https://img.shields.io/badge/Try%20it%20on%20HuggingFace-%F0%9F%94%97-blue?style=for-the-badge)](https://huggingface.co/spaces/Ruusheka/Text_summarizer)

---

## 🚀 About

This web app simplifies reading by generating short summaries from long paragraphs — perfect for students, readers, and researchers.

---

## 🧠 Model Used

- [`sshleifer/distilbart-cnn-12-6`](https://huggingface.co/sshleifer/distilbart-cnn-12-6)  
A lightweight distilled version of BART fine-tuned on CNN/DailyMail dataset for summarization.

---

## 🖼️ Demo

![Demo](https://github.com/Ruusheka/Text-Summarizer/blob/main/assets/demoPic.png?raw=true)

---

## 🔧 Tech Stack

- 🤗 Transformers
- 🧠 Model: `sshleifer/distilbart-cnn-12-6`
- 🖥️ Gradio Interface
- 🌐 Deployed on Hugging Face Spaces

---

## 💡 How to Use

1. Paste any paragraph or long-form content.
2. Click **Summarize**.
3. Get a short, meaningful summary instantly.

---

## 🧪 Run Locally (Optional)

```bash
git clone https://github.com/Ruusheka/Text_summarizer.git
cd Text_summarizer
pip install -r requirements.txt
python app.py
