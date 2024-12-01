from openai import OpenAI


class AI_GPT4o:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o"

    def get_response(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system",
                     "content": """Te vagy az neved: 'AphoniaAI' gpt4-es modelje ami az openai-on alapul. Rövid válaszokat adsz és szépen kifejted és gyorsan a lényegre térsz, és TILOS markdown-t használnod. + Fel ruháztalak egy funkcíóval képes vagy képeket generálni, a '[image_gen: \"<ide a prompt>\"]' parancsal, a '[tts: \"<ide a prompt>\"]' parancsal viszont a Text to speech-t tudod használni! De magyarul adj válaszokat!!"""},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Hiba történt: {str(e)}"

    # History feature
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o"
        self.conversation_history = []  # Beszélgetési előzmények tárolása

    def get_response(self, prompt: str) -> str:
        try:
            messages = [
                {"role": "system",
                 "content": """Te vagy az neved: 'AphoniaAI' gpt4o-es modelje ami az openai-on alapul. Rövid válaszokat adsz és szépen kifejted és gyorsan a lényegre térsz, és TILOS markdown-t használnod. + Fel ruháztalak egy funkcíóval képes vagy képeket generálni, a '[image_gen: \"<ide a prompt>\"]' parancsal, a '[tts: \"<ide a prompt>\"]' parancsal viszont a Text to speech-t tudod használni! De magyarul adj válaszokat!!"""}
            ]

            messages.extend(self.conversation_history)

            messages.append({"role": "user", "content": prompt})

            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )

            assistant_response = response.choices[0].message.content
            self.conversation_history.append({"role": "user", "content": prompt})
            self.conversation_history.append({"role": "assistant", "content": assistant_response})

            return assistant_response

        except Exception as e:
            return f"Hiba történt: {str(e)}"

    def clear_history(self):
        self.conversation_history = []