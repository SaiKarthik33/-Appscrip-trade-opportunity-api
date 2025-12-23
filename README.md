# Trade Opportunities API 📈

## 👋 About This Project
Welcome! This is an AI-powered tool designed to act like a smart financial research assistant. 

The goal was simple: build an API that takes a specific industry sector (like Technology or Agriculture) and instantly tells you what's happening in the market right now. It combines real-time news search with **Google's Gemini 2.5 Flash** to generate a clear, easy-to-read report on trade opportunities and risks in India.

## 🎥 See It in Action
I’ve recorded a quick demo showing exactly how the API processes requests and generates reports.
👉 **[Watch the Video Demo Here](https://drive.google.com/file/d/1LCOFZVrpk_dvX-0JgQa_oHOLlcCtA-l6/view?usp=sharing)**

## ✨ What It Does
* **Analyzes the Market:** It doesn't just guess—it uses DuckDuckGo to fetch the latest real-time news.
* **Thinks Fast:** I integrated the **Gemini 2.5 Flash** model so the analysis is incredibly fast and accurate.
* **Writes Reports:** You get a structured Markdown report with key trends, investment opportunities, and potential risks.
* **Stays Secure:** The API is protected with a custom security token (`x-token`) so unauthorized users can't access it.

## 🛠️ How It’s Built
I chose these tools to ensure performance and reliability:
* **FastAPI:** For a high-performance backend.
* **Google GenAI SDK:** To access the Gemini 2.5 Flash model.
* **DuckDuckGo Search:** For live data fetching without API rate limits.
* **Python 3.11+:** Using the latest features for speed.


