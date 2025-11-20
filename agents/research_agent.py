"""
Agent spécialisé dans la recherche d'informations.
"""
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from utils.research_tools import research_tools


class ResearchAgent:
    """Agent spécialisé dans la recherche web et l'analyse d'actualités."""
    
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.llm_with_tools = self.llm.bind_tools(research_tools)
        
        self.system_prompt = """Tu es un chercheur financier expert.

Tes responsabilités :
- Rechercher des actualités financières
- Analyser le sentiment du marché
- Trouver des informations pertinentes sur les entreprises et les marchés
- Fournir des sources fiables

Cite toujours tes sources et reste objectif dans tes analyses."""
    
    def research(self, query: str) -> str:
        """Effectue une recherche."""
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=query)
        ]
        
        # Premier appel
        response = self.llm_with_tools.invoke(messages)
        
        # Si l'agent veut appeler des tools
        if hasattr(response, 'tool_calls') and response.tool_calls:
            from langgraph.prebuilt import ToolNode
            tool_node = ToolNode(research_tools)
            tool_results = tool_node.invoke({"messages": [response]})
            
            messages.append(response)
            for tool_msg in tool_results["messages"]:
                messages.append(tool_msg)
            
            final_response = self.llm.invoke(messages)
            return final_response.content
        
        return response.content if hasattr(response, 'content') else str(response)