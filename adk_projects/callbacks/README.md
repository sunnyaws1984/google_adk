# Callbacks in ADK

This example demonstrates how to use callbacks in the Agent Development Kit (ADK) to intercept and modify agent behavior at different stages of execution. Callbacks provide powerful hooks into the agent's lifecycle, allowing you to add custom logic for monitoring, logging, content filtering, and result transformation.

## What are Callbacks in ADK?

Callbacks are functions that execute at specific points in an agent's execution flow. They allow you to:

1. **Monitor and Log**: Track agent activity and performance metrics
2. **Filter Content**: Block inappropriate requests or responses
3. **Transform Data**: Modify inputs and outputs in the agent workflow
4. **Implement Security Policies**: Enforce compliance and safety measures
5. **Add Custom Logic**: Insert business-specific processing into the agent flow

ADK provides several types of callbacks that can be attached to different components of your agent system.

## Callback Parameters and Context

Each type of callback provides access to specific context objects that contain valuable information about the current execution state. Understanding these parameters is key to building effective callbacks.

### CallbackContext

The `CallbackContext` object is provided to all callback types and contains:

- **`agent_name`**: The name of the agent being executed
- **`invocation_id`**: A unique identifier for the current agent invocation
- **`state`**: Access to the session state, allowing you to read/write persistent data
- **`app_name`**: The name of the application
- **`user_id`**: The ID of the current user
- **`session_id`**: The ID of the current session


## Additional Resources

- [ADK Callbacks Documentation](https://google.github.io/adk-docs/callbacks/)
- [Types of Callbacks](https://google.github.io/adk-docs/callbacks/types-of-callbacks/)
- [Design Patterns and Best Practices](https://google.github.io/adk-docs/callbacks/design-patterns-and-best-practices/)
