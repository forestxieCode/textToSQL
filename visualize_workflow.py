#!/usr/bin/env python3
"""Visualize workflow wrapper script."""
import sys
import os

# Add src to path for direct execution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from scripts.visualize_workflow import visualize_workflow

if __name__ == "__main__":
    visualize_workflow()
