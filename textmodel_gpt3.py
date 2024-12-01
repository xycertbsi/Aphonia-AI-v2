import requests
import json
from typing import List, Dict, Optional


class AI_GPT3:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.api_url = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        self.conversation_history: List[Dict[str, str]] = []
        self.add_system_message()

    def add_message(self, content: str, role: str = "user") -> None:
        self.conversation_history.append({"role": role, "content": content})

    def add_system_message(self) -> None:
        self.conversation_history.append({"role": "system", "content": """Te vagy az neved: 'AphoniaAI' gpt3-es modelje ami az openai-on alapul. Rövid válaszokat adsz és szépen kifejted és gyorsan a lényegre térsz, és TILOS markdown-t használnod. + Fel ruháztalak egy funkcíóval képes vagy képeket generálni, a '[image_gen: \"<ide a prompt>\"]' parancsal, a '[tts: \"<ide a prompt>\"]' parancsal viszont a Text to speech-t tudod használni! De magyarul adj válaszokat!!"""})

    def clear_history(self) -> None:
        self.conversation_history = []
        self.add_system_message()

    def get_completion(
            self,
            temperature: float = 0.7,
            max_tokens: Optional[int] = None,
            stream: bool = False
    ) -> str:
        data = {
            "model": "gpt-3.5-turbo",
            "messages": self.conversation_history,
            "temperature": temperature,
            "stream": stream
        }

        if max_tokens:
            data["max_tokens"] = max_tokens

        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=data
            )

            response.raise_for_status()
            result = response.json()

            assistant_message = result["choices"][0]["message"]["content"]
            self.add_message(assistant_message, role="assistant")

            return assistant_message

        except requests.exceptions.RequestException as e:
            return f"Hiba történts: {str(e)}"