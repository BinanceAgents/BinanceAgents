from uagents import Model


class TranslationRequest(Model):
    text: str


class TranslationResponse(Model):
    translated_text: str


class Error(Model):
    error: str

# Updated: 2025-10-08T19:59:24.160894

# Updated: 2025-10-08T20:10:26.573458
