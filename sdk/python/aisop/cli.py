import argparse
import sys
from pathlib import Path
from . import load, validate

def main():
    parser = argparse.ArgumentParser(description="AISOP Protocol CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # check command
    check_parser = subparsers.add_parser("check", help="Validate an AISOP file")
    check_parser.add_argument("file", help="Path to .aisop.json file")
    
    args = parser.parse_args()
    
    if args.command == "check":
        try:
            print(f"Loading {args.file}...")
            sop = load(args.file)
            print(f"✅ Schema Validation Passed: {sop.metadata.name} (v{sop.metadata.version})")
            
            print("Running Layer 4 Axiom Checks...")
            validate(sop)
            print("✅ Axiom Checks Passed.")
            
        except Exception as e:
            print(f"❌ Validation Failed: {str(e)}")
            sys.exit(1)
            
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
