import unittest
import json
from aisop import load, validate, SOP
from aisop.models import NodeType

class TestAISOPBasic(unittest.TestCase):
    
    def test_load_hello_world(self):
        """Test loading a valid minimal SOP"""
        json_str = """
        {
            "aisop": "1.0",
            "metadata": {
                "id": "test.1",
                "version": "1.0.0",
                "name": "Test",
                "description": "A valid test SOP"
            },
            "nodes": [
                {
                    "id": "n1", "type": "ACTION", "name": "A",
                    "action": { "primitive": "sys.log" }
                },
                { "id": "end", "type": "END", "name": "Z" }
            ],
            "edges": [
                { "from": "n1", "to": "end" }
            ]
        }
        """
        sop = load(json_str)
        self.assertIsInstance(sop, SOP)
        self.assertEqual(sop.metadata.id, "test.1")
        self.assertEqual(len(sop.nodes), 2)
        
    def test_validation_convergence_axiom(self):
        """Test that the validator catches dangling nodes (Convergence Axiom)"""
        # Node 'n1' has no outgoing edge and is not END
        json_str = """
        {
            "aisop": "1.0",
            "metadata": { "id": "test.fail", "version": "1.0.0", "name": "Fail", "description": "Invalid SOP" },
            "nodes": [
                { "id": "n1", "type": "ACTION", "name": "A", "action": { "primitive": "sys.log" } }
            ],
            "edges": []
        }
        """
        sop = load(json_str)
        with self.assertRaises(ValueError) as cm:
            validate(sop)
        self.assertIn("Convergence Axiom", str(cm.exception))

    def test_unique_ids(self):
        """Test that duplicate node IDs are rejected by Pydantic"""
        json_str = """
        {
            "aisop": "1.0",
            "metadata": { "id": "test.dup", "version": "1.0.0", "name": "Dup", "description": "Duplicate IDs" },
            "nodes": [
                { "id": "A", "type": "END", "name": "End1" },
                { "id": "A", "type": "END", "name": "End2" } 
            ],
            "edges": []
        }
        """
        with self.assertRaises(Exception):
            load(json_str)

if __name__ == '__main__':
    unittest.main()
