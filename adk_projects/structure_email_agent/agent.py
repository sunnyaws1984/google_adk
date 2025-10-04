from google.adk.agents import LlmAgent
from pydantic import BaseModel, Field

# --- Define Output Schema ---
class EmailContent(BaseModel):
    subject: str = Field(
        description="Short and clear subject line that summarizes the support email."
    )
    body: str = Field(
        description="The full email message including greeting, helpful response, and closing signature."
    )


# --- Create Customer Support Email Agent ---
root_agent = LlmAgent(
    name="support_email_agent",
    model="gemini-2.0-flash",
    instruction="""
You are a Customer Support Email Assistant.
Your goal is to write professional, empathetic, and helpful emails in JSON format.

GUIDELINES:
- Keep messages polite, clear, and concise.
- Use actual line breaks in the email body for paragraphs, not '\\n'.
- Start with a warm greeting addressing the customer by name if provided.
- Acknowledge the customer's concern or request.
- Provide a clear solution or helpful information.
- End with a courteous closing (e.g., 'Best regards', 'Sincerely') and your name.
- Ensure the JSON is valid and properly formatted.

IMPORTANT:
Output MUST be valid JSON in this structure:
{
    "subject": "Short and clear subject line",
    "body": "Well-formatted email body using real line breaks for paragraphs"
}

DO NOT include explanations, markdown, or any extra text outside the JSON response.
""",
    description="Generates professional and empathetic customer support emails with clean formatting.",
    output_schema=EmailContent,
    output_key="email",
)