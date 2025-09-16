from uagents import Model


class UARequest(Model):
    text: str


class Error(Model):
    error: str


class UAResponse(Model):
    response: list

# Updated: 2025-10-08T19:59:27.839240

# Updated: 2025-10-08T20:10:24.364009
