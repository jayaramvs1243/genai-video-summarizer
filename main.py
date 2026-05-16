import json
import argparse
from src.extractor import YouTubeExtractor
from src.llm_client import OllamaClient

def main():
    parser = argparse.ArgumentParser(description="Summarize a YouTube video using Ollama.")
    parser.add_argument("url", help="The URL of the YouTube video to summarize")
    parser.add_argument("--host", default="http://localhost:11434", help="Ollama host URL")
    parser.add_argument("--model", default="llama3.2", help="Ollama model to use")
    args = parser.parse_args()

    extractor = YouTubeExtractor(url=args.url)

    try:
        print(f"Extracting transcript for {args.url}...")
        transcript = extractor.extract()

        llm_client = OllamaClient(host_url=args.host, model_name=args.model)

        print("Generating summary...")
        transcript_summary = llm_client.summarize_with_requests(transcript)
        print(f"\nSummary from the API request:\n{transcript_summary}")

        transcript_summary = llm_client.summarize_with_ollama_pkg_zero_shot(transcript)
        print(f"\nSummary from the Ollama package (Zero Shot):\n{transcript_summary}")

        transcript_summary = llm_client.summarize_with_ollama_pkg_system_prompt(transcript)
        print(f"\nSummary from the Ollama package (System Prompt):\n{transcript_summary}")

        transcript_summary = llm_client.summarize_with_ollama_pkg_structured_response(transcript)
        transcript_summary_json = json.loads(transcript_summary)
        print(f"\nSummary from the Ollama package (Structured Response):\n{json.dumps(transcript_summary_json, indent=2)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
