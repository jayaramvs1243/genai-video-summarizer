import requests
import ollama

class OllamaClient:

    PROMPT_TEMPLATE = "Provide a concise summary of the following video transcript:\n\n{transcript}"

    def __init__(self, host_url: str, model_name: str):
        self.host_url = host_url
        self.model_name = model_name

        self.base_url = f"{self.host_url}/api/generate"

    def summarize_with_requests(self, transcript: str) -> str:
        prompt = self.PROMPT_TEMPLATE.format(transcript=transcript)

        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.base_url, json=payload)
        response.raise_for_status()

        return response.json()['response']
    
    def summarize_with_ollama_pkg(self, transcript: str) -> str:
        client = ollama.Client(host=self.host_url)
        prompt = self.PROMPT_TEMPLATE.format(transcript=transcript)

        response = client.generate(model=self.model_name, prompt=prompt, stream=False)
        return response['response']
