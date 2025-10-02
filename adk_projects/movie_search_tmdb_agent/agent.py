from google.adk.agents import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv
from .tools import get_movie_details


root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the get_movie_details tool.
    Use these movie IDs when the user mentions them:
    - Fight Club: 550
    - Inception: 27205
    - The Dark Knight: 155
    - The Matrix: 603
    - Interstellar: 157336
    """,
    tools=[get_movie_details]
)