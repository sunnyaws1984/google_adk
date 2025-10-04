# Structured Outputs in ADK

This example demonstrates how to implement structured outputs in the Agent Development Kit (ADK) using Pydantic models. The main agent in this example, `email_generator`, uses the `output_schema` parameter to ensure its responses conform to a specific structured format.

## What are Structured Outputs?

ADK allows you to define structured data formats for agent inputs and outputs using Pydantic models:

1. **Controlled Output Format**: Using `output_schema` ensures the LLM produces responses in a consistent JSON structure
2. **Data Validation**: Pydantic validates that all required fields are present and correctly formatted
3. **Improved Downstream Processing**: Structured outputs are easier to handle in downstream applications or by other agents

Use structured outputs when you need guaranteed format consistency for integration with other systems or agents.

## Email Generator Example

In this example, we've created an email generator agent that produces structured output with:

1. **Email Subject**: A concise, relevant subject line
2. **Email Body**: Well-formatted email content with greeting, paragraphs, and signature

The agent uses a Pydantic model called `EmailContent` to define this structure, ensuring every response follows the same format.

### Output Schema Definition

The Pydantic model defines exactly what fields are required and includes descriptions for each:

```python
class EmailContent(BaseModel):
    """Schema for email content with subject and body."""
    
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive."
    )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greeting, paragraphs, and signature."
    )
```

### How It Works

1. The user provides a description of the email they need
2. The LLM agent processes this request and generates both a subject and body
3. The agent formats its response as a JSON object matching the `EmailContent` schema
4. ADK validates the response against the schema before returning it
5. The structured output is stored in the session state under the specified `output_key`

## Important Limitations

When using `output_schema`:

1. **No Tool Usage**: Agents with an output schema cannot use tools during their execution
2. **Direct JSON Response**: The LLM must produce a JSON response matching the schema as its final output
3. **Clear Instructions**: The agent's instructions must explicitly guide the LLM to produce properly formatted JSON

## Enter the below prompts to test in ADK UI:

Marketing / Outreach Emails

Try entering any of the following prompts in the ADK web UI:

New Subscription Plans:
Write a marketing email announcing our new subscription plans and their benefits.

Product Webinar Invite:
Draft an email inviting customers to join our upcoming product webinar.

Early Bird Promotion:
Create a promotional email offering a 20% discount for early bird sign-ups.

Product Launch Announcement:
Write an email introducing our latest product line and highlighting key features.

Customer Loyalty Thank You:
Compose an email thanking customers for their loyalty and sharing an exclusive offer.
