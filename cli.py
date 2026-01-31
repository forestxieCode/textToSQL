#!/usr/bin/env python3
"""CLI wrapper script."""
import sys
import os

# Add src to path for direct execution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from scripts.cli import main

if __name__ == "__main__":
    main()
