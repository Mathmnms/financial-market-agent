"""
Utilitaires pour l'export des résultats.
"""
from fpdf import FPDF
import pandas as pd
from datetime import datetime
import re


def clean_text_for_pdf(text):
    """Nettoie le texte pour l'export PDF (retire markdown, emojis)."""
    # Retirer les emojis
    text = text.encode('ascii', 'ignore').decode('ascii')
    # Retirer le markdown basique
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)  # Bold
    text = re.sub(r'\*(.+?)\*', r'\1', text)      # Italic
    text = re.sub(r'`(.+?)`', r'\1', text)        # Code
    text = re.sub(r'#+\s', '', text)              # Headers
    return text


def export_to_pdf(history_items, filename="financial_report.pdf"):
    """
    Exporte l'historique en PDF.
    
    Args:
        history_items: Liste des items d'historique
        filename: Nom du fichier PDF
    
    Returns:
        Chemin du fichier créé
    """
    pdf = FPDF()
    pdf.add_page()
    
    # En-tête
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Financial Market Intelligence Report", ln=True, align="C")
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 10, f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
    pdf.ln(10)
    
    # Contenu
    pdf.set_font("Arial", "", 11)
    
    for i, item in enumerate(history_items, 1):
        # Titre de la requête
        pdf.set_font("Arial", "B", 12)
        pdf.multi_cell(0, 8, f"{i}. {clean_text_for_pdf(item['query'])}")
        
        # Infos
        pdf.set_font("Arial", "I", 10)
        pdf.cell(0, 6, f"Agent: {item['agent']} | Time: {item['timestamp']}", ln=True)
        pdf.ln(2)
        
        # Réponse
        pdf.set_font("Arial", "", 10)
        response_text = clean_text_for_pdf(item['response'])
        # Limiter la longueur pour éviter les pages trop longues
        if len(response_text) > 1000:
            response_text = response_text[:1000] + "..."
        pdf.multi_cell(0, 5, response_text)
        pdf.ln(5)
        
        # Séparateur
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.ln(5)
    
    # Sauvegarder
    pdf.output(filename)
    return filename


def export_to_csv(history_items, filename="financial_data.csv"):
    """
    Exporte l'historique en CSV.
    
    Args:
        history_items: Liste des items d'historique
        filename: Nom du fichier CSV
    
    Returns:
        Chemin du fichier créé
    """
    df = pd.DataFrame(history_items)
    df.to_csv(filename, index=False, encoding='utf-8')
    return filename