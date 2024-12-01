import os
from dotenv import load_dotenv
import requests
from openai import OpenAI

load_dotenv()

class Image:
    def __init__(self):
        pass

    def download_image(self, image_url, save_path):
        save_path = save_path.replace(" ", "_") \
            .replace(".", "") \
            .replace("'", "") \
            .replace('"', "")

        try:
            response = requests.get(image_url)
            response.raise_for_status()

            with open(save_path + ".jpg", 'wb') as file:
                file.write(response.content)

            print(f"Kép sikeresen generáláva: {save_path}.jpg")

        except requests.exceptions.RequestException as e:
            print(f"Hiba történt a kép generálása közben: {e}")

    def generate(self, prompt):
        api_key = os.getenv('OPENAI_API_KEY')
        model = os.getenv('AI_IMAGE_MODEL')

        client = OpenAI(api_key=api_key)

        response = client.images.generate(
            model=model,
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        image_url = response.data[0].url

        self.download_image(image_url, prompt)
