from enum import StrEnum
from typing import Any
from typing import Annotated
from typing import Literal
from typing import Union

from pydantic import BaseModel
from pydantic import Field


class Base64Source(BaseModel):
    type: Literal["Bytes"] = "Bytes"
    data: str


class UrlSource(BaseModel):
    type: Literal["URL"] = "URL"
    url: str


class ReferenceSource(BaseModel):
    type: Literal["Reference"] = "Reference"
    id: str


MediaSource = Annotated[
    Union[Base64Source, UrlSource, ReferenceSource], Field(discriminator="type")
]


class TextContent(BaseModel):
    type: Literal["TextContent"] = "TextContent"
    text: str


class MediaContent(BaseModel):
    type: Literal["MediaContent"] = "MediaContent"
    media_type: str
    source: MediaSource
    title: str | None = None


class ToolCallContent(BaseModel):
    type: Literal["ToolCallContent"] = "ToolCallContent"
    id: str
    name: str
    arguments: dict[str, Any]
    thought_signature: str | None = None


class ToolResponseContent(BaseModel):
    type: Literal["ToolResponseContent"] = "ToolResponseContent"
    tool_call_id: str
    content: str
    is_error: bool = False


class ThinkingContent(BaseModel):
    type: Literal["ThinkingContent"] = "ThinkingContent"
    thinking: str
    signature: str | None = None


class ErrorContent(BaseModel):
    type: Literal["ErrorContent"] = "ErrorContent"
    message: str


Content = Annotated[
    Union[
        TextContent,
        MediaContent,
        ToolCallContent,
        ToolResponseContent,
        ThinkingContent,
        ErrorContent,
    ],
    Field(discriminator="type"),
]


class MessageSource(StrEnum):
    USER = "user"
    MODEL = "model"
    SYSTEM = "system"
    TOOL = "tool"


class Message(BaseModel):
    source: MessageSource
    contents: list[Content]
