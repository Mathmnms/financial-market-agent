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
        
        # Premier appel : l'agent décide quels tools utiliser
        response = self.llm_with_tools.invoke(messages)
        
        # Si l'agent veut appeler des tools
        if hasattr(response, 'tool_calls') and response.tool_calls:
            # Exécuter les tools
            from langgraph.prebuilt import ToolNode
            tool_node = ToolNode(finance_tools)
            tool_results = tool_node.invoke({"messages": [response]})
            
            # Ajouter les résultats et demander la réponse finale
            messages.append(response)
            for tool_msg in tool_results["messages"]:
                messages.append(tool_msg)
            
            # Deuxième appel : générer la réponse finale
            final_response = self.llm.invoke(messages)
            return final_response.content
        
        # Si pas de tool call, retourner la réponse directe
        return response.content if hasattr(response, 'content') else str(response)