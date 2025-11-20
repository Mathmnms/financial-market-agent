# 📊 Financial Market Intelligence Agent

Agent intelligent multi-agents pour l'analyse des marchés financiers en temps réel.

## 🎯 Fonctionnalités

- 📈 Analyse d'actions en temps réel
- 📊 Historique et tendances de marché
- 💰 Calculs financiers avancés
- 🤖 Architecture multi-agents (Supervisor + Specialists)
- 🎨 Interface Streamlit interactive
- 💾 Documentation complète

## 🏗️ Architecture
```
Supervisor Agent
    ├── Market Analyst Agent (analyse marchés)
    ├── Financial Calculator Agent (calculs)
    └── Research Agent (recherche web)
```

### Composants

- **SupervisorAgent** : Coordinateur qui route les requêtes
- **MarketAnalystAgent** : Analyse de prix, tendances, comparaisons
- **CalculatorAgent** : Calculs ROI, profits/pertes, variations
- **ResearchAgent** : Actualités financières, sentiment du marché

## 🚀 Installation

### Prérequis

- Python 3.9+
- Clés API :
  - [OpenAI](https://platform.openai.com/api-keys) (obligatoire)
  - [Tavily](https://tavily.com/) (optionnel - recherche web)

### Étapes d'installation

1. **Cloner le repository**
```bash
git clone https://github.com/Mathmnms/financial-market-agent.git
cd financial-market-agent
```

2. **Créer un environnement virtuel**
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
```

3. **Installer les dépendances**
```bash
pip3 install -r requirements.txt
```

4. **Configurer les variables d'environnement**
```bash
cp .env.example .env
# Puis éditez .env et ajoutez vos vraies clés API
```

Exemple de `.env` :
```env
OPENAI_API_KEY=sk-votre-clé-ici
TAVILY_API_KEY=tvly-votre-clé-ici
```

## 💻 Utilisation

### Mode CLI Interactif
```bash
python3 main.py
# Choisir option 1
```

### Mode CLI Démo
```bash
python3 main.py
# Choisir option 2
```

### Interface Streamlit (Recommandé)
```bash
streamlit run app.py
```

L'interface s'ouvrira automatiquement sur http://localhost:8501

### Tests
```bash
python3 test_agents.py
```

## 📝 Exemples de requêtes

### Analyse de marché
- "Quel est le prix actuel de Apple (AAPL) ?"
- "Compare Microsoft et Google"
- "Donne-moi l'historique de Tesla sur 30 jours"
- "Informations sur l'entreprise NVIDIA"

### Calculs financiers
- "Calcule mon ROI si j'ai investi 10000 et j'ai maintenant 15000"
- "Quel est mon profit si j'achète 50 actions à 100$ et je vends à 150$ ?"
- "Quelle est la variation en pourcentage entre 1000 et 1200 ?"

### Recherche et actualités
- "Quelles sont les actualités sur Tesla ?"
- "Analyse le sentiment du marché crypto"
- "Recherche des informations sur le secteur technologique"

## 📁 Structure du Projet
```
financial-market-agent/
├── main.py                    # Point d'entrée CLI
├── app.py                     # Interface Streamlit
├── test_agents.py             # Tests des agents
├── requirements.txt           # Dépendances Python
├── .env.example              # Template configuration
├── .gitignore
├── README.md
├── presentation.md           # Slides de présentation
│
├── agents/                   # Agents spécialisés
│   ├── __init__.py
│   ├── supervisor.py        # Agent superviseur
│   ├── market_analyst.py    # Analyse de marché
│   ├── calculator_agent.py  # Calculs financiers
│   └── research_agent.py    # Recherche web
│
├── utils/                    # Outils et fonctions
│   ├── __init__.py
│   ├── finance_tools.py     # Tools finance (yfinance)
│   ├── calculator_tools.py  # Tools calculs
│   └── research_tools.py    # Tools recherche (Tavily)
│
└── docs/                     # Documentation
    ├── ARCHITECTURE.md       # Architecture détaillée
    ├── USAGE.md             # Guide d'utilisation
    └── PRESENTATION.md      # Guide de présentation
```

## 🛠️ Technologies

- **LangChain** : Framework pour applications LLM
- **OpenAI GPT-4o-mini** : Modèle de langage
- **Streamlit** : Interface web interactive
- **yfinance** : Données financières Yahoo Finance
- **Tavily** : API de recherche web
- **Python 3.12** : Langage de programmation

## 📊 Outils disponibles

### Finance Tools (4)
- get_stock_price() - Prix actuel d'une action
- get_stock_history() - Historique et statistiques
- compare_stocks() - Comparaison d'actions
- get_company_info() - Informations entreprise

### Calculator Tools (3)
- calculate_roi() - Retour sur investissement
- calculate_profit_loss() - Profits et pertes
- calculate_percent_change() - Variation en %

### Research Tools (4)
- web_search() - Recherche web générale
- search_financial_news() - Actualités financières
- get_market_sentiment() - Sentiment du marché
- get_current_time() - Date et heure

## 🔐 Sécurité

- Les clés API sont stockées dans .env (non versionné)
- Le .gitignore empêche la publication des secrets
- Validation des inputs utilisateur
- Gestion des erreurs robuste

## 🐛 Dépannage

### Erreur 429 (Yahoo Finance)
Limite de requêtes atteinte. Attendez quelques minutes avant de réessayer.

### Erreur OpenAI API
- Vérifiez votre clé API dans .env
- Vérifiez votre crédit OpenAI sur https://platform.openai.com/usage

### Module non trouvé
```bash
source venv/bin/activate
pip3 install -r requirements.txt
```

### Interface Streamlit ne s'ouvre pas
```bash
pip3 install streamlit
streamlit run app.py
```

## 📈 Statistiques

- 4 agents (1 supervisor + 3 spécialisés)
- 13 tools fonctionnels
- 2 interfaces (CLI + Streamlit)
- Documentation complète

## 🚀 Améliorations futures

- Human-in-the-Loop pour validation
- Mémoire persistante avec base de données
- Plus de sources de données (Bloomberg, Reuters)
- Alertes et notifications automatiques
- Prédictions avec Machine Learning
- Support multi-utilisateurs

## 📚 Documentation

- [Architecture détaillée](docs/ARCHITECTURE.md)
- [Guide d'utilisation](docs/USAGE.md)

## 👨‍💻 Auteur

Mathis Meimoun - Projet final MSc Albert - Agentic Systems

## 📄 Licence

Ce projet est créé à des fins éducatives dans le cadre du MSc Albert.

## 🙏 Remerciements

- LangChain pour le framework
- OpenAI pour l'API GPT
- Yahoo Finance pour les données financières
- Tavily pour l'API de recherche
