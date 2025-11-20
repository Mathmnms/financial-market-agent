"""
Point d'entrée principal pour l'agent financier avec LangGraph.
"""
import os
from dotenv import load_dotenv
from agents.langgraph_system import LangGraphFinancialAgent

# Charger les variables d'environnement
load_dotenv()


def print_header():
    """Affiche l'en-tête de l'application."""
    print("\n" + "="*70)
    print("💼 FINANCIAL MARKET INTELLIGENCE AGENT")
    print("🤖 Architecture Multi-Agents avec LangGraph")
    print("="*70)


def print_result(response: dict):
    """Affiche le résultat d'une requête."""
    print("\n" + "─"*70)
    print(f"📝 REQUÊTE: {response['query']}")
    print(f"🤖 AGENT UTILISÉ: {response['agent_used']}")
    print("─"*70)
    print(f"\n💡 RÉPONSE:\n{response['result']}")
    print("\n" + "="*70)


def run_interactive_mode():
    """Mode interactif pour poser des questions."""
    print_header()
    
    # Initialiser le système LangGraph
    print("\n🔄 Initialisation du système LangGraph...")
    agent_system = LangGraphFinancialAgent()
    print("✅ Système prêt!\n")
    
    # Afficher le graphe
    agent_system.visualize()
    
    # Exemples de requêtes
    examples = [
        "Quel est le prix actuel de Apple (AAPL) ?",
        "Calcule mon ROI si j'ai investi 10000 dollars et que j'ai maintenant 15000 dollars",
        "Quelles sont les dernières actualités sur Tesla ?",
        "Compare les actions Microsoft et Google",
    ]
    
    print("📋 EXEMPLES DE REQUÊTES:")
    print("─"*70)
    for i, example in enumerate(examples, 1):
        print(f"{i}. {example}")
    print("─"*70)
    
    while True:
        print("\n💬 Tapez votre question (ou 'q' pour quitter, '1-4' pour un exemple):")
        user_input = input("➤ ").strip()
        
        if user_input.lower() in ['q', 'quit', 'exit']:
            print("\n👋 Au revoir!")
            break
        
        # Sélection d'un exemple
        if user_input.isdigit() and 1 <= int(user_input) <= len(examples):
            query = examples[int(user_input) - 1]
        else:
            query = user_input
        
        if not query:
            print("⚠️  Veuillez entrer une question.")
            continue
        
        # Traiter la requête
        print("\n🔄 Analyse en cours...")
        try:
            response = agent_system.process(query)
            print_result(response)
        except Exception as e:
            print(f"\n❌ Erreur: {str(e)}")


def run_demo_mode():
    """Mode démo avec des exemples prédéfinis."""
    print_header()
    
    print("\n🎬 MODE DÉMO - Exemples d'utilisation\n")
    
    # Initialiser le système
    print("🔄 Initialisation du système LangGraph...")
    agent_system = LangGraphFinancialAgent()
    print("✅ Système prêt!\n")
    
    # Afficher le graphe
    agent_system.visualize()
    
    # Exemples de démonstration
    demo_queries = [
        "Calcule le ROI : investissement initial 5000, valeur finale 7500",
        "Quelles sont les actualités récentes sur le marché des actions technologiques ?",
        "Si j'achète à 100 dollars et je vends à 150 dollars, 50 actions, quel est mon profit ?",
    ]
    
    for i, query in enumerate(demo_queries, 1):
        print(f"\n{'='*70}")
        print(f"📍 DEMO {i}/{len(demo_queries)}")
        print(f"{'='*70}")
        
        try:
            response = agent_system.process(query)
            print_result(response)
            
            if i < len(demo_queries):
                input("\n⏸️  Appuyez sur Entrée pour continuer...")
        except Exception as e:
            print(f"\n❌ Erreur: {str(e)}")


def main():
    """Fonction principale."""
    # Vérifier les clés API
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Erreur: OPENAI_API_KEY non trouvée dans .env")
        return
    
    if not os.getenv("TAVILY_API_KEY"):
        print("⚠️  Avertissement: TAVILY_API_KEY non trouvée (recherche web désactivée)")
    
    # Menu principal
    print("\n" + "="*70)
    print("💼 FINANCIAL MARKET INTELLIGENCE AGENT")
    print("🔄 Utilise LangGraph pour l'orchestration multi-agents")
    print("="*70)
    print("\nChoisissez un mode:")
    print("1. Mode interactif (poser vos questions)")
    print("2. Mode démo (exemples prédéfinis)")
    print("3. Quitter")
    print("─"*70)
    
    choice = input("\n➤ Votre choix (1-3): ").strip()
    
    if choice == "1":
        run_interactive_mode()
    elif choice == "2":
        run_demo_mode()
    elif choice == "3":
        print("\n👋 Au revoir!")
    else:
        print("\n❌ Choix invalide.")


if __name__ == "__main__":
    main()