"""
Agent spécialisé dans les calculs financiers.
"""
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from utils.calculator_tools import calculator_tools


class CalculatorAgent:
    """Agent spécialisé dans les calculs financiers."""
    
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.llm_with_tools = self.llm.bind_tools(calculator_tools)
        
        self.system_prompt = """Tu es un expert en calculs financiers.

Tes responsabilités :
- Calculer les retours sur investissement (ROI)
- Calculer les profits et pertes
- Calculer les variations en pourcentage
- Effectuer des analyses quantitatives

Sois précis dans tes calculs et explique tes résultats clairement."""
    
    def calculate(self, query: str) -> str:
        """Effectue un calcul financier."""
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=query)
        ]
        
        # Premier appel
        response = self.llm_with_tools.invoke(messages)
        
        # Si l'agent veut appeler des tools
        if hasattr(response, 'tool_calls') and response.tool_calls:
            from langgraph.prebuilt import ToolNode
            tool_node = ToolNode(calculator_tools)
            tool_results = tool_node.invoke({"messages": [response]})
            
            messages.append(response)
            for tool_msg in tool_results["messages"]:
                messages.append(tool_msg)
            
            final_response = self.llm.invoke(messages)
            return final_response.content
        
        return response.content if hasattr(response, 'content') else str(response)