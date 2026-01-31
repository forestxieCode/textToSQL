#!/usr/bin/env python3
"""Test database wrapper script."""
import sys
import os

# Add src to path for direct execution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from tests.test_database import test_database_queries

if __name__ == "__main__":
    test_database_queries()
