from crewai import Agent,LLM
from tool.stock_research_tool import get_stock_price

llm =LLM(
    model="google/gemini-2.5-flash",
    temperature=0.3
)
analyst_agent=Agent(
    role="Financial Market Analyst",

    goal = ("Perform in-depth evaluations of publicly traded stocks using real-time data, "
           "identifying trends, performance insights, and key financial signals to support decision-making."),

    backstory = ("You are a veteran financial analyst with deep expertise in interpreting stock market data, "
                 "technical trends, and fundamentals. You specialize in producing well-structured reports that evaluate "
                 "stock performance using live market indicators."),
    llm=llm,
    tool=[get_stock_price],
    #verbose=True,
)
