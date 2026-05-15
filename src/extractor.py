from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

class YouTubeExtractor:
    """
    A class to extract and format transcripts from a YouTube video URL.
    """

    def __init__(self, url):
        self.url = url
        self.formatter = TextFormatter()

        self.video_id = self._extract_video_id()

    def _extract_video_id(self) -> str:
        """
        Extracts the video ID from the YouTube URL.

        Returns:
            str: The video ID extracted from the URL.
        """
        parsed_url = urlparse(self.url)

        if parsed_url.scheme not in ["http", "https"]:
            raise ValueError("Invalid URL: URL must start with http:// or https://")
        
        if parsed_url.hostname in ["youtu.be"]:
            return parsed_url.path[1:]  # Remove the leading '/' from the path to get the video ID

        if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
            query_params = parse_qs(parsed_url.query)
            video_id = query_params.get("v")
            if video_id:
                return video_id[0]
        
        raise ValueError("Invalid YouTube URL: Video ID not found.")

    def extract(self) -> str:
        """
        Fetches the transcript for a given YouTube video ID.

        Returns:
            str: The full text transcript of the video.
            
        Raises:
            Exception: If the transcript cannot be retrieved.
        """
        try:
            # Fetch the raw transcript using the YouTubeTranscriptApi
            raw_transcript = YouTubeTranscriptApi().fetch(video_id=self.video_id)

            # Format the transcript into a single readable string; using the TextFormatter
            formatted_transcript = self.formatter.format_transcript(raw_transcript)

            return formatted_transcript
        except Exception as e:
            raise Exception(f"Error fetching transcript for video id: {self.video_id}. Error: {str(e)}")
