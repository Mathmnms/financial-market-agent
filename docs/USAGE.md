# Guide d'utilisation

## Installation
```bash
# Cloner le repository
git clone https://github.com/Mathmnms/financial-market-agent.git
cd financial-market-agent

# Créer environnement virtuel
python3 -m venv venv
source venv/bin/activate

# Installer dépendances
pip3 install -r requirements.txt

# Configurer .env
cp .env.example .env
# Éditer .env avec vos clés API
```

## Configuration

### Clés API requises

1. **OpenAI API** (obligatoire)
   - Obtenir sur: https://platform.openai.com/api-keys
   - Ajouter dans `.env`: `OPENAI_API_KEY=sk-...`

2. **Tavily API** (optionnel, pour recherche web)
   - Obtenir sur: https://tavily.com
   - Ajouter dans `.env`: `TAVILY_API_KEY=tvly-...`

## Utilisation

### Mode Interactif
```bash
python3 main.py
# Choisir option 1
```

### Mode Démo
```bash
python3 main.py
# Choisir option 2
```

### Tests
```bash
python3 test_agents.py
```

## Exemples de requêtes

### Analyse de marché
- "Quel est le prix actuel de Apple (AAPL) ?"
- "Compare Microsoft et Google"
- "Donne-moi l'historique de Tesla sur 30 jours"

### Calculs financiers
- "Calcule mon ROI si j'ai investi 10000 et j'ai maintenant 15000"
- "Quel est mon profit si j'achète 50 actions à 100$ et je vends à 150$ ?"
- "Quelle est la variation entre 1000 et 1200 ?"

### Recherche
- "Quelles sont les actualités sur Tesla ?"
- "Analyse le sentiment du marché crypto"
- "Recherche des informations sur le secteur tech"

## Dépannage

### Erreur 429 (Yahoo Finance)
Limite de requêtes atteinte. Attendez quelques minutes.

### Erreur OpenAI API
Vérifiez votre clé API et votre crédit OpenAI.

### Module non trouvé
```bash
pip3 install -r requirements.txt
```