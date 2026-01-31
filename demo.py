#!/usr/bin/env python3
"""Demo wrapper script."""
import sys
import os

# Add src to path for direct execution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from scripts.demo import demo_agent_workflow

if __name__ == "__main__":
    demo_agent_workflow()
