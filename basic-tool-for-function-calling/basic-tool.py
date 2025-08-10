import os
from langchain.agents import initialize_agent, AgentType
from langchain_openapi import ChatOpenAI
from langchain.tools import tool

from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAPI_API_KEY")

# Initialise the LangChain LLM Client
llm = ChatOpenAI(
  model="gpt-4o",
  temperature=0.2,
  openai_api_key=api_key
)


# Basic tool for function calling
@tool
def get_exchange_rate(from_currency: str, to_currency: str) -> str:
  """Returns a dummy exchange rate between two currencies"""
  return f"1 {from_currency} = 1.09 {to_currency}"


def agent_executor():
  tools = [get_exchange_rate]
  agent = initialize.agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS)
  response = agent.run("Convert USD to EUR")
  print(response)


if __name__ == "__main__":
  agent_executor()
  
