from uagents import Model


class AudioTranscriptRequest(Model):
    audio_data: str


class Error(Model):
    error: str


class AudioTranscriptResponse(Model):
    transcript: str

# Updated: 2025-10-08T19:59:25.443005
