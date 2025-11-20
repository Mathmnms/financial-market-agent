"""
Tools de calcul financier avancé.
"""
from langchain_core.tools import tool
from typing import Optional


@tool
def calculate_roi(initial_investment: float, final_value: float) -> str:
    """
    Calcule le retour sur investissement (ROI).
    
    Args:
        initial_investment: Montant initial investi
        final_value: Valeur finale de l'investissement
    
    Returns:
        ROI en pourcentage et gain/perte
    """
    try:
        roi = ((final_value - initial_investment) / initial_investment) * 100
        gain_loss = final_value - initial_investment
        
        emoji = "📈" if gain_loss > 0 else "📉"
        
        return f"""
{emoji} RETOUR SUR INVESTISSEMENT (ROI)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 Investissement initial: ${initial_investment:,.2f}
💵 Valeur finale: ${final_value:,.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 ROI: {roi:+.2f}%
{emoji} Gain/Perte: ${gain_loss:+,.2f}
"""
    except Exception as e:
        return f"❌ Erreur de calcul: {str(e)}"


@tool
def calculate_portfolio_value(holdings: str) -> str:
    """
    Calcule la valeur totale d'un portefeuille.
    
    Args:
        holdings: Format "SYMBOL:QUANTITY,SYMBOL:QUANTITY" (ex: "AAPL:10,MSFT:5")
    
    Returns:
        Valeur totale et détails par action
    """
    try:
        import yfinance as yf
        
        holdings_list = [h.strip() for h in holdings.split(',')]
        total_value = 0
        details = []
        
        for holding in holdings_list:
            symbol, quantity = holding.split(':')
            symbol = symbol.strip().upper()
            quantity = float(quantity.strip())
            
            stock = yf.Ticker(symbol)
            price = stock.info.get('currentPrice', stock.info.get('regularMarketPrice', 0))
            value = price * quantity
            total_value += value
            
            details.append(f"{symbol}: {quantity} actions × ${price:.2f} = ${value:,.2f}")
        
        return f"""
💼 VALEUR DU PORTEFEUILLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{chr(10).join(details)}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 VALEUR TOTALE: ${total_value:,.2f}
"""
    except Exception as e:
        return f"❌ Erreur: {str(e)}"


@tool
def calculate_profit_loss(buy_price: float, sell_price: float, quantity: int) -> str:
    """
    Calcule le profit ou la perte sur une transaction.
    
    Args:
        buy_price: Prix d'achat par action
        sell_price: Prix de vente par action
        quantity: Nombre d'actions
    
    Returns:
        Profit/perte en dollars et pourcentage
    """
    try:
        cost = buy_price * quantity
        revenue = sell_price * quantity
        profit_loss = revenue - cost
        percentage = (profit_loss / cost) * 100
        
        emoji = "📈 PROFIT" if profit_loss > 0 else "📉 PERTE"
        
        return f"""
{emoji}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📥 Prix d'achat: ${buy_price:.2f} × {quantity} = ${cost:,.2f}
📤 Prix de vente: ${sell_price:.2f} × {quantity} = ${revenue:,.2f}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💵 Résultat: ${profit_loss:+,.2f} ({percentage:+.2f}%)
"""
    except Exception as e:
        return f"❌ Erreur: {str(e)}"


@tool
def calculate_moving_average(symbol: str, days: int = 50) -> str:
    """
    Calcule la moyenne mobile d'une action.
    
    Args:
        symbol: Symbole de l'action
        days: Nombre de jours pour la moyenne (défaut: 50)
    
    Returns:
        Moyenne mobile et analyse de tendance
    """
    try:
        import yfinance as yf
        
        stock = yf.Ticker(symbol.upper())