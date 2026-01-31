"""
LangGraph Text-to-SQL Agent

A smart agent that converts natural language questions to SQL queries and executes them.
"""
from .core.agent import run_query, AgentState
from .core.sql_generator import create_sql_generator
from .database.manager import db_manager
from .utils.formatter import OutputFormatter
from .utils.logger import logger
from .utils.config import config
from .utils.exceptions import (
    TextToSQLError,
    DatabaseError,
    SchemaRetrievalError,
    SQLExecutionError,
    UnsafeQueryError,
    SQLGenerationError,
)

__version__ = "1.0.0"

__all__ = [
    "run_query",
    "AgentState",
    "create_sql_generator",
    "db_manager",
    "OutputFormatter",
    "logger",
    "config",
    "TextToSQLError",
    "DatabaseError",
    "SchemaRetrievalError",
    "SQLExecutionError",
    "UnsafeQueryError",
    "SQLGenerationError",
]
