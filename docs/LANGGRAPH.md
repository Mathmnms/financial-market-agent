# LangGraph Implementation

## Vue d'ensemble

Ce projet utilise **LangGraph** pour implémenter une architecture multi-agents avec routing intelligent.

## Composants LangGraph

### 1. State (`AgentState`)
```python
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    query: str
    agent_used: str
    final_answer: str
```

L'état est partagé entre tous les nœuds et maintient :
- L'historique des messages
- La requête utilisateur
- L'agent sélectionné
- La réponse finale

### 2. Nœuds

#### Supervisor Node
- **Rôle** : Analyse la requête et décide quel agent utiliser
- **Input** : État avec la requête utilisateur
- **Output** : Nom de l'agent à utiliser

#### Market Analyst Node
- **Rôle** : Analyse les marchés financiers
- **Tools** : 4 tools (get_stock_price, get_stock_history, compare_stocks, get_company_info)
- **Output** : Analyse détaillée

#### Calculator Node
- **Rôle** : Effectue des calculs financiers
- **Tools** : 3 tools (calculate_roi, calculate_profit_loss, calculate_percent_change)
- **Output** : Résultat du calcul

#### Researcher Node
- **Rôle** : Recherche d'informations
- **Tools** : 4 tools (web_search, search_financial_news, get_market_sentiment, get_current_time)
- **Output** : Synthèse des recherches

### 3. Edges

#### Entry Point
```python
workflow.set_entry_point("supervisor")
```

Le graphe commence toujours par le superviseur.

#### Conditional Edges
```python
workflow.add_conditional_edges(
    "supervisor",
    self._route_after_supervisor,
    {
        "market_analyst": "market_analyst",
        "calculator": "calculator",
        "researcher": "researcher"
    }
)
```

Le routing est dynamique basé sur l'analyse du superviseur.

#### Terminal Edges
```python
workflow.add_edge("market_analyst", END)
workflow.add_edge("calculator", END)
workflow.add_edge("researcher", END)
```

Tous les agents spécialisés terminent le workflow.

## Flux d'Exécution

1. **Initialisation** : `initial_state` avec la requête utilisateur
2. **Supervisor** : Analyse et choisit l'agent
3. **Agent Spécialisé** : Exécute avec ses tools
4. **Fin** : Retourne la réponse finale

## Avantages vs Architecture Simple

| Aspect | Sans LangGraph | Avec LangGraph |
|--------|----------------|----------------|
| **Structure** | Conditionnels manuels | Graphe déclaratif |
| **State** | Variables locales | State partagé |
| **Extensibilité** | Ajouter du code | Ajouter un nœud |
| **Visualisation** | Aucune | ASCII/Mermaid |
| **Debugging** | Difficile | Traçable |

## Visualisation du Graphe

Le graphe peut être visualisé avec :
```python
agent_system.visualize()
```

Sortie :
```
                    +-----------+                            
                    | __start__ |                            
                    +-----------+                            
                          *                                  
                   +------------+                            
                   | supervisor |                            
                ...+------------+....                        
           .....          .          .....                   
    +------------+  +----------------+  +------------+ 
    | calculator |  | market_analyst |  | researcher | 
    +------------+  +----------------+  +------------+ 
           .....          .          .....                   
                   +---------+                              
                   | __end__ |                              
                   +---------+                              
```

## Code Principal

Fichier : `agents/langgraph_system.py`

Les parties clés :
1. Définition du graphe : `StateGraph(AgentState)`
2. Ajout des nœuds : `workflow.add_node()`
3. Définition des edges : `workflow.add_conditional_edges()`
4. Compilation : `workflow.compile()`

## Exemple d'Utilisation
```python
from agents.langgraph_system import LangGraphFinancialAgent

# Initialiser
agent = LangGraphFinancialAgent()

# Traiter une requête
response = agent.process("Quel est le prix de Apple ?")

# Résultat
print(response["agent_used"])  # "Market Analyst"
print(response["result"])      # Prix et analyse
```

## Performance

- **Latence** : 2-5 secondes par requête
- **Coût** : ~$0.01-0.05 par requête (GPT-4o-mini)
- **Scalabilité** : Extensible horizontalement

## Améliorations Futures

- [ ] Ajout de nœuds intermédiaires (validation, enrichissement)
- [ ] Boucles conditionnelles (retry logic)
- [ ] Persistence de l'état entre sessions
- [ ] Checkpointing pour reprise après erreur
- [ ] Human-in-the-loop avec interrupts