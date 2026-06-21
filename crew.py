from crewai import Crew

from analyst_agent import analyst_agent
from trader_agent import trader_agent
from analyst_task import analyst_task
from trader_task import trader_task
#from stock_research_tool import get_stock_price

stock_crew=Crew(
    agents=[analyst_agent,trader_agent],
    tasks=[analyst_task,trader_task],
    verbose=True
)

