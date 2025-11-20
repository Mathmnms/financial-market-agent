"""
Tools financiers pour l'analyse de marché.
"""
from langchain_core.tools import tool
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
from typing import Optional


@tool
def get_stock_price(symbol: str) -> str:
    """
    Récupère le prix actuel d'une action avec variation.
    
    Args:
        symbol: Symbole de l'action (ex: AAPL, MSFT, GOOGL)
    
    Returns:
        Prix actuel, variation et statistiques du jour
    """
    try:
        stock = yf.Ticker(symbol.upper())
        info = stock.info
        
        current_price = info.get('currentPrice', info.get('regularMarketPrice'))
        previous_close = info.get('previousClose')
        day_high = info.get('dayHigh')
        day_low = info.get('dayLow')
        volume = info.get('volume', 0)
        
        if current_price and previous_close:
            change = current_price - previous_close
            change_pct = (change / previous_close) * 100
            
            return f"""
{symbol.upper()} - {info.get('longName', 'N/A')}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 Prix actuel: ${current_price:.2f}
📊 Variation: {change:+.2f} ({change_pct:+.2f}%)
📈 Plus haut du jour: ${day_high:.2f}
📉 Plus bas du jour: ${day_low:.2f}
📦 Volume: {volume:,}
🕐 Clôture précédente: ${previous_close:.2f}
"""
        return f"Impossible de récupérer le prix pour {symbol}"
    except Exception as e:
        return f"❌ Erreur: {str(e)}"


@tool
def get_stock_history(symbol: str, period: str = "1mo") -> str:
    """
    Récupère l'historique d'une action avec statistiques.
    
    Args:
        symbol: Symbole de l'action
        period: Période (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, max)
    
    Returns:
        Statistiques détaillées sur la période
    """
    try:
        stock = yf.Ticker(symbol.upper())
        hist = stock.history(period=period)
        
        if hist.empty:
            return f"Aucune donnée disponible pour {symbol}"
        
        # Calculs statistiques
        current = hist['Close'].iloc[-1]
        start = hist['Close'].iloc[0]
        min_price = hist['Close'].min()
        max_price = hist['Close'].max()
        avg_price = hist['Close'].mean()
        volatility = hist['Close'].std()
        total_change = ((current - start) / start) * 100
        
        return f"""
{symbol.upper()} - Historique {period}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Prix actuel: ${current:.2f}
📈 Plus haut: ${max_price:.2f}
📉 Plus bas: ${min_price:.2f}
📊 Moyenne: ${avg_price:.2f}
📊 Volatilité: ${volatility:.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💹 Performance: {total_change:+.2f}%
"""
    except Exception as e:
        return f"❌ Erreur: {str(e)}"


@tool
def compare_stocks(symbols: str) -> str:
    """
    Compare plusieurs actions côte à côte.
    
    Args:
        symbols: Symboles séparés par des virgules (ex: AAPL,MSFT,GOOGL)
    
    Returns:
        Tableau comparatif des actions
    """
    try:
        symbol_list = [s.strip().upper() for s in symbols.split(',')]
        comparisons = []
        
        for symbol in symbol_list:
            stock = yf.Ticker(symbol)
            info = stock.info
            
            price = info.get('currentPrice', info.get('regularMarketPrice', 0))
            previous = info.get('previousClose', price)
            change_pct = ((price - previous) / previous * 100) if previous else 0
            market_cap = info.get('marketCap', 0)
            pe_ratio = info.get('trailingPE', 'N/A')
            
            comparisons.append(
                f"{symbol}: ${price:.2f} ({change_pct:+.2f}%) | "
                f"P/E: {pe_ratio if pe_ratio == 'N/A' else f'{pe_ratio:.2f}'} | "
                f"Cap: ${market_cap/1e9:.1f}B"
            )
        
        return "📊 COMPARAISON DES ACTIONS\n" + "━"*50 + "\n" + "\n".join(comparisons)
    except Exception as e:
        return f"❌ Erreur: {str(e)}"


@tool
def get_company_info(symbol: str) -> str:
    """
    Récupère les informations détaillées d'une entreprise.
    
    Args:
        symbol: Symbole de l'action
    
    Returns:
        Informations complètes sur l'entreprise
    """
    try:
        stock = yf.Ticker(symbol.upper())
        info = stock.info
        
        return f"""
🏢 {info.get('longName', symbol.upper())}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏭 Secteur: {info.get('sector', 'N/A')}
🔧 Industrie: {info.get('industry', 'N/A')}
🌍 Pays: {info.get('country', 'N/A')}
👥 Employés: {info.get('fullTimeEmployees', 0):,}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 Capitalisation: ${info.get('marketCap', 0)/1e9:.2f}B
📊 P/E Ratio: {info.get('trailingPE', 'N/A')}
📈 EPS: ${info.get('trailingEps', 'N/A')}
💵 Dividende: {info.get('dividendYield', 0)*100:.2f}%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 Description:
{info.get('longBusinessSummary', 'N/A')[:300]}...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 Site web: {info.get('website', 'N/A')}
"""
    except Exception as e:
        return f"❌ Erreur: {str(e)}"


# Export des tools
finance_tools = [
    get_stock_price,
    get_stock_history,
    compare_stocks,
    get_company_info
]