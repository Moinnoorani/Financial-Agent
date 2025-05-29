import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OPENAI_API_KEY is not set!")

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

# web serach agent 
websearch_agent = Agent(
    name="webs_earch_agent",
    role="Search the web dor the information",
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[DuckDuckGo()],
    instructions=["Always include sources in your answer."],
    markdown=True,
    
)

# financial agent
fianace_agent = Agent(
    name="financial_agent",
    model=Groq(id='llama-3.3-70b-versatile'),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent = Agent(
    team=[websearch_agent, fianace_agent],
    instructions=["Always include soursces in your answer.", "Use table to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Sumarize analyst recommendations and share the latest new on nvidia", stream=True)


