import uuid
import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from question_answer_agent import question_answer_agent
from session_store import save_session, load_session

load_dotenv()

async def main():
    # Initialize in-memory session service for stateful interactions
    session_service_stateful = InMemorySessionService()
    APP_NAME = "Aarav Bot"
    USER_ID = "aarav_sharma"

    # Try to load an existing session from disk
    existing_session = load_session()

    if existing_session:
        # Session exists locally; load it into memory so the Runner can use it
        print("LOADED EXISTING SESSION:")
        SESSION_ID = existing_session["session_id"]
        print("Session ID:", SESSION_ID)
        state = existing_session["state"]
        
        # Create/load session in memory with the previously saved state
        await session_service_stateful.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            session_id=SESSION_ID,
            state=state,
        )
    else:
        # No existing session; create a new one with initial state
        print("CREATED NEW SESSION:")
        SESSION_ID = str(uuid.uuid4())
        print("Session ID:", SESSION_ID)
        state = {
            "user_name": "Aarav Sharma",
            "user_preferences": """
                I love playing cricket, badminton, and football.
                My favorite food is paneer butter masala with naan.
                My favorite movie is 3 Idiots.
                I enjoy exploring hill stations like Manali and Munnar.
                I like chai more than coffee and enjoy reading about Indian history.
                I love doing coding in Java.
            """,
        }  # State stores all information about the user or conversation across interactions

        # Store the new session in memory
        await session_service_stateful.create_session(
             app_name=APP_NAME,
             user_id=USER_ID,
             session_id=SESSION_ID,
             state=state,
         )

    # Initialize the Runner (agent executor) with the session service
    runner = Runner(
        agent=question_answer_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful,
    )

    # Example user query
    new_message = types.Content(
        role="user",
        parts=[types.Part(text="Can you tell me Aarav favorite coding langauge ?")],
    )

    # Explanation of types:
    # - types → library with message tools
    # - Content → a complete message (role + message parts)
    # - Part → a single piece of the message (usually text)


    #This starts the agent and tells who the user is (USER_ID) & which session/chat it belongs to i.e SESSION_ID

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        # Only handle the final response from the agent
        #print ("event",event)
        if event.is_final_response():
            if event.content and event.content.parts:
                # Print the text of the first part of the response
                print(f"Final Response: {event.content.parts[0].text}")
        #event → bot’s response event
        #is_final_response() → checks if the bot finished replying
        #event.content → structured message object (Content)
        #event.content.parts → list of message parts, each with text

    # Retrieve the updated session state from memory
    session = await session_service_stateful.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    # Save the updated session state to disk for future runs
    save_session(APP_NAME, USER_ID, SESSION_ID, session.state)

if __name__ == "__main__":
    asyncio.run(main())
