"""
Module utilitaire pour l'agent financier.
"""
from utils.finance_tools import finance_tools
from utils.calculator_tools import calculator_tools
from utils.research_tools import research_tools

# Tous les tools disponibles
all_tools = finance_tools + calculator_tools + research_tools

__all__ = [
    'finance_tools',
    'calculator_tools', 
    'research_tools',
    'all_tools'
]