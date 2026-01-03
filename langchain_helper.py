from my_secret_key import GEMINI_API_KEY
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

api_key = GEMINI_API_KEY

# --- THE LOGIC (LangChain + Gemini) ---
def get_song_recommendations(zodiac, language):
    
    # Initialize the Gemini Model
    # "gemini-1.5-flash" is faster and cheaper, "gemini-1.5-pro" is more creative
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=api_key,
        temperature = 0.9
    )

    # Create a prompt template
    # This instructs the AI on exactly how to behave
    prompt = ChatPromptTemplate.from_template(
        f"""
        You are a music taste expert and astrologer. Suggest 5 songs in {language} that perfectly match the vibe and personality of a {zodiac}.
        For each song, provide:
        1. Song Title - Artist
        2. A one-sentence explanation of why it fits this sign in the next line.
        Format the output as a clean list.
        """
    )

    # Create the chain: Prompt -> LLM
    chain = prompt | llm
    
    # Run the chain
    try:
        response = chain.invoke({"zodiac": zodiac})
        return response.content
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "Resource has been exhausted" in error_msg:
            return(
                "Oh! My powers are gone... I must revive myself with evil deeds which involve putting kids under spell and making them do atrocities!😈\n\nHaha don't worry the tokens ran out, try again tomorrow ✨"
            )


if __name__ == "__main__":
    print(get_song_recommendations("Taurus", "Hindi"))