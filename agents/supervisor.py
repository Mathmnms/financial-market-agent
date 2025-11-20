"""
Agent superviseur qui coordonne les autres agents.
"""
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from agents.market_analyst import MarketAnalystAgent
from agents.calculator_agent import CalculatorAgent
from agents.research_agent import ResearchAgent


class SupervisorAgent:
    """Agent superviseur qui route les requêtes vers les agents spécialisés."""
    
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        
        # Initialiser les agents spécialisés
        self.market_analyst = MarketAnalystAgent()
        self.calculator = CalculatorAgent()
        self.researcher = ResearchAgent()
        
        self.system_prompt = """Tu es un superviseur d'agents financiers.

Ton rôle est d'analyser les requêtes des utilisateurs et de déterminer quel agent doit traiter la demande :

1. **MarketAnalyst** : Pour les questions sur les prix d'actions, comparaisons, informations sur les entreprises
   Exemples : "Quel est le prix de AAPL ?", "Compare TSLA et NVDA"

2. **Calculator** : Pour les calculs financiers (ROI, profits/pertes, pourcentages)
   Exemples : "Calcule mon ROI", "Quel est mon profit si...", "Variation entre X et Y"

3. **Researcher** : Pour les actualités, sentiment du marché, recherches générales
   Exemples : "Actualités sur Tesla", "Sentiment du marché crypto", "Recherche sur..."

Réponds UNIQUEMENT avec le nom de l'agent approprié : MarketAnalyst, Calculator, ou Researcher.
Si la requête nécessite plusieurs agents, commence par le plus pertinent."""
    
    def route(self, query: str) -> str:
        """Détermine quel agent doit traiter la requête."""
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=f"Quelle agent doit traiter cette requête ?\n\nRequête: {query}")
        ]
        
        response = self.llm.invoke(messages)
        agent_name = response.content.strip()
        
        return agent_name
    
    def process(self, query: str) -> dict:
        """Traite une requête en la routant vers le bon agent."""
        # Déterminer l'agent approprié
        agent_name = self.route(query)
        
        # Router vers l'agent
        if "MarketAnalyst" in agent_name:
            result = self.market_analyst.analyze(query)
            agent_used = "Market Analyst"
        elif "Calculator" in agent_name:
            result = self.calculator.calculate(query)
            agent_used = "Calculator"
        elif "Researcher" in agent_name:
            result = self.researcher.research(query)
            agent_used = "Researcher"
        else:
            result = "Je ne suis pas sûr de quel agent utiliser pour cette requête."
            agent_used = "Supervisor"
        
        return {
            "query": query,
            "agent_used": agent_used,
            "result": result
        }