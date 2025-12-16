from agno.agent import Agent
from agno.models.ollama import Ollama 
from tools.search import duckduckgo_search
from tools.finance import get_stock_price

llm = Ollama(
    # model="llama3.1",
    id="llama3.1",
    #id="phi3:mini",
    # temperature=0.2
)


agent = Agent(
    name="Local Research & Finance Agent",
    model=llm,
    tools=[duckduckgo_search, get_stock_price],
    # instructions="""
    # Before doing anything:
    # - Say what you plan to do in one short sentence.
    # Then execute tools.
    # Then give the final answer.
    # You are a local AI agent.
    # Use duckduckgo_search for web research.
    # Use get_stock_price for financial data.
    # Be concise and accurate.
    # """,
    instructions="""
    Decide quickly.
    If the question is about stock price, call get_stock_price immediately.
    """,
    # show_tool_calls=True,
    markdown=True,
    # reasoning="tree-of-thoughts",
    stream_intermediate_steps=True,
)
