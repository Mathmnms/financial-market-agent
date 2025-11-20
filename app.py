"""
Interface Streamlit améliorée pour l'agent financier.
"""
import streamlit as st
from dotenv import load_dotenv
from agents.langgraph_system import LangGraphFinancialAgent
import os
from datetime import datetime

# Charger les variables d'environnement
load_dotenv()

# Configuration de la page
st.set_page_config(
    page_title="Financial Market Intelligence",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Style CSS amélioré
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        font-weight: bold;
        color: #1e3a8a;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #64748b;
        margin-bottom: 2rem;
    }
    .agent-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        margin: 0.5rem;
        font-size: 0.9rem;
    }
    .market-analyst {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    .calculator {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
    }
    .researcher {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
    }
    .metric-card {
        background: #f8fafc;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #3b82f6;
    }
    .success-box {
        background: #f0fdf4;
        border-left: 4px solid #22c55e;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialise l'état de la session."""
    if 'supervisor' not in st.session_state:
        st.session_state.supervisor = LangGraphFinancialAgent()
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'agent_stats' not in st.session_state:
        st.session_state.agent_stats = {
            'Market Analyst': 0,
            'Calculator': 0,
            'Researcher': 0
        }


def display_sidebar():
    """Affiche la barre latérale."""
    with st.sidebar:
        st.markdown("### 🤖 À propos du système")
        st.markdown("""
        Agent multi-agents utilisant **LangGraph** pour l'analyse 
        financière intelligente.
        """)
        
        st.markdown("---")
        
        # Architecture
        st.markdown("### 🏗️ Architecture")
        st.markdown("""
        <div style='text-align: center; font-family: monospace; font-size: 0.8rem;'>
        <b>Supervisor</b><br>
        ↓<br>
        ┌──────┼──────┐<br>
        Market Calculator Researcher<br>
        Analyst
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Agents disponibles
        st.markdown("### 🎯 Agents Spécialisés")
        
        st.markdown('<div class="agent-badge market-analyst">📈 Market Analyst</div>', 
                   unsafe_allow_html=True)
        st.caption("Prix, tendances, comparaisons")
        
        st.markdown('<div class="agent-badge calculator">🧮 Calculator</div>', 
                   unsafe_allow_html=True)
        st.caption("ROI, profits, calculs")
        
        st.markdown('<div class="agent-badge researcher">🔍 Researcher</div>', 
                   unsafe_allow_html=True)
        st.caption("Actualités, sentiment")
        
        st.markdown("---")
        
        # Stats globales
        if st.session_state.history:
            st.markdown("### 📊 Statistiques")
            total = len(st.session_state.history)
            st.metric("Requêtes traitées", total)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("📈", st.session_state.agent_stats['Market Analyst'], 
                         delta=None, delta_color="off")
            with col2:
                st.metric("🧮", st.session_state.agent_stats['Calculator'], 
                         delta=None, delta_color="off")
            with col3:
                st.metric("🔍", st.session_state.agent_stats['Researcher'], 
                         delta=None, delta_color="off")


def display_header():
    """Affiche l'en-tête."""
    st.markdown('<h1 class="main-header">💼 Financial Market Intelligence</h1>', 
                unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Powered by LangGraph Multi-Agent System</p>', 
                unsafe_allow_html=True)


def get_agent_badge(agent_name):
    """Retourne le badge HTML pour un agent."""
    badges = {
        "Market Analyst": '<div class="agent-badge market-analyst">📈 Market Analyst</div>',
        "Calculator": '<div class="agent-badge calculator">🧮 Calculator</div>',
        "Researcher": '<div class="agent-badge researcher">🔍 Researcher</div>',
    }
    return badges.get(agent_name, f'<div class="agent-badge">{agent_name}</div>')


def tab_home():
    """Onglet Accueil."""
    st.markdown("### 🏠 Bienvenue")
    
    st.markdown("""
    Cet agent intelligent analyse les marchés financiers en temps réel grâce à 
    une architecture multi-agents orchestrée par **LangGraph**.
    """)
    
    # Exemples populaires
    st.markdown("### 💡 Exemples de questions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**📈 Analyse de Marché**")
        if st.button("Prix d'Apple", use_container_width=True):
            st.session_state.example_query = "Quel est le prix d'Apple (AAPL) ?"
        if st.button("Compare MSFT et GOOGL", use_container_width=True):
            st.session_state.example_query = "Compare Microsoft et Google"
    
    with col2:
        st.markdown("**🧮 Calculs Financiers**")
        if st.button("Calcul ROI", use_container_width=True):
            st.session_state.example_query = "Calcule mon ROI : investi 10000, valeur 15000"
        if st.button("Profit/Perte", use_container_width=True):
            st.session_state.example_query = "Acheté à 100$, vendu à 150$, 50 actions, profit ?"
    
    with col3:
        st.markdown("**🔍 Recherche**")
        if st.button("News Tesla", use_container_width=True):
            st.session_state.example_query = "Actualités sur Tesla"
        if st.button("Sentiment Marché", use_container_width=True):
            st.session_state.example_query = "Sentiment du marché tech"
    
    # Capacités
    st.markdown("---")
    st.markdown("### ⚡ Capacités du Système")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**13 Tools Spécialisés**\n\n4 Finance + 3 Calculs + 4 Recherche")
    with col2:
        st.success("**Routing Intelligent**\n\nLe superviseur choisit automatiquement le bon agent")
    with col3:
        st.warning("**Temps Réel**\n\nDonnées de marché et actualités actualisées")


def tab_analyze():
    """Onglet Analyse."""
    st.markdown("### 🎯 Analyser")
    
    # Vérifier les clés API
    if not os.getenv("OPENAI_API_KEY"):
        st.error("❌ OPENAI_API_KEY non trouvée. Configurez votre .env")
        return
    
    # Zone de saisie
    query = st.text_input(
        "💬 Posez votre question :",
        value=st.session_state.get('example_query', ''),
        placeholder="Ex: Quel est le prix de Apple ? ou Calcule mon ROI...",
        key="query_input"
    )
    
    col1, col2, col3 = st.columns([1, 1, 3])
    with col1:
        submit = st.button("🚀 Analyser", type="primary", use_container_width=True)
    with col2:
        if st.button("🗑️ Effacer", use_container_width=True):
            st.session_state.example_query = ""
            st.rerun()
    
    # Traiter la requête
    if submit and query:
        with st.spinner("🔄 L'agent réfléchit..."):
            try:
                # Exécuter
                response = st.session_state.supervisor.process(query)
                
                # Mettre à jour les stats
                agent_used = response['agent_used']
                if agent_used in st.session_state.agent_stats:
                    st.session_state.agent_stats[agent_used] += 1
                
                # Ajouter à l'historique
                st.session_state.history.append({
                    "query": query,
                    "agent": agent_used,
                    "response": response['result'],
                    "timestamp": datetime.now().strftime("%H:%M:%S")
                })
                
                # Afficher le résultat
                st.markdown("---")
                st.markdown(get_agent_badge(agent_used), unsafe_allow_html=True)
                
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.markdown("### 💡 Réponse")
                st.markdown(response['result'])
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Réinitialiser
                if 'example_query' in st.session_state:
                    del st.session_state.example_query
                
            except Exception as e:
                st.error(f"❌ Erreur : {str(e)}")


def tab_history():
    """Onglet Historique."""
    st.markdown("### 📜 Historique des Requêtes")
    
    if not st.session_state.history:
        st.info("Aucune requête dans l'historique. Commencez par poser une question !")
        return
    
    # Options de filtrage
    col1, col2 = st.columns([3, 1])
    with col1:
        filter_agent = st.selectbox(
            "Filtrer par agent :",
            ["Tous"] + list(st.session_state.agent_stats.keys())
        )
    with col2:
        if st.button("🗑️ Effacer l'historique", use_container_width=True):
            st.session_state.history = []
            st.session_state.agent_stats = {
                'Market Analyst': 0,
                'Calculator': 0,
                'Researcher': 0
            }
            st.rerun()
    
    # Afficher l'historique filtré
    filtered_history = st.session_state.history
    if filter_agent != "Tous":
        filtered_history = [h for h in st.session_state.history if h['agent'] == filter_agent]
    
    st.markdown(f"**{len(filtered_history)} requête(s) trouvée(s)**")
    
    for i, item in enumerate(reversed(filtered_history[-10:]), 1):
        with st.expander(f"🔹 [{item['timestamp']}] {item['query'][:60]}...", 
                        expanded=(i==1)):
            st.markdown(get_agent_badge(item['agent']), unsafe_allow_html=True)
            st.markdown(item['response'])


def tab_stats():
    """Onglet Statistiques."""
    st.markdown("### 📊 Dashboard & Statistiques")
    
    if not st.session_state.history:
        st.info("Aucune donnée disponible. Effectuez des requêtes pour voir les statistiques.")
        return
    
    # Métriques principales
    col1, col2, col3, col4 = st.columns(4)
    
    total = len(st.session_state.history)
    with col1:
        st.metric(
            label="Total Requêtes",
            value=total,
            delta=f"+{total}" if total > 0 else None
        )
    
    with col2:
        market_pct = (st.session_state.agent_stats['Market Analyst'] / total * 100) if total > 0 else 0
        st.metric(
            label="📈 Market Analyst",
            value=st.session_state.agent_stats['Market Analyst'],
            delta=f"{market_pct:.0f}%"
        )
    
    with col3:
        calc_pct = (st.session_state.agent_stats['Calculator'] / total * 100) if total > 0 else 0
        st.metric(
            label="🧮 Calculator",
            value=st.session_state.agent_stats['Calculator'],
            delta=f"{calc_pct:.0f}%"
        )
    
    with col4:
        research_pct = (st.session_state.agent_stats['Researcher'] / total * 100) if total > 0 else 0
        st.metric(
            label="🔍 Researcher",
            value=st.session_state.agent_stats['Researcher'],
            delta=f"{research_pct:.0f}%"
        )
    
    st.markdown("---")
    
    # Distribution des agents
    st.markdown("### 📊 Distribution par Agent")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Bar chart simple
        agents = list(st.session_state.agent_stats.keys())
        values = list(st.session_state.agent_stats.values())
        
        st.bar_chart(dict(zip(agents, values)))
    
    with col2:
        st.markdown("**Détails :**")
        for agent, count in st.session_state.agent_stats.items():
            percentage = (count / total * 100) if total > 0 else 0
            st.progress(percentage / 100, text=f"{agent}: {count} ({percentage:.1f}%)")
    
    st.markdown("---")
    
    # Dernières activités
    st.markdown("### ⏱️ Dernières Activités")
    
    for item in reversed(st.session_state.history[-5:]):
        col1, col2, col3 = st.columns([1, 3, 1])
        with col1:
            st.caption(item['timestamp'])
        with col2:
            st.text(item['query'][:50] + "...")
        with col3:
            st.markdown(get_agent_badge(item['agent']), unsafe_allow_html=True)


def main():
    """Fonction principale."""
    initialize_session_state()
    display_header()
    display_sidebar()
    
    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs(["🏠 Accueil", "🎯 Analyser", "📜 Historique", "📊 Stats"])
    
    with tab1:
        tab_home()
    
    with tab2:
        tab_analyze()
    
    with tab3:
        tab_history()
    
    with tab4:
        tab_stats()


if __name__ == "__main__":
    main()