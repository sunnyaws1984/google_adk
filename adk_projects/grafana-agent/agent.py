import os
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPServerParams
from .prompt import VALIDATOR_PROMPT

MCP_URL = os.environ.get("MCP_URL", "http://localhost:8000/mcp") #Make sure MCP is up and running

root_agent = LlmAgent(
    name="grafana_agent",
    model="gemini-2.5-flash",
    description="Execute Grafana MCP tools and intelligently refine the raw output for clarity and usefulness.",
    tools=[
        MCPToolset(
            connection_params=StreamableHTTPServerParams(
                url=MCP_URL
            )
        )
    ],
    instruction=VALIDATOR_PROMPT
)
