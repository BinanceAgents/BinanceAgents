from typing import Optional
from uagents import Model, Field


class RagRequest(Model):
    question: str = Field(
        description="The question that the user wants to have an answer for."
    )
    url: str = Field(description="The url of the docs where the answer is.")
    deep_read: Optional[str] = Field(
        description="Specifies weather all nested pages referenced from the starting URL should be read or not. The value should be yes or no.",
        default="no",
    )

# Updated: 2025-10-08T19:59:23.523283

# Updated: 2025-10-08T20:10:21.167784
