"""
Module des agents spécialisés.
"""
from agents.supervisor import SupervisorAgent
from agents.market_analyst import MarketAnalystAgent
from agents.calculator_agent import CalculatorAgent
from agents.research_agent import ResearchAgent

__all__ = [
    'SupervisorAgent',
    'MarketAnalystAgent',
    'CalculatorAgent',
    'ResearchAgent'
]