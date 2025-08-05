from uagents import Model


class Request(Model):
    text: str


class Error(Model):
    error: str


class Data(Model):
    generated_text: str

# Updated: 2025-10-08T19:59:20.302541
