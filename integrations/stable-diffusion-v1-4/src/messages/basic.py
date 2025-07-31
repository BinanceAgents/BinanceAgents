from uagents import Model


class SDRequest(Model):
    image_desc: str


class Error(Model):
    error: str


class SDResponse(Model):
    image_data: str

# Updated: 2025-10-08T19:59:17.741084
