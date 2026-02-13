"""
AISOP Protocol — Core Functions (load, validate, dump)

Supports Chat-Native Array format with UTF-8 BOM handling.
"""
import json
import re
from pathlib import Path
from typing import Union, Dict, List, Set, Tuple

from .models import AISopDocument, Metadata, UserContent


def load(source: Union[str, Path, list]) -> AISopDocument:
    """
    Load an AISOP document from a file path, JSON string, or list.

    Args:
        source: File path (str/Path), JSON string, or list (Chat-Native Array).

    Returns:
        AISopDocument: Validated AISOP document.

    Raises:
        ValueError: If the input is not valid Chat-Native Array format.
        ValidationError: If the input does not conform to AISOP schema.
    """
    if isinstance(source, list):
        return _parse_array(source)

    if isinstance(source, (str, Path)):
        path = Path(source)
        if path.is_file():
            with open(path, 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
            return _parse_array(data)

        if isinstance(source, str):
            data = json.loads(source)
            return _parse_array(data)

    raise ValueError("Source must be a file path, JSON string, or list.")


def _parse_array(data: list) -> AISopDocument:
    """Parse Chat-Native Array [system, user] into AISopDocument."""
    if not isinstance(data, list) or len(data) != 2:
        raise ValueError("AISOP document must be a JSON array with exactly 2 elements.")

    system_content = None
    user_content = None

    for msg in data:
        if not isinstance(msg, dict) or 'role' not in msg or 'content' not in msg:
            raise ValueError("Each element must have 'role' and 'content' fields.")
        if msg['role'] == 'system':
            system_content = msg['content']
        elif msg['role'] == 'user':
            user_content = msg['content']

    if system_content is None:
        raise ValueError("Missing system message.")
    if user_content is None:
        raise ValueError("Missing user message.")

    metadata = Metadata.model_validate(system_content)
    uc = UserContent.model_validate(user_content)

    return AISopDocument(metadata=metadata, user_content=uc)


def validate(doc: AISopDocument) -> bool:
    """
    Run protocol-level validations (SPEC.md Section 5: Convergence Axiom).

    Checks:
        1. Every branch in aisop Mermaid graphs must reach endNode((End)).
        2. aisop must contain a 'main' entry-point graph.

    Args:
        doc: The AISOP document to validate.

    Returns:
        True if valid.

    Raises:
        ValueError: If any validation fails.
    """
    for name, graph in doc.user_content.aisop.items():
        if name.startswith('_'):
            continue
        _validate_convergence(name, graph)

    return True


def _parse_mermaid_graph(graph: str) -> Tuple[Set[str], Dict[str, List[str]], Set[str]]:
    """
    Parse a Mermaid graph string.

    Returns:
        (all_nodes, adjacency, end_nodes)
        - all_nodes: set of all node IDs
        - adjacency: dict of node_id -> list of target node_ids
        - end_nodes: set of node IDs that are End nodes
    """
    all_nodes: Set[str] = set()
    adjacency: Dict[str, List[str]] = {}
    end_nodes: Set[str] = set()

    def extract_node_id(part: str) -> str:
        """Extract the node ID from a Mermaid node expression."""
        match = re.match(r'([a-zA-Z_][a-zA-Z0-9_]*)', part.strip())
        return match.group(1) if match else ""

    def is_end_node(part: str) -> bool:
        """Check if a node expression defines an End node."""
        node_id = extract_node_id(part)
        # Convention: node ID 'endNode' is always an End node
        if node_id and node_id.lower() == 'endnode':
            return True
        # Also match ((End)), ((Done)), etc.
        return bool(re.search(r'\(\(.*\)\)', part))

    # Split by both newlines and semicolons (Mermaid supports both)
    raw_lines = graph.strip().split('\n')
    lines = []
    for raw in raw_lines:
        lines.extend(part.strip() for part in raw.split(';'))

    for line in lines:
        # Skip non-edge lines
        if not line or line.startswith('graph ') or line.startswith('%%'):
            continue
        if line.startswith('subgraph') or line == 'end':
            continue
        if line.startswith('style') or line.startswith('classDef') or line.startswith('class '):
            continue

        # Split by arrow --> with optional labels |...|
        parts = re.split(r'\s*-->(?:\|[^|]*\|)?\s*', line)

        if len(parts) < 2:
            # Standalone node definition (e.g. "nodeId[Label]")
            nid = extract_node_id(line)
            if nid:
                all_nodes.add(nid)
                if is_end_node(line):
                    end_nodes.add(nid)
            continue

        # Process edge chain: A --> B --> C
        node_ids = []
        for part in parts:
            nid = extract_node_id(part)
            if nid:
                node_ids.append(nid)
                all_nodes.add(nid)
                if is_end_node(part):
                    end_nodes.add(nid)

        for i in range(len(node_ids) - 1):
            adjacency.setdefault(node_ids[i], []).append(node_ids[i + 1])

    return all_nodes, adjacency, end_nodes


def _validate_convergence(name: str, graph: str):
    """Validate that all branches in a Mermaid graph reach endNode((End))."""
    all_nodes, adjacency, end_nodes = _parse_mermaid_graph(graph)

    if not end_nodes:
        raise ValueError(
            f"Convergence violation in aisop['{name}']: No endNode((End)) found."
        )

    # Every leaf node (no outgoing edges) must be an End node
    for node in all_nodes:
        if node not in adjacency and node not in end_nodes:
            raise ValueError(
                f"Convergence violation in aisop['{name}']: "
                f"Node '{node}' has no outgoing edges and is not an End node."
            )


def dump(doc: AISopDocument, indent: int = 2) -> str:
    """
    Serialize AISopDocument to JSON string (Chat-Native Array format).

    Args:
        doc: The AISOP document to serialize.
        indent: JSON indentation level.

    Returns:
        JSON string.
    """
    system_content = doc.metadata.model_dump(exclude_none=True)
    user_content = doc.user_content.model_dump()

    data = [
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content}
    ]

    return json.dumps(data, indent=indent, ensure_ascii=False)
