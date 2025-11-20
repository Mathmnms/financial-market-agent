"""
Système multi-agents utilisant LangGraph.
"""
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

from agents.graph_state import AgentState
from utils.finance_tools import finance_tools
from utils.calculator_tools import calculator_tools
from utils.research_tools import research_tools

load_dotenv()


class LangGraphFinancialAgent:
    """Système d'agents financiers utilisant LangGraph."""
    
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        
        # Tous les tools disponibles
        self.all_tools = finance_tools + calculator_tools + research_tools
        
        # Créer le graphe
        self.graph = self._create_graph()
    
    def _create_supervisor_node(self):
        """Crée le nœud superviseur qui décide quel agent utiliser."""
        
        supervisor_prompt = """Tu es un superviseur d'agents financiers.

Analyse la requête de l'utilisateur et détermine quel type d'agent doit la traiter :

1. **market_analyst** : Pour les questions sur les prix d'actions, comparaisons, historiques, informations sur les entreprises
   Exemples : "Prix de AAPL ?", "Compare TSLA et NVDA", "Historique de Microsoft"

2. **calculator** : Pour les calculs financiers (ROI, profits/pertes, pourcentages)
   Exemples : "Calcule mon ROI", "Mon profit si...", "Variation entre X et Y"

3. **researcher** : Pour les actualités, sentiment du marché, recherches générales
   Exemples : "Actualités sur Tesla", "Sentiment du marché", "Recherche sur..."

Réponds UNIQUEMENT avec un de ces mots : market_analyst, calculator, ou researcher"""
        
        def supervisor_node(state: AgentState):
            """Nœud qui décide quel agent utiliser."""
            query = state["query"]
            
            messages = [
                SystemMessage(content=supervisor_prompt),
                HumanMessage(content=f"Requête: {query}")
            ]
            
            response = self.llm.invoke(messages)
            agent_choice = response.content.strip().lower()
            
            # Déterminer le prochain nœud
            if "market" in agent_choice:
                next_agent = "market_analyst"
            elif "calculator" in agent_choice:
                next_agent = "calculator"
            elif "research" in agent_choice:
                next_agent = "researcher"
            else:
                next_agent = "calculator"  # Par défaut
            
            return {
                "agent_used": next_agent,
                "messages": state["messages"]
            }
        
        return supervisor_node
    
    def _create_market_analyst_node(self):
        """Crée le nœud Market Analyst."""
        
        system_prompt = """Tu es un analyste de marché financier expert.

Utilise les tools à ta disposition pour obtenir des données en temps réel sur les actions.
Sois précis, factuel et professionnel dans tes analyses."""
        
        llm_with_tools = self.llm.bind_tools(finance_tools)
        
        def market_analyst_node(state: AgentState):
            """Nœud qui analyse les marchés."""
            query = state["query"]
            
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=query)
            ]
            
            # Premier appel : décider quels tools utiliser
            response = llm_with_tools.invoke(messages)
            
            # Si tool calls, les exécuter
            if hasattr(response, 'tool_calls') and response.tool_calls:
                tool_node = ToolNode(finance_tools)
                tool_results = tool_node.invoke({"messages": [response]})
                
                # Ajouter les résultats
                messages.append(response)
                for tool_msg in tool_results["messages"]:
                    messages.append(tool_msg)
                
                # Génération finale
                final_response = self.llm.invoke(messages)
                answer = final_response.content
            else:
                answer = response.content
            
            return {
                "final_answer": answer,
                "messages": state["messages"] + [HumanMessage(content=query), response]
            }
        
        return market_analyst_node
    
    def _create_calculator_node(self):
        """Crée le nœud Calculator."""
        
        system_prompt = """Tu es un expert en calculs financiers.

Utilise les tools à ta disposition pour effectuer des calculs précis.
Explique tes résultats clairement."""
        
        llm_with_tools = self.llm.bind_tools(calculator_tools)
        
        def calculator_node(state: AgentState):
            """Nœud qui effectue les calculs."""
            query = state["query"]
            
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=query)
            ]
            
            response = llm_with_tools.invoke(messages)
            
            if hasattr(response, 'tool_calls') and response.tool_calls:
                tool_node = ToolNode(calculator_tools)
                tool_results = tool_node.invoke({"messages": [response]})
                
                messages.append(response)
                for tool_msg in tool_results["messages"]:
                    messages.append(tool_msg)
                
                final_response = self.llm.invoke(messages)
                answer = final_response.content
            else:
                answer = response.content
            
            return {
                "final_answer": answer,
                "messages": state["messages"] + [HumanMessage(content=query), response]
            }
        
        return calculator_node
    
    def _create_researcher_node(self):
        """Crée le nœud Researcher."""
        
        system_prompt = """Tu es un chercheur financier expert.

Utilise les tools à ta disposition pour rechercher des informations pertinentes.
Cite tes sources et reste objectif."""
        
        llm_with_tools = self.llm.bind_tools(research_tools)
        
        def researcher_node(state: AgentState):
            """Nœud qui effectue les recherches."""
            query = state["query"]
            
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=query)
            ]
            
            response = llm_with_tools.invoke(messages)
            
            if hasattr(response, 'tool_calls') and response.tool_calls:
                tool_node = ToolNode(research_tools)
                tool_results = tool_node.invoke({"messages": [response]})
                
                messages.append(response)
                for tool_msg in tool_results["messages"]:
                    messages.append(tool_msg)
                
                final_response = self.llm.invoke(messages)
                answer = final_response.content
            else:
                answer = response.content
            
            return {
                "final_answer": answer,
                "messages": state["messages"] + [HumanMessage(content=query), response]
            }
        
        return researcher_node
    
    def _route_after_supervisor(self, state: AgentState) -> str:
        """Détermine le prochain nœud après le superviseur."""
        return state["agent_used"]
    
    def _create_graph(self):
        """Crée et compile le graphe LangGraph."""
        
        # Créer le graphe
        workflow = StateGraph(AgentState)
        
        # Ajouter les nœuds
        workflow.add_node("supervisor", self._create_supervisor_node())
        workflow.add_node("market_analyst", self._create_market_analyst_node())
        workflow.add_node("calculator", self._create_calculator_node())
        workflow.add_node("researcher", self._create_researcher_node())
        
        # Définir le point d'entrée
        workflow.set_entry_point("supervisor")
        
        # Ajouter les edges conditionnelles depuis le superviseur
        workflow.add_conditional_edges(
            "supervisor",
            self._route_after_supervisor,
            {
                "market_analyst": "market_analyst",
                "calculator": "calculator",
                "researcher": "researcher"
            }
        )
        
        # Tous les agents spécialisés mènent à END
        workflow.add_edge("market_analyst", END)
        workflow.add_edge("calculator", END)
        workflow.add_edge("researcher", END)
        
        # Compiler le graphe
        return workflow.compile()
    
    def process(self, query: str) -> dict:
        """
        Traite une requête utilisateur.
        
        Args:
            query: Question de l'utilisateur
        
        Returns:
            dict avec query, agent_used, et result
        """
        # Préparer l'état initial
        initial_state = {
            "messages": [],
            "query": query,
            "agent_used": "",
            "final_answer": ""
        }
        
        # Exécuter le graphe
        result = self.graph.invoke(initial_state)
        
        # Formater le nom de l'agent
        agent_name_map = {
            "market_analyst": "Market Analyst",
            "calculator": "Calculator",
            "researcher": "Researcher"
        }
        
        agent_display = agent_name_map.get(result["agent_used"], result["agent_used"])
        
        return {
            "query": query,
            "agent_used": agent_display,
            "result": result["final_answer"]
        }
    
    def visualize(self):
        """Affiche la structure du graphe."""
        try:
            print("\n" + "="*60)
            print("STRUCTURE DU GRAPHE LANGGRAPH")
            print("="*60)
            print(self.graph.get_graph().draw_ascii())
            print("="*60 + "\n")
        except Exception as e:
            print(f"Impossible d'afficher le graphe: {e}")