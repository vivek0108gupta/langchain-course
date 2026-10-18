
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools  import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel, Field

class Source(BaseModel):
    """Schema for a source of information."""
    url: str = Field(description="The URL of the source.")

class AgentResponse(BaseModel):
    """Schema for the agent's response."""
    answer: str = Field(description="The agent's answer to the query.")
    sources: List[Source] = Field(default_factory=list, description="A list of sources used to generate the answer.") 

load_dotenv()
# tavily=TavilyClient()
# @tool
# def search(query: str) -> str:
#     return tavily.search(query=query)


llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.7, max_tokens=500)
tools = [TavilySearch]
agent = create_agent(llm=llm, tools=tools, response_schema=AgentResponse)


def agent() -> None:
    print("Hello from langchain-course!")  
    agent_response = agent.invoke([HumanMessage(content="Search for the latest news on AI")])
    print(agent_response.content) 


if __name__ == "__agent__":
    agent()