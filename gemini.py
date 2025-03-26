# ai_agent_builder/utils/gemini.py
import json
import os
import re

import google.generativeai as genai
from dotenv import load_dotenv
from google import genai as streaming_genai
from google.genai import types as streaming_types

# Load API KEY from .env
load_dotenv()

# Configure Gemini API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")

genai.configure(api_key=GOOGLE_API_KEY)


def generate_text(prompt: str, system_prompt: str = "") -> str:
    try:
        model = genai.GenerativeModel("gemini-2.0-flash-lite")
        # Prepare the messages payload
        messages = []
        if system_prompt:
            messages.append({"role": "user", "parts": [system_prompt]})
        messages.append({"role": "user", "parts": [prompt]})

        # Generate the response
        response = model.generate_content(messages)  # type: ignore

        # Check for safety rating or inappropriate content.
        if response.prompt_feedback:
            print(f"PROMPT FEEDBACK {response.prompt_feedback}")

        if not response.text:
            raise ValueError("Empty response from Gemini model.")
        # Print the response
        return response.text  # type: ignore

    except Exception as e:
        print(f"Gemini API Error : {e}")
        return f"Error generating text: {e}"


