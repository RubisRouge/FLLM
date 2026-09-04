from pydantic import BaseModel, Field
from enum import StrEnum
from typing import Annotated, Any, Literal, Union


class ToolsCallingMode(StrEnum):
    AUTO = "auto"
    ANY = "any"
    NONE = "none"


class Tool(BaseModel):
    type: Literal["Tool"] = "Tool"
    name: str
    description: str
    parameters: dict[str, Any]


class WebSearchTool(BaseModel):
    type: Literal["WebSearchTool"] = "WebSearchTool"
    exclude_domains: list[str] = []


ToolDefinition = Annotated[Union[Tool, WebSearchTool], Field(discriminator="type")]


class ToolsConfig(BaseModel):
    tools: list[ToolDefinition]
    parallel_calling: bool
    mode: ToolsCallingMode
