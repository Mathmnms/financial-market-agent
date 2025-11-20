# Architecture du Système

## Vue d'ensemble

Le Financial Market Intelligence Agent utilise une **architecture multi-agents supervisée**.

## Diagramme
```
                    ┌─────────────────┐
                    │   Utilisateur   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Supervisor    │
                    │     Agent       │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
      ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
      │   Market     │ │  Calculator  │ │  Research    │
      │   Analyst    │ │    Agent     │ │    Agent     │
      └──────┬───────┘ └──────┬───────┘ └──────┬───────┘
             │                │                │
             ▼                ▼                ▼
      ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
      │   Finance    │ │  Calculator  │ │  Research    │
      │    Tools     │ │    Tools     │ │    Tools     │
      └──────────────┘ └──────────────┘ └──────────────┘
```

## Agents

### 1. SupervisorAgent
**Rôle**: Coordinateur principal
- Analyse les requêtes utilisateur
- Route vers l'agent approprié
- Agrège les résultats

### 2. MarketAnalystAgent
**Spécialisation**: Analyse de marché
- Prix des actions en temps réel
- Comparaisons d'actions
- Informations sur les entreprises
- Historique et tendances

**Tools**:
- `get_stock_price()`
- `get_stock_history()`
- `compare_stocks()`
- `get_company_info()`

### 3. CalculatorAgent
**Spécialisation**: Calculs financiers
- Retour sur investissement (ROI)
- Profits et pertes
- Variations en pourcentage

**Tools**:
- `calculate_roi()`
- `calculate_profit_loss()`
- `calculate_percent_change()`

### 4. ResearchAgent
**Spécialisation**: Recherche et actualités
- Actualités financières
- Sentiment du marché
- Recherche web générale

**Tools**:
- `web_search()`
- `search_financial_news()`
- `get_market_sentiment()`

## Flux d'exécution

1. **Réception**: L'utilisateur pose une question
2. **Routing**: Le Supervisor analyse et choisit l'agent
3. **Traitement**: L'agent spécialisé traite la requête
4. **Tools**: L'agent utilise ses tools si nécessaire
5. **Réponse**: Le résultat est retourné à l'utilisateur

## Technologies

- **LLM**: OpenAI GPT-4o-mini
- **Framework**: LangChain
- **APIs**: Yahoo Finance (yfinance), Tavily (recherche)
- **Langage**: Python 3.12