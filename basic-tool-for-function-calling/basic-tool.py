import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAPI_API_KEY")

# Initialise the LangChain LLM Client
from langchain_openapi import ChatOpenAI

llm = ChatOpenAI(
  model="gpt-4o",
  temperature=0.2,
  openai_api_key=api_key
)

# Basic tool for function calling
from langchain.tools import tool

@tool
def get_exchange_rate(from_currency: str, to_currency: str) -> str:
  """Returns a dummy exchnage rate between two currencies"""
  return f"1 {from_currency} = 1.09 {to_currency}"
