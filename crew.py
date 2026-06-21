from crewai import Crew

from agent.analyst_agent import analyst_agent
from agent.trader_agent import trader_agent
from task.analyst_task import analyst_task
from task.trader_task import trader_task
#from tool.stock_research_tool import get_stock_price

stock_crew=Crew(
    agents=[analyst_agent,trader_agent],
    tasks=[analyst_task,trader_task],
    verbose=True
)

