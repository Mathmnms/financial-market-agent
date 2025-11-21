"""
Financial Market Intelligence - ULTIMATE EDITION
Interface Streamlit Ultra Premium avec toutes les fonctionnalités avancées
"""
import streamlit as st
from dotenv import load_dotenv
from agents.langgraph_system import LangGraphFinancialAgent
import os
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
from utils.export_utils import export_to_pdf, export_to_csv
import time
import json
import yfinance as yf

# Charger les variables d'environnement
load_dotenv()

# Configuration de la page
st.set_page_config(
    page_title="Financial Intelligence Ultimate",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Ultra Premium avec Dark Mode
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    /* Variables */
    :root {
        --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        --success-gradient: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        --dark-bg: #0f172a;
        --card-bg: #1e293b;
        --text-primary: #f1f5f9;
        --text-secondary: #94a3b8;
    }
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main container */
    .main {
        background: var(--dark-bg);
        color: var(--text-primary);
    }
    
    .block-container {
        padding-top: 2rem;
        max-width: 1400px;
    }
    
    /* Animated Header */
    .ultimate-header {
        text-align: center;
        padding: 2rem 0;
        background: var(--primary-gradient);
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
        animation: slideDown 0.6s ease-out;
    }
    
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .ultimate-header h1 {
        font-size: 3.5rem;
        font-weight: 800;
        color: white;
        margin: 0;
        text-shadow: 0 4px 20px rgba(0,0,0,0.3);
        letter-spacing: -1px;
    }
    
    .ultimate-header .subtitle {
        font-size: 1.3rem;
        color: rgba(255,255,255,0.9);
        margin-top: 0.5rem;
        font-weight: 500;
    }
    
    /* Glass Card Effect */
    .glass-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 48px rgba(0,0,0,0.4);
        border-color: rgba(255,255,255,0.2);
    }
    
    /* Premium Buttons */
    .stButton > button {
        background: var(--primary-gradient) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
    }
    
    /* Agent Badges Premium */
    .agent-badge-ultimate {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.75rem 1.5rem;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1rem;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .agent-badge-ultimate::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: rgba(255,255,255,0.2);
        transition: left 0.5s;
    }
    
    .agent-badge-ultimate:hover::before {
        left: 100%;
    }
    
    .agent-badge-ultimate:hover {
        transform: scale(1.05) translateY(-2px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.4);
    }
    
    .badge-market {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .badge-calc {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        color: white;
    }
    
    .badge-research {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
    }
    
    /* Metric Cards */
    .metric-ultimate {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .metric-ultimate::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: var(--primary-gradient);
    }
    
    .metric-ultimate:hover {
        transform: translateY(-5px);
        border-color: rgba(102, 126, 234, 0.5);
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 800;
        background: var(--primary-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        color: var(--text-secondary);
        font-size: 0.9rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Tabs Ultra Premium */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: var(--card-bg);
        padding: 0.5rem;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        padding: 0 2rem;
        background: transparent;
        border-radius: 12px;
        color: var(--text-secondary);
        font-weight: 600;
        font-size: 1.05rem;
        transition: all 0.3s ease;
        border: 2px solid transparent;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255,255,255,0.05);
        color: var(--text-primary);
    }
    
    .stTabs [aria-selected="true"] {
        background: var(--primary-gradient) !important;
        color: white !important;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.4);
        border-color: rgba(255,255,255,0.3);
    }
    
    /* Input Fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: var(--card-bg) !important;
        border: 2px solid rgba(255,255,255,0.1) !important;
        border-radius: 12px !important;
        color: var(--text-primary) !important;
        font-size: 1rem !important;
        padding: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: rgba(102, 126, 234, 0.8) !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2) !important;
    }
    
    /* Sidebar Premium */
    [data-testid="stSidebar"] {
        background: var(--card-bg);
        border-right: 1px solid rgba(255,255,255,0.1);
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: var(--text-primary);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: var(--card-bg);
        border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.1);
        color: var(--text-primary);
        font-weight: 600;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: rgba(102, 126, 234, 0.5);
    }
    
    /* Success/Info/Warning Boxes */
    .stSuccess, .stInfo, .stWarning {
        background: var(--card-bg) !important;
        border-left: 4px solid !important;
        border-radius: 12px !important;
        padding: 1rem !important;
    }
    
    /* Loading Animation */
    .loading-pulse {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: var(--primary-gradient);
        animation: pulse 1.5s ease-in-out infinite;
        margin: 0 4px;
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
            transform: scale(1);
        }
        50% {
            opacity: 0.3;
            transform: scale(0.8);
        }
    }
    
    /* Chart Container */
    .chart-container {
        background: var(--card-bg);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid rgba(255,255,255,0.1);
        margin: 1rem 0;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: var(--dark-bg);
    }
    
    ::-webkit-scrollbar-thumb {
        background: var(--primary-gradient);
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Footer */
    .ultimate-footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        border-top: 1px solid rgba(255,255,255,0.1);
        color: var(--text-secondary);
    }
    
    /* Floating Action Button */
    .fab {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: var(--primary-gradient);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.3s ease;
        z-index: 1000;
    }
    
    .fab:hover {
        transform: scale(1.1) rotate(90deg);
        box-shadow: 0 12px 35px rgba(102, 126, 234, 0.7);
    }
</style>
""", unsafe_allow_html=True)

def initialize_session_state():
    """Initialise l'état de la session avec persistence."""
    if 'supervisor' not in st.session_state:
        st.session_state.supervisor = LangGraphFinancialAgent()
    if 'history' not in st.session_state:
        st.session_state.history = load_history()
    if 'agent_stats' not in st.session_state:
        st.session_state.agent_stats = load_agent_stats()  # ✅ Chargement depuis fichier ou historique
    if 'favorites' not in st.session_state:
        st.session_state.favorites = load_favorites()  # ✅ Changement ici
    if 'theme' not in st.session_state:
        st.session_state.theme = 'dark'
    if 'watchlist' not in st.session_state:
        st.session_state.watchlist = ['AAPL', 'MSFT', 'GOOGL', 'TSLA']


def save_history():
    """Sauvegarde l'historique dans un fichier JSON."""
    try:
        with open('.streamlit_history.json', 'w') as f:
            json.dump(st.session_state.history, f)
    except:
        pass


def load_history():
    """Charge l'historique depuis le fichier JSON."""
    try:
        with open('.streamlit_history.json', 'r') as f:
            return json.load(f)
    except:
        return []

def save_favorites():
    """Sauvegarde les favoris dans un fichier JSON."""
    try:
        with open('.streamlit_favorites.json', 'w') as f:
            json.dump(st.session_state.favorites, f)
    except:
        pass


def load_favorites():
    """Charge les favoris depuis le fichier JSON."""
    try:
        with open('.streamlit_favorites.json', 'r') as f:
            return json.load(f)
    except:
        return []

def save_agent_stats():
    """Sauvegarde les stats des agents dans un fichier JSON."""
    try:
        with open('.streamlit_agent_stats.json', 'w') as f:
            json.dump(st.session_state.agent_stats, f)
    except:
        pass


def load_agent_stats():
    """Charge les stats des agents depuis le fichier JSON."""
    try:
        with open('.streamlit_agent_stats.json', 'r') as f:
            return json.load(f)
    except:
        # Si le fichier n'existe pas, calculer depuis l'historique
        stats = {
            'Market Analyst': 0,
            'Calculator': 0,
            'Researcher': 0
        }
        
        # Charger l'historique
        history = load_history()
        
        # Compter depuis l'historique
        for item in history:
            agent = item.get('agent', '')
            if agent in stats:
                stats[agent] += 1
        
        return stats

def get_stock_mini_chart(symbol):
    """Récupère un mini graphique pour une action."""
    try:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="7d")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=hist.index,
            y=hist['Close'],
            mode='lines',
            line=dict(color='#667eea', width=2),
            fill='tozeroy',
            fillcolor='rgba(102, 126, 234, 0.2)'
        ))
        
        fig.update_layout(
            height=100,
            margin=dict(l=0, r=0, t=0, b=0),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            xaxis=dict(visible=False),
            yaxis=dict(visible=False)
        )
        
        return fig
    except:
        return None


def display_ultimate_header():
    """Affiche l'en-tête ultra premium."""
    st.markdown("""
    <div class="ultimate-header">
        <h1>💎 Financial Intelligence Ultimate</h1>
        <div class="subtitle">
            🚀 Multi-Agent System • Powered by LangGraph • Real-time Market Analysis
        </div>
    </div>
    """, unsafe_allow_html=True)


def display_premium_sidebar():
    """Sidebar ultra premium avec watchlist et stats live."""
    with st.sidebar:
        st.markdown("### 💎 Ultimate Edition")
        st.caption("v2.0 - Toutes les fonctionnalités")
        
        st.markdown("---")
        
        # Live Watchlist
        st.markdown("### 📊 Watchlist Live")
        
        for symbol in st.session_state.watchlist:
            try:
                stock = yf.Ticker(symbol)
                info = stock.info
                price = info.get('currentPrice', info.get('regularMarketPrice', 0))
                prev_close = info.get('previousClose', price)
                change = ((price - prev_close) / prev_close * 100) if prev_close else 0
                
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.markdown(f"**{symbol}**")
                    st.caption(f"${price:.2f}")
                with col2:
                    color = "🟢" if change > 0 else "🔴"
                    st.markdown(f"{color} {change:+.1f}%")
                
                # Mini chart
                mini_chart = get_stock_mini_chart(symbol)
                if mini_chart:
                    st.plotly_chart(mini_chart, use_container_width=True, config={'displayModeBar': False})
                
                st.markdown("---")
            except:
                pass
        
        # Quick Actions
        st.markdown("### ⚡ Actions Rapides")
        
        if st.button("🔄 Rafraîchir Watchlist", use_container_width=True):
            st.rerun()
        
        fav_count = len(st.session_state.favorites)
        if st.button(f"⭐ Favoris ({fav_count})", use_container_width=True):
            st.session_state.active_tab = 1  # Aller à l'onglet Favoris
            st.rerun()
        
        if st.button("📥 Export Complet", use_container_width=True):
            st.session_state.show_export = True
        
        st.markdown("---")
        
        # System Stats
        st.markdown("---")
        st.markdown("### 📈 Stats Système")

        if st.session_state.history:
            total = len(st.session_state.history)
            
            # Metric avec style
            st.markdown(f"""
            <div style="text-align: center; padding: 1rem; background: rgba(102, 126, 234, 0.1); border-radius: 10px; margin-bottom: 1rem;">
                <div style="color: #94a3b8; font-size: 0.8rem; text-transform: uppercase;">Requêtes</div>
                <div style="font-size: 2.5rem; font-weight: 800; color: #667eea;">{total}</div>
                <div style="color: #22c55e; font-size: 0.9rem;">↑ +{total}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Distribution des agents
            st.markdown("**Par Agent:**")
            
            for agent, count in st.session_state.agent_stats.items():
                percentage = (count / total * 100) if total > 0 else 0
                
                # Couleur selon l'agent
                colors = {
                    'Market Analyst': '#667eea',
                    'Calculator': '#f5576c',
                    'Researcher': '#00f2fe'
                }
                color = colors.get(agent, '#667eea')
                
                st.markdown(f"""
                <div style="margin-bottom: 0.75rem;">
                    <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                        <span style="color: #f1f5f9; font-size: 0.85rem;">{agent[:10]}...</span>
                        <span style="color: {color}; font-weight: 600;">{count}</span>
                    </div>
                    <div style="background: rgba(255,255,255,0.1); border-radius: 10px; height: 6px; overflow: hidden;">
                        <div style="background: {color}; width: {percentage}%; height: 100%; border-radius: 10px; transition: width 0.3s;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="text-align: center; padding: 2rem; background: rgba(255,255,255,0.05); border-radius: 10px;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">📊</div>
                <div style="color: #94a3b8; font-size: 0.9rem;">Aucune donnée</div>
                <div style="color: #64748b; font-size: 0.8rem; margin-top: 0.5rem;">Effectuez une analyse</div>
            </div>
            """, unsafe_allow_html=True)


def get_ultimate_badge(agent_name):
    """Badge ultra premium pour les agents."""
    badges = {
        "Market Analyst": '<span class="agent-badge-ultimate badge-market">📈 Market Analyst</span>',
        "Calculator": '<span class="agent-badge-ultimate badge-calc">🧮 Calculator</span>',
        "Researcher": '<span class="agent-badge-ultimate badge-research">🔍 Researcher</span>',
    }
    return badges.get(agent_name, f'<span class="agent-badge-ultimate">{agent_name}</span>')


def tab_home_ultimate():
    """Page d'accueil ultra premium."""
    
    # Hero Stats
    col1, col2, col3, col4 = st.columns(4)
    
    metrics_data = [
        ("🎯", "Agents", "4", "+3 depuis v1"),
        ("🛠️", "Tools", "13", "Multi-domaines"),
        ("⚡", "Uptime", "100%", "Toujours prêt"),
        ("🚀", "Speed", "<3s", "Moyenne")
    ]
    
    for col, (icon, label, value, delta) in zip([col1, col2, col3, col4], metrics_data):
        with col:
            st.markdown(f"""
            <div class="metric-ultimate">
                <div style="font-size: 2rem;">{icon}</div>
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div style="color: #94a3b8; font-size: 0.85rem;">{delta}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Features Grid
    st.markdown("### ⚡ Fonctionnalités Premium")
    
    col1, col2, col3 = st.columns(3)
    
    features = [
        ("🎯", "Routing Intelligent", "Le superviseur choisit automatiquement le meilleur agent pour votre requête"),
        ("📊", "Analytics Avancés", "Graphiques interactifs et dashboard complet avec insights"),
        ("💾", "Persistance", "Historique sauvegardé automatiquement entre les sessions"),
        ("📥", "Export Multi-format", "PDF et CSV avec formatage professionnel"),
        ("🔍", "Recherche Avancée", "Filtres multiples et recherche dans l'historique"),
        ("⭐", "Watchlist Live", "Suivez vos actions préférées en temps réel"),
    ]
    
    for i, (col, (icon, title, desc)) in enumerate(zip([col1, col2, col3] * 2, features)):
        with col:
            st.markdown(f"""
            <div class="glass-card" style="height: 300px; display: flex; flex-direction: column; justify-content: flex-start;">
                <div style="font-size: 2.5rem; margin-bottom: 1rem; flex-shrink: 0;">{icon}</div>
                <h3 style="color: #f1f5f9; margin-bottom: 0.5rem; flex-shrink: 0;">{title}</h3>
                <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.5; overflow: hidden;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick Start Examples
    st.markdown("### 🚀 Exemples Rapides")
    
    col1, col2, col3 = st.columns(3)
    
    examples_by_category = {
        col1: [
            ("📈 Analyse", [
                ("Prix AAPL", "Quel est le prix d'Apple ?"),
                ("Compare Tech", "Compare MSFT, GOOGL et AAPL"),
                ("Historique TSLA", "Historique Tesla 30 jours"),
            ])
        ],
        col2: [
            ("🧮 Calculs", [
                ("ROI", "ROI : investi 10000, valeur 15000"),
                ("Profit", "Acheté 50 à 100$, vendu à 150$"),
                ("Variation", "Variation entre 5000 et 7500"),
            ])
        ],
        col3: [
            ("🔍 Recherche", [
                ("News", "Actualités Tesla"),
                ("Sentiment", "Sentiment marché crypto"),
                ("Tendances", "Tendances tech actuelles"),
            ])
        ]
    }
    
    for col, items in examples_by_category.items():
        with col:
            for category, examples in items:
                st.markdown(f"**{category}**")
                for label, query in examples:
                    if st.button(f"💡 {label}", key=f"ex_{label}", use_container_width=True):
                        st.session_state.example_query = query
                        st.session_state.active_tab = 1


def tab_analyze_ultimate():
    """Onglet d'analyse ultra premium avec features avancées."""
    
    # Vérifier API
    if not os.getenv("OPENAI_API_KEY"):
        st.error("❌ OPENAI_API_KEY non configurée")
        return
    
    st.markdown("### 🎯 Analyse Intelligente")
    
    # Input avec suggestions
    query = st.text_area(
        "💬 Votre question financière",
        value=st.session_state.get('example_query', ''),
        placeholder="Ex: Analyse le prix d'Apple et calcule le ROI si j'investis 10000$...",
        height=120,
        key="query_ultimate"
    )
    
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    
    with col1:
        analyze = st.button("🚀 Analyser", type="primary", use_container_width=True)
    with col2:
        clear = st.button("🗑️ Effacer", use_container_width=True)
    with col3:
        fav = st.button("⭐ Favori", use_container_width=True, disabled=not query)
    with col4:
        voice = st.button("🎤 Voice", use_container_width=True, disabled=True)
    
    if clear:
        st.session_state.example_query = ""
        st.rerun()
    
    if fav and query:
        if query not in st.session_state.favorites:
            st.session_state.favorites.append(query)
            save_favorites()  # ✅ Sauvegarder
            st.success("✅ Ajouté aux favoris !")
            time.sleep(1)
            st.rerun()
        else:
            st.warning("⚠️ Cette requête est déjà dans vos favoris !")
        
    # Analyse
    if analyze and query:
        st.markdown("---")
        
        # Progress avec étapes
        progress_container = st.container()
        result_container = st.container()
        
        with progress_container:
            progress_bar = st.progress(0)
            status = st.empty()
            
            try:
                # Étape 1
                status.markdown("🤖 **Supervisor** analyse la requête...")
                progress_bar.progress(25)
                time.sleep(0.3)
                
                # Exécution
                response = st.session_state.supervisor.process(query)
                
                # Étape 2
                status.markdown(f"⚙️ **{response['agent_used']}** traite la demande...")
                progress_bar.progress(75)
                time.sleep(0.3)
                
                # Étape 3
                status.markdown("✨ **Génération** de la réponse...")
                progress_bar.progress(100)
                time.sleep(0.2)
                
                # Nettoyer
                progress_bar.empty()
                status.empty()
                
                # Stats
                agent_used = response['agent_used']
                if agent_used in st.session_state.agent_stats:
                    st.session_state.agent_stats[agent_used] += 1
                    save_agent_stats()
                
                # Historique
                st.session_state.history.append({
                    "query": query,
                    "agent": agent_used,
                    "response": response['result'],
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                save_history()
                
                # Affichage résultat
                with result_container:
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(get_ultimate_badge(agent_used), unsafe_allow_html=True)
                    with col2:
                        st.caption(f"⏱️ {datetime.now().strftime('%H:%M:%S')}")
                    
                    st.markdown(f"""
                    <div class="glass-card">
                        <h3 style="color: #f1f5f9; margin-bottom: 1rem;">💡 Réponse</h3>
                        <div style="color: #e2e8f0; line-height: 1.7;">
                            {response['result']}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Actions
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        if st.button("📋 Copier", key="copy"):
                            st.info("Utilisez Ctrl+C pour copier")
                    with col2:
                        if st.button("💾 Sauvegarder", key="save"):
                            st.success("Sauvegardé dans l'historique !")
                    with col3:
                        if st.button("🔄 Nouvelle", key="new"):
                            st.session_state.example_query = ""
                            st.rerun()
                
                if 'example_query' in st.session_state:
                    del st.session_state.example_query
                    
            except Exception as e:
                progress_bar.empty()
                status.empty()
                st.error(f"❌ Erreur: {str(e)}")


def tab_history_ultimate():
    """Historique ultra premium avec recherche avancée."""
    
    st.markdown("### 📜 Historique Complet")
    
    if not st.session_state.history:
        st.markdown("""
        <div class="glass-card" style="text-align: center; padding: 3rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">📭</div>
            <h3 style="color: #f1f5f9;">Aucune analyse dans l'historique</h3>
            <p style="color: #94a3b8;">Commencez par poser une question dans l'onglet Analyser !</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Filtres et export
    col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
    
    with col1:
        filter_agent = st.selectbox(
            "🔍 Filtrer par agent",
            ["Tous"] + list(st.session_state.agent_stats.keys())
        )
    
    with col2:
        search = st.text_input("🔎 Rechercher", "")
    
    with col3:
        if st.button("📥 PDF", use_container_width=True):
            try:
                filename = export_to_pdf(st.session_state.history)
                with open(filename, "rb") as f:
                    st.download_button("⬇️ DL", f, filename, "application/pdf")
            except Exception as e:
                st.error(str(e))
    
    with col4:
        if st.button("📊 CSV", use_container_width=True):
            try:
                filename = export_to_csv(st.session_state.history)
                with open(filename, "rb") as f:
                    st.download_button("⬇️ DL", f, filename, "text/csv")
            except Exception as e:
                st.error(str(e))
    
    # Filtrer
    filtered = st.session_state.history
    
    if filter_agent != "Tous":
        filtered = [h for h in filtered if h['agent'] == filter_agent]
    
    if search:
        filtered = [h for h in filtered 
                   if search.lower() in h['query'].lower() 
                   or search.lower() in h['response'].lower()]
    
    st.caption(f"**{len(filtered)}** résultat(s) sur {len(st.session_state.history)}")
    
    st.markdown("---")
    
    # Affichage
    for i, item in enumerate(reversed(filtered[-20:]), 1):
        with st.expander(
            f"🔹 [{item['timestamp']}] {item['query'][:60]}...",
            expanded=(i==1)
        ):
            st.markdown(get_ultimate_badge(item['agent']), unsafe_allow_html=True)
            st.markdown(f"**Question:** {item['query']}")
            st.markdown(f"**Réponse:** {item['response']}")


def tab_stats_ultimate():
    """Stats ultra premium avec graphiques avancés."""
    
    st.markdown("### 📊 Dashboard Analytics")
    
    if not st.session_state.history:
        st.info("Pas encore de données. Effectuez des analyses !")
        return
    
    total = len(st.session_state.history)
    
    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total", total, f"+{total}")
    with col2:
        st.metric("Market", st.session_state.agent_stats['Market Analyst'])
    with col3:
        st.metric("Calculator", st.session_state.agent_stats['Calculator'])
    with col4:
        st.metric("Research", st.session_state.agent_stats['Researcher'])
    
    st.markdown("---")
    
    # Graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Distribution")
        fig = px.pie(
            values=list(st.session_state.agent_stats.values()),
            names=list(st.session_state.agent_stats.keys()),
            color_discrete_sequence=['#667eea', '#f5576c', '#00f2fe']
        )
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#f1f5f9'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### Tendances")
        fig = go.Figure(data=[
            go.Bar(
                x=list(st.session_state.agent_stats.keys()),
                y=list(st.session_state.agent_stats.values()),
                marker_color=['#667eea', '#f5576c', '#00f2fe']
            )
        ])
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color='#f1f5f9'
        )
        st.plotly_chart(fig, use_container_width=True)

def tab_favorites_ultimate():
    """Onglet Favoris ultra premium."""
    
    st.markdown("### ⭐ Mes Favoris")
    
    if not st.session_state.favorites:
        st.markdown("""
        <div class="glass-card" style="text-align: center; padding: 3rem;">
            <div style="font-size: 4rem; margin-bottom: 1rem;">⭐</div>
            <h3 style="color: #f1f5f9;">Aucun favori enregistré</h3>
            <p style="color: #94a3b8;">Ajoutez vos requêtes préférées en cliquant sur ⭐ dans l'onglet Analyser</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    st.markdown(f"**{len(st.session_state.favorites)} requête(s) favorite(s)**")
    st.markdown("---")
    
    # Options de gestion
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🗑️ Tout effacer", use_container_width=True):
            st.session_state.favorites = []
            save_favorites()
            st.rerun()
    
    # Affichage des favoris avec style amélioré
    st.markdown("""
    <style>
    .fav-container {
        display: grid;
        grid-template-columns: 8fr 1fr 1fr;
        gap: 0.5rem;
        margin-bottom: 0.75rem;
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

    for i, fav_query in enumerate(st.session_state.favorites):
        col1, col2, col3 = st.columns([8, 1, 1])
        
        with col1:
            st.markdown(f"""
            <div class="glass-card" style="padding: 1.2rem 1rem; margin: 0;">
                <p style="color: #f1f5f9; margin: 0; font-size: 1.05rem;">
                    {fav_query}
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div style="height: 100%;">', unsafe_allow_html=True)
            if st.button("🚀", key=f"use_fav_{i}", use_container_width=True, help="Utiliser"):
                st.session_state.example_query = fav_query
                st.session_state.active_tab = 1
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col3:
            st.markdown('<div style="height: 100%;">', unsafe_allow_html=True)
            if st.button("❌", key=f"del_fav_{i}", use_container_width=True, help="Supprimer"):
                st.session_state.favorites.pop(i)
                save_favorites()
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Statistiques
    st.markdown("---")
    st.markdown("### 📊 Statistiques")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class="metric-ultimate">
            <div style="font-size: 2rem;">⭐</div>
            <div class="metric-label">Total Favoris</div>
            <div class="metric-value">{len(st.session_state.favorites)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Calculer la longueur moyenne
        avg_length = sum(len(f) for f in st.session_state.favorites) / len(st.session_state.favorites) if st.session_state.favorites else 0
        st.markdown(f"""
        <div class="metric-ultimate">
            <div style="font-size: 2rem;">📏</div>
            <div class="metric-label">Longueur Moyenne</div>
            <div class="metric-value">{avg_length:.0f}</div>
            <div style="color: #94a3b8; font-size: 0.85rem;">caractères</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # Trouver le favori le plus long
        longest = max(st.session_state.favorites, key=len) if st.session_state.favorites else ""
        st.markdown(f"""
        <div class="metric-ultimate">
            <div style="font-size: 2rem;">🏆</div>
            <div class="metric-label">Plus Long</div>
            <div class="metric-value">{len(longest)}</div>
            <div style="color: #94a3b8; font-size: 0.85rem;">caractères</div>
        </div>
        """, unsafe_allow_html=True)

def main():
    """Fonction principale."""
    initialize_session_state()
    display_ultimate_header()
    display_premium_sidebar()
    
    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏠 Accueil",
        "🎯 Analyser", 
        "⭐ Favoris",
        "📜 Historique",
        "📊 Stats"
    ])

    with tab1:
        tab_home_ultimate()

    with tab2:
        tab_analyze_ultimate()

    with tab3:
        tab_favorites_ultimate()

    with tab4:
        tab_history_ultimate()

    with tab5:
        tab_stats_ultimate()
    
    # Footer
    st.markdown("""
    <div class="ultimate-footer">
        <p style="font-size: 0.95rem;">💎 <strong>Financial Intelligence Ultimate Edition</strong> v2.0</p>
        <p style="font-size: 0.85rem; margin-top: 0.5rem;">
            Powered by LangGraph • OpenAI GPT-4o-mini • Real-time Market Data
        </p>
        <p style="font-size: 0.8rem; margin-top: 1rem; color: #64748b;">
            Made with ❤️ by Mathis Meimoun • © 2024
        </p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()