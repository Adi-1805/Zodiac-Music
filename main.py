import streamlit as st
from langchain_helper import get_song_recommendations

# ---  CONFIGURATION ---
st.set_page_config(page_title="StarTrack", page_icon="🎵")
st.title("🔮 Your Stars, Your Tracks")

# --- THE UI (Streamlit) ---

# Input: Dropdown ensures the user picks a valid sign
zodiac = st.selectbox(
    "Select your Zodiac Sign:",
    ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", 
     "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
)

language = st.selectbox(
    "Select your language:",
    ["Assamese", "Bengali", "Bodo", "Dogri", "English", "Gujarati", "Hindi", "Kannada", "Kashmiri", "Konkani", "Maithili", "Malayalam", "Manipuri", "Marathi", "Nepali", "Odia", "Punjabi", "Sanskrit", "Santali", "Sindhi", "Tamil", "Telugu", "Urdu"]
)

# Button to trigger the AI
if st.button("Get My Playlist 🎶"):
    with st.spinner(f"Consulting the stars for {zodiac}..."):
        try:
            result = get_song_recommendations(zodiac, language)
            st.markdown("### 🌟 Here is your Cosmic Playlist")
            st.write(result)
        except Exception as e:
            st.error(f"An error occurred: {e}")