"""
AISOP Protocol — Command Line Interface
"""
import argparse
import sys
from pathlib import Path
from . import load, validate


def main():
    parser = argparse.ArgumentParser(description="AISOP Protocol CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    check_parser = subparsers.add_parser("check", help="Validate an AISOP file")
    check_parser.add_argument("file", help="Path to .aisop.json file")

    args = parser.parse_args()

    if args.command == "check":
        try:
            print(f"Loading {args.file}...")
            doc = load(args.file)
            name = doc.metadata.name or doc.metadata.id
            print(f"Schema Validation Passed: {name} (v{doc.metadata.version})")

            print("Running Convergence Checks...")
            validate(doc)
            print("Convergence Checks Passed.")

        except Exception as e:
            print(f"Validation Failed: {e}")
            sys.exit(1)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
