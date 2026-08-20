from typing import Literal
from typing import Union
from typing_extensions import Annotated

from pydantic import BaseModel, Field


class TextDelta(BaseModel):
    type: Literal["TextDelta"] = "TextDelta"
    text: str


class ThinkingDelta(BaseModel):
    type: Literal["ThinkingDelta"] = "ThinkingDelta"
    thinking: str


class MediaDelta(BaseModel):
    type: Literal["MediaDelta"] = "MediaDelta"
    media_type: str
    data: str


class StreamDelta(BaseModel):
    type: Literal["StreamDelta"] = "StreamDelta"
    delta: Annotated[
        Union[TextDelta, ThinkingDelta, MediaDelta], Field(discriminator="type")
    ]
