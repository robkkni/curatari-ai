# app.py
import os
import chainlit as cl
from langroid.agent.chat_agent import ChatAgent, ChatAgentConfig
from langroid.language_models.openai_gpt import OpenAIChatModel, OpenAIGPTConfig

config = ChatAgentConfig(
    llm=OpenAIGPTConfig(
        api_key=os.getenv("OPENAI_API_KEY"),
        chat_model="gpt-4-turbo",
    )
)

agent = ChatAgent(config=config)

@cl.on_message
async def on_message(msg: cl.Message):
    response = await cl.make_async(agent.llm_response)(msg.content)
    await cl.Message(content=response.content).send()
