"""
AISOP Protocol — Python Data Models (Chat-Native Array Format)

Aligned with aisop.schema.json and SPEC.md v1.0.0.
"""
import re
from typing import Dict, List, Any, Optional, Literal
from pydantic import BaseModel, Field, field_validator


class Parameter(BaseModel):
    """Input parameter definition for an AISOP."""
    type: str = Field(..., description="Parameter type (string, integer, number, boolean, array, object)")
    description: str = Field(..., description="Parameter description")
    default: Optional[Any] = Field(None, description="Default value for this parameter")


class Metadata(BaseModel):
    """System message content — AISOP metadata and configuration."""
    protocol: Literal["AISOP V1.0.0"] = Field("AISOP V1.0.0", description="AISOP Protocol Version")
    id: str = Field(..., description="Unique identifier")
    version: str = Field(..., description="Semantic version + lifecycle stage (e.g. '1.0.0 stable')")
    name: Optional[str] = Field(None, description="Human-readable name")
    summary: str = Field(..., description="What this AISOP does")
    description: Optional[str] = Field(None, description="Detailed description")
    verified_on: List[str] = Field(default_factory=list, description="Verified agentic runtimes")
    tools: List[str] = Field(default_factory=list, description="Required capabilities")
    parameters: Dict[str, Parameter] = Field(default_factory=dict, description="Input parameters")
    system_prompt: str = Field(..., description="Shim prompt to run this AISOP")

    @field_validator('version')
    @classmethod
    def validate_version(cls, v: str) -> str:
        if not re.match(r'^[0-9]+\.[0-9]+\.[0-9]+ (stable|test|dev)$', v):
            raise ValueError(f"Version must match 'X.Y.Z (stable|test|dev)', got: {v}")
        return v


class UserContent(BaseModel):
    """User message content — instruction, AISOP logic flows, and functions."""
    instruction: str = Field(..., description="Entry-point directive (e.g. 'Execute aisop.main')")
    aisop: Dict[str, str] = Field(..., description="Mermaid graph definitions (must include 'main')")
    functions: Dict[str, Any] = Field(..., description="Step-Map function definitions")

    @field_validator('aisop')
    @classmethod
    def validate_aisop_has_main(cls, v: Dict[str, str]) -> Dict[str, str]:
        if 'main' not in v:
            raise ValueError("'aisop' must contain a 'main' entry-point graph.")
        return v


class AISopDocument(BaseModel):
    """AISOP Protocol Document — Chat-Native Array format [system, user]."""
    metadata: Metadata
    user_content: UserContent
