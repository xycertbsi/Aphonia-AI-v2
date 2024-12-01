
# dotenv
import os
from dotenv import load_dotenv, set_key

load_dotenv()
AITextCheck = os.getenv("AI_TXT_MODEL")
AIImageCheck = os.getenv("AI_IMAGE_MODEL")
AIAudioCheck = os.getenv("AUDIO_MODEL")

import time

class SetupSys:
    def __init__(self):
        pass

    def second_TxTm(self):
        print("----------> | Felolvassó Model Setup | <----------")
        print("[1] Nova [lány] (alapértelmezett)")
        print("[2] Onyx [fiú]")
        print("[3] Alloy [fiú]")
        print("[4] Echo [fiú]")
        print("[5] Fable [fiú]")
        print("[6] Shimmer [fiú]")
        print("[0] Vissza!")
        user_input = input("Válassz > ")

        if user_input == "1":
            set_key(".env", "AUDIO_MODEL", "nova")
            os.environ['AUDIO_MODEL'] = 'nova'

        elif user_input == "2":
            set_key(".env", "AUDIO_MODEL", "onyx")
            os.environ['AUDIO_MODEL'] = 'onyx'

        elif user_input == "3":
            set_key(".env", "AUDIO_MODEL", "alloy")
            os.environ['AUDIO_MODEL'] = 'alloy'

        elif user_input == "4":
            set_key(".env", "AUDIO_MODEL", "echo")
            os.environ['AUDIO_MODEL'] = 'echo'

        elif user_input == "5":
            set_key(".env", "AUDIO_MODEL", "fable")
            os.environ['AUDIO_MODEL'] = 'fable'

        elif user_input == "6":
            set_key(".env", "AUDIO_MODEL", "shimmer")
            os.environ['AUDIO_MODEL'] = 'shimmer'


        elif user_input == "0":
            self.first()

        else:
            print("! Érvénytelen választás!")
            self.second_TxTm()

        print("Beállítva! > ")
        self.first()

    def second_Tm(self): # szöveg modell
        print("----------> | Szöveg Model Setup | <----------")
        print("[1] GPT-4o")
        print("[2] GPT-4")
        print("[3] GPT-3.5")
        print("[0] Vissza!")
        user_input = input("Válassz > ")

        if user_input == "1":
            set_key(".env", "AI_TXT_MODEL", "gpt-4o")
            os.environ['AI_TXT_MODEL'] = 'gpt-4o'

        elif user_input == "2":
            set_key(".env", "AI_TXT_MODEL", "gpt-4")
            os.environ['AI_TXT_MODEL'] = 'gpt-3.5-turbo'

        elif user_input == "3":
            set_key(".env", "AI_TXT_MODEL", "gpt-3.5-turbo")
            os.environ['AI_TXT_MODEL'] = 'gpt-3.5-turbo'

        elif user_input == "0":
            self.first()

        else:
            print("! Érvénytelen választás!")
            self.second_Tm()

        print("Beállítva!")
        self.first()


    def second_Im(self): # image modell
        print("----------> | Image Model Setup | <----------")
        print("[1] DALL-E 3")
        print("[2] DALL-E 2")
        print("[0] Vissza!")
        user_input = input("Válassz > ")

        if user_input == "1":
            set_key(".env", "AI_IMAGE_MODEL", "dall-e-3")
            os.environ['AI_IMAGE_MODEL'] = 'dall-e-3'

        elif user_input == "2":
            set_key(".env", "AI_IMAGE_MODEL", "dall-e-2")
            os.environ['AI_IMAGE_MODEL'] = 'dall-e-2'

        elif user_input == "0":
            self.first()

        else:
            print("! Érvénytelen választás!")
            self.second_Tm()

        print("Beállítva!")
        self.first()


    def first(self):
        AITextCheck = os.getenv("AI_TXT_MODEL")
        AIImageCheck = os.getenv("AI_IMAGE_MODEL")
        AIAudioCheck = os.getenv("AUDIO_MODEL")

        def checkTXT():
            if AITextCheck == "":
                return "Nincs beállítva"
            else:
                return "Kész"

        def checkIMG():
            if AIImageCheck == "":
                return "Nincs beállítva"
            else:
                return "Kész"

        def checkAudi(): # ;) audi xd
            if AIAudioCheck == "":
                return "Nincs beállítva"
            else:
                return "Kész"


        print("")
        print("----------> Setup <----------")
        print(f"[1] Szöveg model beálítása ({checkTXT()})")
        print(f"[2] Image model beállítása ({checkIMG()})")
        print(f"[3] Felolvasás model beállítása ({checkAudi()})")
        if AITextCheck == "" and AIImageCheck == "" and AIAudioCheck == "":
            pass
        elif AITextCheck == "" or AIImageCheck == "" or AIAudioCheck == "":
            pass
        elif AITextCheck != "" and AIImageCheck != "" and AIAudioCheck != "":
            print("[4] Setup befejezése")

        print("[0] Setup megszakítása")

        user_input = input("Válassz > ")

        if user_input.lower() == "1": self.second_Tm() # szöveg modell
        elif user_input.lower() == "2": self.second_Im() # image modell
        elif user_input.lower() == "3": self.second_TxTm() # audio modell

        elif user_input.lower() == "4":
            set_key(".env", "SETUP", "yes")
            os.environ['SETUP'] = 'yes' # biztonság kedvért  :D

        elif user_input.lower() == "0":
            confirm = input("Biztos? [I/N]: ")
            if confirm == "i" or confirm == "I":
                print("jó cs")
                exit()
            else:
                print("Azé :D")
                self.first()
        else:
            print("! Érvénytelen választás!")
            self.first()

        OpenAIKey = os.getenv("OPENAI_API_KEY")

        if OpenAIKey == "":
            print("! Határozz meg egy API kulcsot a .env-ben! SZÜKSÉGES A MÜKÖDÉSHEZ")
            asd = input("Nyomj entert ha kész vagy! ")

            if asd == "fekfoeofjeopfjoejfoejofsjeofjsoefjosefosjfoejofjs":
                pass
            else:
                print("Biztosan meg határozttad? Útolsó figyelmeztetés!")
                input("Nyomj entert... ")

                print("# Na most, índísd újra a programot! (Automatikus bezárás 10 másodperc múlva ;) )")

                time.sleep(10)
                exit("Nyan kedv")

        else:
            print("# Na most, índísd újra a programot! (Automatikus bezárás 10 másodperc múlva ;) )")

            time.sleep(10)
            exit("Nyan kedv")