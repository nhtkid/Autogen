# filename: get_transcript.py

from youtube_transcript_api import YouTubeTranscriptApi

video_id = "NrQkdDVupQE"  # replace with your video id
transcript = YouTubeTranscriptApi.get_transcript(video_id)

for entry in transcript:
    print(entry['text'])