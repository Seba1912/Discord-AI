# translator.py
# -- Handles language detection and translation using Google Translator for 
# -- advanced translation.

from googletrans import Translator

translator = Translator()

def translate(text, target_lang="en"):
    try:
        result = translator.translate(text, dest=target_lang)
        return result.text
    except Exception as e:
        return text
