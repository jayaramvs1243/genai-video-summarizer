import requests
import ollama

class OllamaClient:

    ZERO_SHOT_PROMPT_TEMPLATE = "Provide a concise summary of the following video transcript:\n\n{transcript}"

    SYSTEM_PROMPT = "You are an expert AI assistant specializing in summarizing video content. Your task is to extract the main points, key takeaways, and provide a highly readable and concise summary."
    USER_PROMPT_TEMPLATE = "Here is the transcript of the video:\n\n{transcript}\n\nPlease summarize this video."

    STRUCTURED_SYSTEM_PROMPT = '''
        You are an expert AI assistant specializing in summarizing video content. Your task is to extract the main points and key takeaways from the provided transcript. 
        You must respond STRICTLY in valid JSON format. Do not include any conversational text, markdown formatting, or explanations outside of the JSON object.
        The JSON object must perfectly adhere to the following schema:
        {
        "title": "A concise title for the video",
        "artist": "The name of the speaker or presenter in the video",
        "summary": "A highly readable and concise summary of the video content",
        "key_takeaways": [
            "Takeaway 1",
            "Takeaway 2",
            "Takeaway 3"
        ]
        }
    '''

    def __init__(self, host_url: str, model_name: str):
        self.host_url = host_url
        self.model_name = model_name

        self.base_url = f"{self.host_url}/api/generate"

    def summarize_with_requests(self, transcript: str) -> str:
        prompt = self.ZERO_SHOT_PROMPT_TEMPLATE.format(transcript=transcript)

        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.base_url, json=payload)
        response.raise_for_status()

        return response.json()['response']
    
    def summarize_with_ollama_pkg_zero_shot(self, transcript: str) -> str:
        client = ollama.Client(host=self.host_url)
        prompt = self.ZERO_SHOT_PROMPT_TEMPLATE.format(transcript=transcript)

        response = client.generate(
            model=self.model_name,
            prompt=prompt,
            stream=False
        )
        return response['response']
    
    def summarize_with_ollama_pkg_system_prompt(self, transcript: str) -> str:
        client = ollama.Client(host=self.host_url)
        prompt = self.USER_PROMPT_TEMPLATE.format(transcript=transcript)

        response = client.generate(
            model=self.model_name,
            system=self.SYSTEM_PROMPT,
            prompt=prompt,
            stream=False
        )
        return response['response']
    
    def summarize_with_ollama_pkg_structured_response(self, transcript: str) -> str:
        client = ollama.Client(host=self.host_url)

        response = client.generate(
            model=self.model_name,
            system=self.STRUCTURED_SYSTEM_PROMPT,
            prompt=transcript,
            stream=False,
            format="json"
        )
        return response['response']

