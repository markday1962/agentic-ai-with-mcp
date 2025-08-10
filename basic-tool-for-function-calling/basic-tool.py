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

