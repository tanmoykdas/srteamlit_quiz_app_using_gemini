import os 
from google import genai
from dotenv import load_dotenv
import io
from gtts import gTTS

load_dotenv()
api_key=os.environ.get("GEMINI_API_KEY")
client= genai.Client(api_key=api_key)

def note_generator(images):
    prompt="""Summarize the picture in note format at maximum 100 words.
    make sure to add markdowd to differntiate different section."""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text

def audio_generarton(text):
    speech = gTTS(text, lang="en", slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)

    return audio_buffer

def quiz_generation(text, level):
    prompt="""Make some quize based on this note, 
    use proper markdown to better vizualize."""

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[text, f"{prompt} at {level} level."]
    )
    return response.text