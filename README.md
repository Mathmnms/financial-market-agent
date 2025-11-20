# 📊 Financial Market Intelligence Agent

Agent intelligent multi-agents pour l'analyse des marchés financiers en temps réel.

## 🎯 Fonctionnalités

- 📈 Analyse d'actions en temps réel
- 📊 Historique et tendances de marché
- 💰 Calculs financiers avancés
- 🤖 Architecture multi-agents (Supervisor + Specialists)
- ⏸️ Human-in-the-Loop pour validation
- 🎨 Interface Streamlit interactive
- 💾 Mémoire persistante

## 🏗️ Architecture
```
Supervisor Agent
    ├── Market Analyst Agent (analyse marchés)
    ├── Financial Calculator Agent (calculs)
    └── Research Agent (recherche web)
```

## 🚀 Installation

1. Cloner le repository
2. Créer environnement virtuel : `python3 -m venv venv`
3. Activer : `source venv/bin/activate`
4. Installer : `pip3 install -r requirements.txt`
5. Configurer `.env` avec vos clés API

## 💻 Utilisation
```bash
# Mode CLI
python3 main.py

# Interface Streamlit
streamlit run app.py
```

## 👨‍💻 Auteur

Projet final - MSc Albert - Agentic Systems