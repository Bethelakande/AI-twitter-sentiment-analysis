# Twitter Sentiment Analysis 🐦💬

A sophisticated Python-based tool designed to fetch real-time data from X (formerly Twitter) and perform deep sentiment analysis using State-of-the-Art (SOTA) Natural Language Processing models.

## 🚀 Overview

This project leverages the power of Machine Learning to understand the emotional pulse of the internet on any given topic. By analyzing recent tweets, the application classifies public opinion into three distinct categories: **Negative**, **Neutral**, and **Positive**.

Whether you're tracking brand reputation, political sentiment, or social trends, this tool provides a data-driven window into the global conversation.

## 🛠️ Tech Stack

The project is built with a modern Python ecosystem for data science and AI:

- **Language:** Python 3.12+
- **API Integration:** [Tweepy](https://www.tweepy.org/) (X API v2)
- **Deep Learning Framework:** [PyTorch](https://pytorch.org/) & [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- **Sentiment Model:** [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest)
- **Data Processing:** NumPy, SciPy (Softmax), and TextBlob
- **Environment Management:** `python-dotenv` for secure API credential handling

## ✨ Key Features

- **X (Twitter) API v2 Integration:** Seamlessly fetches recent tweets based on specific keywords or topics.
- **Advanced Pre-processing:** Automatically cleans tweets by normalizing user mentions (`@user`) and anonymizing URLs to improve model accuracy.
- **RoBERTa Sentiment Engine:** Uses a specialized RoBERTa model trained specifically on Twitter datasets to understand slang, emojis, and social media nuances better than traditional lexicons.
- **Confidence Scoring:** Calculates the probability of each sentiment category using Softmax normalization.

## 📋 Setup & Installation

### 1. Prerequisites
- Python 3.12 or higher.
- An X (Twitter) Developer Account with API Keys and a Bearer Token.

### 2. Configuration
Create a `.env` file in the root directory and add your credentials:

```env
CUSTOMER_API_KEY=your_key_here
CUSTOMER_API_KEY_SECRET=your_secret_here
ACCESS_TOKEN=your_token_here
ACCESS_TOKEN_SECRET=your_token_secret_here
BEARER_TOKEN=your_bearer_token_here
```

### 3. Installation
Using `uv` (recommended):
```bash
uv sync
```
Or using `pip`:
```bash
pip install -r requirements.txt
```

## 🔮 Future Improvements & Use Cases

We are actively looking to expand this project into a more dynamic and interactive platform:

- **🌐 Web Interface:** Build a sleek Streamlit or Next.js frontend to replace the CLI.
- 
### 🌟 Real-Time Live Monitoring
The next evolution involves moving from batch processing to **Real-Time Streaming**. By implementing X's filtered streams, we can monitor "feelings" on a certain topic as they happen, second by second.

### ⚽ The World Cup 2026 Use Case
Imagine the World Cup 2026 is happening. You're busy, but you want to know if a particular match is worth tuning into. 
- **The Concept:** A "Hype-O-Meter" that analyzes the sentiment and volume of tweets during a live match.
- **Functionality:** If the sentiment is overwhelmingly positive and the "excitement score" is high (detecting words like "goal", "unbelievable", "wonder-strike"), the tool sends you a notification: *"Stop what you're doing—this match is heating up!"*
- **Outcome:** Use real-time public emotion to determine whether a match is a "must-watch" or a "skip".

---

*Developed as part of an AI learning journey to bridge the gap between social data and actionable insights.*
