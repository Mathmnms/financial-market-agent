"""
Tools de recherche et d'analyse de marché.
"""
from langchain_core.tools import tool
from tavily import TavilyClient
import os
from datetime import datetime


@tool
def web_search(query: str) -> str:
    """
    Recherche d'informations sur le web.
    
    Args:
        query: Question ou terme de recherche
    
    Returns:
        Résultats pertinents de la recherche
    """
    try:
        tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        response = tavily_client.search(query, max_results=5)
        
        results = []
        for i, result in enumerate(response.get('results', []), 1):
            results.append(
                f"{i}. {result['title']}\n"
                f"   📰 {result['content'][:200]}...\n"
                f"   🔗 {result['url']}"
            )
        
        return "🔍 RÉSULTATS DE RECHERCHE\n" + "━"*50 + "\n\n" + "\n\n".join(results)
    except Exception as e:
        return f"❌ Erreur de recherche: {str(e)}"


@tool
def search_financial_news(company_or_topic: str) -> str:
    """
    Recherche des actualités financières récentes.
    
    Args:
        company_or_topic: Entreprise ou sujet financier
    
    Returns:
        Actualités financières pertinentes
    """
    try:
        tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        
        query = f"{company_or_topic} financial news stock market"
        response = tavily_client.search(
            query, 
            max_results=5,
            search_depth="advanced",
            topic="news"
        )
        
        news = []
        for i, result in enumerate(response.get('results', []), 1):
            news.append(
                f"{i}. 📰 {result['title']}\n"
                f"   {result['content'][:250]}...\n"
                f"   🔗 Source: {result['url']}\n"
            )
        
        return f"""
📰 ACTUALITÉS FINANCIÈRES - {company_or_topic.upper()}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{chr(10).join(news)}
"""
    except Exception as e:
        return f"❌ Erreur: {str(e)}"


@tool
def get_market_sentiment(topic: str) -> str:
    """
    Analyse le sentiment du marché sur un sujet.
    
    Args:
        topic: Sujet ou entreprise à analyser
    
    Returns:
        Analyse du sentiment basée sur les actualités
    """
    try:
        tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        
        query = f"{topic} market sentiment analysis opinion"
        response = tavily_client.search(query, max_results=5, search_depth="advanced")
        
        articles = []
        for result in response.get('results', [])[:3]:
            articles.append(f"• {result['content'][:150]}...")
        
        return f"""
📊 SENTIMENT DU MARCHÉ - {topic.upper()}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Analyse basée sur les sources récentes:

{chr(10).join(articles)}

⚠️ Note: Cette analyse est basée sur des sources publiques.
Consultez un conseiller financier pour des décisions d'investissement.
"""
    except Exception as e:
        return f"❌ Erreur: {str(e)}"


@tool
def get_current_time() -> str:
    """
    Retourne la date et l'heure actuelles.
    
    Returns:
        Date et heure formatées
    """
    now = datetime.now()
    return f"📅 {now.strftime('%d/%m/%Y')} ⏰ {now.strftime('%H:%M:%S')}"


# Export des tools
research_tools = [
    web_search,
    search_financial_news,
    get_market_sentiment,
    get_current_time
]