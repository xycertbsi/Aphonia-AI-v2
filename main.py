
# egyeb
import art
import time
import os
from dotenv import load_dotenv
import requests

# Models
from textmodel_gpt3 import AI_GPT3
from textmodel_gpt4 import AI_GPT4
from textmodel_gpt4o import AI_GPT4o
from img_dall_e import Image
from text_to_speech import TextToSpeech

# .env load
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
AI_MODELTXT = os.getenv("AI_TXT_MODEL")
SETUPGET = os.getenv("SETUP")

# setup config
from setupSystem import SetupSys
setup = SetupSys()

print(art.text2art("Aphonia   AI"))
print("            By. XYCert | OpenAI | Python version")
print("")


# condezátorok
def gen_content(text: str) -> str:
    if "[image_gen: " in text and text.count("[image_gen: ") == 1:
        start = text.find("[image_gen: \"") + len("[image_gen: \"")
        end = text.find("\"]", start)
        if end != -1:
            return text[start:end]
    return ""
def txt_content(text: str) -> str:
    if "[tts: " in text and text.count("[tts: ") == 1:
        start = text.find("[tts: \"") + len("[tts: \"")
        end = text.find("\"]", start)
        if end != -1:
            return text[start:end]
    return ""

def translate(text: str) -> str:
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "hu",
        "tl": "en",
        "dt": "t",
        "q": text
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()[0][0][0]
        else:
            return "Fordítási hiba"
    except Exception as e:
        return f"Hiba: {str(e)}"

def main():
    print("< | Parancsok: /quit ; /setup | >")

    img_gen = Image()

    if AI_MODELTXT == "gpt-3.5-turbo":
        chat = AI_GPT3(API_KEY)
        ai_modelframe = "GPT-3.5"

    elif AI_MODELTXT == "gpt-4":
        chat = AI_GPT4(API_KEY)
        ai_modelframe = "GPT-4"

    elif AI_MODELTXT == "gpt-4o":
        chat = AI_GPT4o(API_KEY)
        ai_modelframe = "GPT-4o"

    else:
        print("! Érvénytelen szöveg model!", "Elérhető szöveg modellek: gpt-3.5-turbo, gpt-4, gpt-4o")
        print("> Megoldás: írd át a 'AI_TXT_MODEL'-t az elérhető szöveg modellek egyikére!")
        print("# Kilépés 5 másodperc múlva!")
        time.sleep(5)
        exit("cs")

    try:
        while True:
            user_input = input("> ")

            if user_input.lower() == '/quit':
                break

            elif user_input.lower() == "/setup":
                setup.first()

            if AI_MODELTXT == "gpt-3.5-turbo":
                chat.add_message(user_input)
                response = chat.get_completion()

            elif AI_MODELTXT == "gpt-4":
                response = chat.get_response(user_input)

            elif AI_MODELTXT == "gpt-4o":
                response = chat.get_response(user_input)

            image_prompt = gen_content(response)

            if image_prompt == "":
                pass
            else:
                img_gen.generate(translate(image_prompt))

            tts = txt_content(response)
            if tts == "":
                pass
            else:
                app = TextToSpeech()
                filename = app.generate(tts)
                print(f"A fájl mentve: '{filename}'!")


            print(f"{ai_modelframe} <|> {response}")

    except KeyboardInterrupt:
        print("\nProgram leállítva.")

    except Exception as e:
        print(f"\nHiba történt: {str(e)}")

if __name__ == "__main__":
    if SETUPGET == "yes":
        main()
    elif SETUPGET == "no":
        setup.first()
    else:
        setup.first()