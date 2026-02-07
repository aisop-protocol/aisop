import json
from pathlib import Path
from typing import Union, Dict
from .models import SOP

def load(source: Union[str, Path, Dict]) -> SOP:
    """
    Load an SOP from a file path, JSON string, or dictionary.
    
    Args:
        source: File path (str/Path), JSON string, or dict.
        
    Returns:
        SOP: Validated AISOP object.
        
    Raises:
        ValidationError: If the input does not conform to AISOP schema.
    """
    if isinstance(source, (str, Path)):
        # Check if it's a file path
        path = Path(source)
        if path.is_file() or (str(source).endswith('.json') and len(str(source)) < 255): 
             # Heuristic: if it looks like a path and ends in json, try reading it.
             # If it fails, assume it's a JSON string.
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return SOP.model_validate(data)
            except OSError:
                pass # Fallback to treating as JSON string
    
    if isinstance(source, str):
        data = json.loads(source)
        return SOP.model_validate(data)
        
    if isinstance(source, dict):
        return SOP.model_validate(source)
        
    raise ValueError("Source must be a file path, JSON string, or dict.")

def validate(sop: SOP) -> bool:
    """
    Run Layer 4 Axiom Validations (Logic Layer).
    
    Args:
        sop: The SOP object to validate.
        
    Returns:
        True if valid. Raises exceptions if invalid.
    """
    # 1. Convergence Axiom: Check for dangling nodes
    # Build adjacency
    out_degree = {n.id: 0 for n in sop.nodes}
    for edge in sop.edges:
        if edge.from_node in out_degree:
            out_degree[edge.from_node] += 1
            
    # Check
    for node in sop.nodes:
        if node.type != "END" and out_degree[node.id] == 0:
             raise ValueError(f"Convergence Axiom Violation: Node '{node.id}' ({node.name}) has no outgoing edges but is not an END node.")
             
    # TODO: Add Causality and Acyclicity checks
    
    return True

def dump(sop: SOP, indent: int = 2) -> str:
    """
    Serialize SOP to JSON string.
    """
    return sop.model_dump_json(by_alias=True, indent=indent)
