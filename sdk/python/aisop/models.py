from typing import List, Dict, Any, Optional, Union, Literal
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, field_validator, model_validator, ConfigDict

# --- Layer 2: Structure (Syntax) ---

class AISOPVersion(str, Enum):
    V1_0 = "1.0"

class ExecutionMode(str, Enum):
    DETERMINISTIC = "deterministic"
    PROBABILISTIC = "probabilistic"

class NodeType(str, Enum):
    ACTION = "ACTION"
    DECISION = "DECISION"
    SUB_SOP = "SUB_SOP"
    PARALLEL = "PARALLEL"
    END = "END" 

class RetryPolicy(BaseModel):
    max_attempts: int = Field(default=3, description="Maximum number of retry attempts")
    backoff_factor: float = Field(default=1.5, description="Multiplier for backoff delay")
    initial_delay_ms: int = Field(default=1000, description="Initial delay in milliseconds")

class ToolDependency(BaseModel):
    id: str
    uri: Optional[str] = None
    description: Optional[str] = None

class PromptDependency(BaseModel):
    id: str
    uri: Optional[str] = None
    description: Optional[str] = None

class Dependencies(BaseModel):
    tools: List[ToolDependency] = Field(default_factory=list)
    prompts: List[PromptDependency] = Field(default_factory=list)

class AgentRecord(BaseModel):
    engine: str
    model: Optional[str] = None
    success_rate: Optional[float] = Field(None, ge=0.0, le=1.0)
    date: Optional[str] = None

class EvolutionRecord(BaseModel):
    generation: Optional[int] = None
    parent_id: Optional[str] = None
    mutation_op: Optional[str] = None
    fitness_score: Optional[float] = None

class ActionDef(BaseModel):
    primitive: str = Field(..., description="e.g., sys.io.read_file, sys.resource.read")
    params: Dict[str, Any] = Field(default_factory=dict)
    
class Node(BaseModel):
    model_config = ConfigDict(extra='forbid')

    id: str = Field(..., description="Unique identifier within the SOP")
    type: NodeType
    name: str
    description: Optional[str] = None
    action: Optional[ActionDef] = None
    retry_policy: RetryPolicy = Field(default_factory=RetryPolicy)
    timeout_ms: int = Field(default=300000) 
    ui_pos: Optional[Dict[str, float]] = None 

    @model_validator(mode='after')
    def validate_action_requirement(self):
        if self.type == NodeType.ACTION and not self.action:
            raise ValueError("Node of type ACTION must have an 'action' definition.")
        return self

class Edge(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    from_node: str = Field(..., alias="from")
    to_node: str = Field(..., alias="to")
    condition: Optional[str] = Field(None, description="Expression for DECISION branches.")

class SOPMetadata(BaseModel):
    id: str = Field(..., description="Unique URI-like identifier")
    version: str = Field(..., description="Semantic version")
    name: str
    description: Optional[str] = None
    author: Optional[str] = None
    license: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    tested_agents: List[AgentRecord] = Field(default_factory=list)
    evolution: Optional[EvolutionRecord] = None

class VariableDef(BaseModel):
    name: str
    type: str = "string" 
    default: Optional[Any] = None
    description: Optional[str] = None

class Constraint(BaseModel):
    type: str 
    params: Dict[str, Any]

class SOP(BaseModel):
    """
    AISOP Protocol Document Root Object
    """
    model_config = ConfigDict(extra='ignore')

    aisop: AISOPVersion = AISOPVersion.V1_0
    mode: ExecutionMode = ExecutionMode.PROBABILISTIC
    metadata: SOPMetadata
    dependencies: Optional[Dependencies] = None
    variables: List[VariableDef] = Field(default_factory=list)
    nodes: List[Node]
    edges: List[Edge]
    constraints: List[Constraint] = Field(default_factory=list)

    @field_validator('nodes')
    @classmethod
    def ensure_unique_node_ids(cls, v: List[Node]) -> List[Node]:
        ids = [n.id for n in v]
        if len(ids) != len(set(ids)):
            raise ValueError("Node IDs must be unique within an SOP.")
        return v
    
    def get_node(self, node_id: str) -> Optional[Node]:
        for n in self.nodes:
            if n.id == node_id:
                return n
        return None
