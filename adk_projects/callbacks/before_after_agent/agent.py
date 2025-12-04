from google.adk.agents import LlmAgent

def before(callback_context):
    print(">>> BEFORE: Agent started processing.")

def after(callback_context):
    print("<<< AFTER: Agent finished processing.")

root_agent = LlmAgent(
    name="logger_agent",
    model="gemini-2.0-flash",
    description="Agent with minimal logging callbacks",
    instruction="You are a friendly greeting agent.",
    before_agent_callback=before,
    after_agent_callback=after,
)

