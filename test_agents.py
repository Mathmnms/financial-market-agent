"""
Script de test pour vérifier que tous les agents fonctionnent.
"""
from agents.supervisor import SupervisorAgent


def test_supervisor():
    """Test du système multi-agents."""
    print("🧪 TEST DU SYSTÈME MULTI-AGENTS\n")
    print("="*60)
    
    supervisor = SupervisorAgent()
    
    # Test 1: Calcul simple
    print("\n📊 TEST 1: Calcul financier")
    print("-"*60)
    query1 = "Calcule mon ROI: investissement 1000, valeur finale 1500"
    response1 = supervisor.process(query1)
    print(f"Agent utilisé: {response1['agent_used']}")
    print(f"Réponse: {response1['result'][:100]}...")
    
    # Test 2: Routing
    print("\n🔀 TEST 2: Routing du superviseur")
    print("-"*60)
    test_queries = [
        "Quel est le prix de Apple?",
        "Calcule 10% de variation",
        "Actualités sur Tesla"
    ]
    
    for query in test_queries:
        agent = supervisor.route(query)
        print(f"'{query}' → {agent}")
    
    print("\n" + "="*60)
    print("✅ Tests terminés!")


if __name__ == "__main__":
    test_supervisor()