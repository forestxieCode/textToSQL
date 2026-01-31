"""Setup configuration for text_to_sql package."""
from setuptools import setup, find_packages

setup(
    name="text_to_sql",
    version="1.0.0",
    description="LangGraph-based Text-to-SQL Agent",
    author="forestxieCode",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        line.strip()
        for line in open("requirements.txt").readlines()
        if line.strip() and not line.startswith("#")
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "text-to-sql=scripts.cli:main",
            "text-to-sql-demo=scripts.demo:main",
            "text-to-sql-init=scripts.init_database:main",
            "text-to-sql-visualize=scripts.visualize_workflow:visualize_workflow",
        ],
    },
)
