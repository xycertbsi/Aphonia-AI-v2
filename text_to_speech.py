from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


class TextToSpeech:
    def __init__(self):
        self.key = os.getenv('OPENAI_API_KEY')
        self.model = os.getenv('AUDIO_MODEL')
        self.client = OpenAI(api_key=self.key)

    def generate(self, prompt: str):
        if not prompt or not isinstance(prompt, str):
            raise ValueError("A promptnak egy nem üres szövegnek kell lennie")

        # Fájlnév generálás
        base_name = "speech"
        counter = 1
        file_name = f"{base_name}.mp3"

        # Ellenőrizzük, hogy létezik-e már ilyen nevű fájl
        while os.path.exists(file_name):
            file_name = f"{base_name}{counter}.mp3"
            counter += 1

        response = self.client.audio.speech.create(
            model="tts-1",
            voice=self.model,
            input=prompt
        )
        response.stream_to_file(file_name)
        return file_name  # Visszaadjuk az új fájl nevét