"""
Tools de calcul financier avancé.
"""
from langchain_core.tools import tool


@tool
def calculate_roi(initial_investment: float, final_value: float) -> str:
    """Calcule le retour sur investissement (ROI)."""
    try:
        roi = ((final_value - initial_investment) / initial_investment) * 100
        gain_loss = final_value - initial_investment
        emoji = "📈" if gain_loss > 0 else "📉"
        return f"{emoji} ROI: {roi:+.2f}% | Gain/Perte: ${gain_loss:+,.2f}"
    except Exception as e:
        return f"❌ Erreur: {str(e)}"


@tool
def calculate_profit_loss(buy_price: float, sell_price: float, quantity: int) -> str:
    """Calcule le profit ou la perte sur une transaction."""
    try:
        cost = buy_price * quantity
        revenue = sell_price * quantity
        profit_loss = revenue - cost
        percentage = (profit_loss / cost) * 100
        emoji = "📈" if profit_loss > 0 else "📉"
        return f"{emoji} Résultat: ${profit_loss:+,.2f} ({percentage:+.2f}%)"
    except Exception as e:
        return f"❌ Erreur: {str(e)}"


@tool
def calculate_percent_change(old_value: float, new_value: float) -> str:
    """Calcule le pourcentage de variation entre deux valeurs."""
    try:
        change = ((new_value - old_value) / old_value) * 100
        emoji = "📈" if change > 0 else "📉"
        return f"{emoji} Variation: {change:+.2f}%"
    except Exception as e:
        return f"❌ Erreur: {str(e)}"


# Export
calculator_tools = [
    calculate_roi,
    calculate_profit_loss,
    calculate_percent_change
]