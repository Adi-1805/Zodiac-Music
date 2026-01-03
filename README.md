# 🔮 StarTrack: AI-Powered Song Recommender

**StarTrack** is a Python-based web application that curates personalized music playlists based on your astrological sign to expand your listening horizon.

Built with **Streamlit** for the frontend and **LangChain + Google Gemini** for the intelligence, this app analyzes the personality traits of a Zodiac sign and acts as a "Cosmic DJ" to suggest songs that match the vibe in your language of choice.

## 🚀 Features

* **Zodiac Analysis**: Understands the psychological profile (traits, strengths, weaknesses) of all 12 signs.
* **Language Option**: Making it expand boundaries by adding 23 Indian languages.
* **AI Curation**: Uses Google's **Gemini 2.0 Flash** model to generate unique song recommendations with explanations.
* **Robust Error Handling**: Includes custom messages for API quota limits ("Credits Over") and invalid keys.
* **Separation of Concerns**: Clean architecture separating the UI (`app.py`) from the Logic (`langchain_helper.py`).

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **LLM Orchestration**: LangChain
* **AI Model**: Google Gemini (via `langchain-google-genai`)
* **Language**: Python 3.10+

## 📂 Project Structure

```text
Zodiac-Music/
│
├── app.py                  # Main entry point (Streamlit UI)
├── langchain_helper.py     # AI Logic & LangChain chains
├── my_secret_key.py        # Stores API Key (Do not commit to GitHub!)
├── requirements.txt        # List of dependencies
└── README.md               # Documentation
