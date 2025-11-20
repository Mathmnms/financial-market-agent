"""
Interface Streamlit pour l'agent financier.
"""
import streamlit as st
from dotenv import load_dotenv
from agents.langgraph_system import LangGraphFinancialAgent
import os

# Charger les variables d'environnement
load_dotenv()

# Configuration de la page
st.set_page_config(
    page_title="Financial Market Intelligence",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .agent-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        margin: 0.5rem;
    }
    .market-analyst {
        background-color: #e3f2fd;
        color: #1976d2;
    }
    .calculator {
        background-color: #f3e5f5;
        color: #7b1fa2;
    }
    .researcher {
        background-color: #e8f5e9;
        color: #388e3c;
    }
    .stAlert {
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialise l'état de la session."""
    if 'supervisor' not in st.session_state:
        st.session_state.supervisor = LangGraphFinancialAgent()
    if 'history' not in st.session_state:
        st.session_state.history = []


def display_header():
    """Affiche l'en-tête de l'application."""
    st.markdown('<h1 class="main-header">💼 Financial Market Intelligence Agent</h1>', 
                unsafe_allow_html=True)
    st.markdown("### 🤖 Architecture Multi-Agents pour l'Analyse Financière")
    st.markdown("---")


def display_sidebar():
    """Affiche la barre latérale."""
    with st.sidebar:
        st.header("📊 À propos")
        st.markdown("""
        Cet agent intelligent utilise une **architecture multi-agents** 
        pour analyser les marchés financiers.
        
        ### 🤖 Agents disponibles:
        
        <div class="agent-badge market-analyst">📈 Market Analyst</div>
        
        - Analyse de prix et tendances
        - Comparaison d'actions
        - Informations sur les entreprises
        
        <div class="agent-badge calculator">🧮 Calculator</div>
        
        - Calculs de ROI
        - Profits et pertes
        - Variations en %
        
        <div class="agent-badge researcher">🔍 Researcher</div>
        
        - Actualités financières
        - Sentiment du marché
        - Recherche web
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Exemples de questions
        st.header("💡 Exemples de questions")
        examples = [
            "Quel est le prix de Apple (AAPL) ?",
            "Calcule mon ROI: investi 10000, valeur 15000",
            "Actualités sur Tesla",
            "Compare Microsoft et Google",
            "Mon profit: acheté à 100$, vendu à 150$, 50 actions"
        ]
        
        for example in examples:
            if st.button(example, key=example):
                st.session_state.current_query = example
        
        st.markdown("---")
        
        # Statistiques
        if st.session_state.history:
            st.header("📊 Statistiques")
            st.metric("Requêtes traitées", len(st.session_state.history))
            
            # Compter les agents utilisés
            agent_counts = {}
            for item in st.session_state.history:
                agent = item['agent_used']
                agent_counts[agent] = agent_counts.get(agent, 0) + 1
            
            st.write("**Agents utilisés:**")
            for agent, count in agent_counts.items():
                st.write(f"- {agent}: {count}")


def display_main_interface():
    """Affiche l'interface principale."""
    
    # Vérifier les clés API
    if not os.getenv("OPENAI_API_KEY"):
        st.error("❌ OPENAI_API_KEY non trouvée. Veuillez configurer votre fichier .env")
        return
    
    # Zone de saisie
    col1, col2 = st.columns([5, 1])
    
    with col1:
        query = st.text_input(
            "💬 Posez votre question financière:",
            value=st.session_state.get('current_query', ''),
            placeholder="Ex: Quel est le prix de Apple ? ou Calcule mon ROI...",
            key="query_input"
        )
    
    with col2:
        st.write("")  # Espaceur
        st.write("")  # Espaceur
        submit = st.button("🚀 Analyser", type="primary", use_container_width=True)
    
    # Traiter la requête
    if submit and query:
        with st.spinner("🔄 Analyse en cours..."):
            try:
                response = st.session_state.supervisor.process(query)
                
                # Ajouter à l'historique
                st.session_state.history.append(response)
                
                # Afficher le résultat
                st.markdown("---")
                
                # Badge de l'agent utilisé
                agent = response['agent_used']
                if "Market" in agent:
                    badge_class = "market-analyst"
                    emoji = "📈"
                elif "Calculator" in agent:
                    badge_class = "calculator"
                    emoji = "🧮"
                else:
                    badge_class = "researcher"
                    emoji = "🔍"
                
                st.markdown(f'<div class="agent-badge {badge_class}">{emoji} {agent}</div>', 
                           unsafe_allow_html=True)
                
                # Résultat
                st.markdown("### 💡 Réponse:")
                st.markdown(response['result'])
                
                # Réinitialiser la requête
                if 'current_query' in st.session_state:
                    del st.session_state.current_query
                
            except Exception as e:
                st.error(f"❌ Erreur: {str(e)}")
    
    # Afficher l'historique
    if st.session_state.history:
        st.markdown("---")
        st.header("📜 Historique des requêtes")
        
        # Afficher les 5 dernières requêtes (inversé)
        for i, item in enumerate(reversed(st.session_state.history[-5:])):
            with st.expander(f"🔹 {item['query']}", expanded=(i==0)):
                st.markdown(f"**Agent:** {item['agent_used']}")
                st.markdown(item['result'])
        
        # Bouton pour effacer l'historique
        if st.button("🗑️ Effacer l'historique"):
            st.session_state.history = []
            st.rerun()


def main():
    """Fonction principale."""
    initialize_session_state()
    display_header()
    display_sidebar()
    display_main_interface()


if __name__ == "__main__":
    main()