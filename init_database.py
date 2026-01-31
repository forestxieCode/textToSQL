#!/usr/bin/env python3
"""Database initialization wrapper script."""
import sys
import os

# Add src to path for direct execution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from scripts.init_database import init_database

if __name__ == "__main__":
    init_database()
