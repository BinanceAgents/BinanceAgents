from uagents import Model


class UARequest(Model):
    text: str


class Error(Model):
    error: str


class UAResponse(Model):
    response: list
# Updated: 2025-10-08T19:59:33.824278
