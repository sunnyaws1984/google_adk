from google.adk.agents import Agent
from .sql_tools import run_sql  # import our function

root_agent = Agent(
    name="db_agent",
    model="gemini-2.5-flash",
    description="Agent that queries a MySQL database.",
    instruction="""
    You MUST use the run_sql tool to answer ALL user questions about the database.
    Never output SQL directly. Always call run_sql with the generated SQL query.

    Database schema:
    TABLE employees (
    id INT,
    name VARCHAR,
    department VARCHAR,
    salary INT
    )

    Do not guess column names

    """,
    tools=[run_sql]
)
