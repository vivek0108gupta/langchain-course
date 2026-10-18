
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools  import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


load_dotenv()
# tavily=TavilyClient()
# @tool
# def search(query: str) -> str:
#     return tavily.search(query=query)


llm = ChatOpenAI(model='gpt-4o-mini', temperature=0.7, max_tokens=500)
tools = [TavilySearch]
agent = create_agent(llm=llm, tools=tools)


def agent() -> None:
    print("Hello from langchain-course!")  
    agent_response = agent.invoke([HumanMessage(content="Search for the latest news on AI")])
    print(agent_response.content) 


if __name__ == "__agent__":
    agent()