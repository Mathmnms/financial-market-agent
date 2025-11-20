# 🎤 Présentation - Financial Market Intelligence Agent

## 📋 Structure (10 minutes)

### BUSINESS PART (2-3 minutes)

#### 1. Le Problème
> "Les investisseurs et analystes financiers font face à plusieurs défis :
> - Données dispersées sur différentes plateformes
> - Besoin de calculs manuels répétitifs
> - Difficulté à suivre l'actualité en temps réel
> - Temps perdu à chercher et synthétiser l'information"

#### 2. La Solution
> "J'ai créé un agent intelligent multi-agents qui :
> - Centralise l'analyse financière
> - Automatise les calculs complexes
> - Recherche et synthétise l'actualité
> - Répond en langage naturel"

#### 3. Démo Live (1 minute)
**Montrer l'interface Streamlit :**
1. Requête simple : "Quel est le prix de Apple ?"
2. Calcul : "Calcule mon ROI : investi 5000, valeur 7500"
3. Actualités : "Actualités sur le marché tech"

---

### TECH PART (6-7 minutes)

#### 1. Architecture (2 minutes)
**Montrer le diagramme :**
```
Utilisateur
    ↓
Supervisor Agent (Router)
    ↓
    ├─→ Market Analyst (Actions/Prix)
    ├─→ Calculator (Calculs financiers)
    └─→ Researcher (Actualités/Web)
```

**Expliquer :**
- Architecture multi-agents supervisée
- Chaque agent a sa spécialisation
- 13 tools au total (4 + 3 + 4 + 2)

#### 2. Code Walkthrough (3 minutes)

**a) Les Tools (30 sec)**
```python
@tool
def get_stock_price(symbol: str) -> str:
    """Récupère le prix d'une action."""
    stock = yf.Ticker(symbol.upper())
    # ...
```

**b) Les Agents (1 min)**
```python
class MarketAnalystAgent:
    def analyze(self, query: str):
        # 1. Appel LLM avec tools
        # 2. Exécution des tools
        # 3. Synthèse finale
```

**c) Le Superviseur (1 min)**
```python
class SupervisorAgent:
    def route(self, query: str) -> str:
        # Analyse et choix de l'agent approprié
    
    def process(self, query: str):
        # Route vers le bon agent
```

**d) Interface Streamlit (30 sec)**
- Interface interactive
- Historique des requêtes
- Statistiques en temps réel

#### 3. Exécution Live (1-2 minutes)
**Dans le terminal, montrer :**
```bash
python3 main.py
# Mode démo ou interactif
```

**Ou dans Streamlit :**
- Montrer les différents agents en action
- Afficher l'historique
- Montrer les statistiques

---

### QUESTIONS (1-2 minutes)

**Questions attendues :**

1. **"Pourquoi une architecture multi-agents ?"**
   > "Séparation des préoccupations, spécialisation, extensibilité"

2. **"Quelles difficultés avez-vous rencontrées ?"**
   > "Gestion des tool calls, gestion d'état, limites des APIs"

3. **"Comment pourriez-vous l'améliorer ?"**
   > "Ajout Human-in-the-Loop, mémoire persistante, plus de sources de données"

4. **"Coût d'utilisation ?"**
   > "Environ $0.01-0.05 par requête (GPT-4o-mini)"

---

## 🎯 Points Clés à Retenir

✅ **Architecture moderne** : Multi-agents supervisée
✅ **Production-ready** : Gestion d'erreurs, interface pro
✅ **Extensible** : Facile d'ajouter de nouveaux agents/tools
✅ **Documenté** : README, architecture, usage

## 📊 Statistiques du Projet

- **21+ commits** sur GitHub
- **13 tools** fonctionnels
- **4 agents** (1 supervisor + 3 spécialisés)
- **2 interfaces** (CLI + Streamlit)
- **Documentation complète**