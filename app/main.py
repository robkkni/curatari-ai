import chainlit as cl
from app.agent.workflows import curatari_task

@cl.on_chat_start
async def on_chat_start():
    """Initialize the chat session"""
    await cl.Message(
        content="Welcome to Curatari AI. How can I assist you today?"
    ).send()

@cl.on_message
async def on_message(message: cl.Message):
    """Process incoming messages"""
    # Show thinking indicator
    thinking = cl.Message(content="", author="Curatari AI")
    await thinking.send()
    
    # Process the message with Langroid agent
    response = curatari_task.process_message(message.content)
    
    # Update the message with the response
    await thinking.update(content=response)

if __name__ == "__main__":
    # This is used when running locally with `chainlit run app/main.py`
    import os
    import dotenv
    
    dotenv.load_dotenv()
    cl.run()
