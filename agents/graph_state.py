"""
State management pour le graphe LangGraph.
"""
from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """
    État partagé entre tous les nœuds du graphe.
    """
    messages: Annotated[list, add_messages]
    query: str
    agent_used: str
    final_answer: str