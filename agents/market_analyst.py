"""
Agent spécialisé dans l'analyse de marché.
"""
from typing import Annotated
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from utils.finance_tools import finance_tools


class MarketAnalystAgent:
    """Agent spécialisé dans l'analyse de marchés financiers."""
    
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.llm_with_tools = self.llm.bind_tools(finance_tools)
        
        self.system_prompt = """Tu es un analyste de marché financier expert.
        
Tes responsabilités :
- Analyser les prix des actions et leur évolution
- Comparer différentes actions
- Fournir des informations sur les entreprises
- Identifier les tendances du marché

Utilise les tools à ta disposition pour obtenir des données en temps réel.
Sois précis, factuel et professionnel dans tes analyses."""
    
    def analyze(self, query: str) -> str:
        """Analyse une requête liée aux marchés."""
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=query)
        ]
        
        response = self.llm_with_tools.invoke(messages)
        return response.content if hasattr(response, 'content') else str(response)