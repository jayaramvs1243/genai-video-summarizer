# Video Summarizer

A Python command-line application that extracts transcripts from YouTube videos and generates concise summaries using a local Large Language Model (LLM) via [Ollama](https://ollama.com/).

## Features

- **Transcript Extraction**: Dynamically parses YouTube URLs to extract the video ID and fetch the transcript using `youtube-transcript-api`.
- **Local AI Summarization**: Keeps your data private and free by using local LLMs through Ollama.
- **CLI Interface**: Simple command-line execution with options to override the target model and Ollama server host.
- **Dual Client Implementation**: Demonstrates integrating with Ollama using both raw HTTP requests (`requests` library) and the official `ollama` Python package.

## Prerequisites

1. **Python 3.x**
2. **Ollama**: Install and run Ollama.
3. **An LLM Model**: Pull the model you want to use. The application defaults to `llama3.2`. 
   ```bash
   ollama pull llama3.2
   ```

## Installation

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone <your-repo-url>
   cd video-summarizer
   ```

2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   # venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the summarizer by passing a YouTube URL to the `main.py` script.

```bash
python main.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### CLI Options

You can customize the execution with optional flags:
- `--model`: Specify a different model (e.g., `--model mistral`). Default is `llama3.2`.
- `--host`: Provide a different Ollama server address (e.g., `--host http://192.168.1.50:11434`). Default is `http://localhost:11434`.