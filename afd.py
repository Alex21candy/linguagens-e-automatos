# Autômato Finito Determinístico (AFD)
# Linguagem: cadeias sobre {a, e, i, o, u, b, p, m, n} onde:
# - n não pode aparecer imediatamente antes de b ou p
# - aceita qualquer palavra válida com essas letras

# Definição do AFD como 5-tupla M = (Q, Σ, δ, q0, F)

# Conjunto de estados
Q = {"q0", "q_normal", "q_n", "q_dead"}

# Alfabeto (vogais + consoantes permitidas)
Sigma = {"a", "e", "i", "o", "u", "b", "p", "m", "n"}

# Estado inicial
q0 = "q0"

# Conjunto de estados finais (aceita em q_normal e q_n, mas não em q_dead)
F = {"q_normal", "q_n"}

# Função de transição δ
# Explicação dos estados:
# q0: estado inicial
# q_normal: estado normal (qualquer letra exceto n acabou de ser lida)
# q_n: acabou de ler 'n' (precisa verificar se próxima é b ou p)
# q_dead: erro - tentou colocar n antes de b ou p

delta = {
    # Estado inicial
    "q0": {
        "a": "q_normal", "e": "q_normal", "i": "q_normal", 
        "o": "q_normal", "u": "q_normal",  # vogais vão para normal
        "b": "q_normal", "p": "q_normal", "m": "q_normal",  # consoantes permitidas
        "n": "q_n"  # n vai para estado especial
    },
    
    # Estado normal (qualquer letra menos n)
    "q_normal": {
        "a": "q_normal", "e": "q_normal", "i": "q_normal",
        "o": "q_normal", "u": "q_normal",  # vogais continuam normal
        "b": "q_normal", "p": "q_normal", "m": "q_normal",  # consoantes ok
        "n": "q_n"  # n vai para estado especial
    },
    
    # Estado após ler 'n' (não pode ler b ou p agora!)
    "q_n": {
        "a": "q_normal", "e": "q_normal", "i": "q_normal",
        "o": "q_normal", "u": "q_normal",  # vogais ok, volta ao normal
        "b": "q_dead", "p": "q_dead",  # ERRO! n seguido de b ou p
        "m": "q_normal",  # m é permitido após n
        "n": "q_n"  # outro n, continua no estado n
    },
    
    # Estado morto (erro)
    "q_dead": {
        "a": "q_dead", "e": "q_dead", "i": "q_dead",
        "o": "q_dead", "u": "q_dead", "b": "q_dead", 
        "p": "q_dead", "m": "q_dead", "n": "q_dead"
    }
}

def simular(cadeia: str) -> bool:
    """Simula o AFD para a cadeia fornecida"""
    estado_atual = q0
    print(f"\n--- Simulando cadeia: '{cadeia}' ---")
    print(f"Estado inicial: {estado_atual}")
    
    for i, simbolo in enumerate(cadeia):
        if simbolo not in Sigma:
            print(f"❌ Símbolo inválido '{simbolo}' na posição {i}. Rejeitando...")
            return False
        
        estado_anterior = estado_atual
        estado_atual = delta[estado_atual][simbolo]
        
        print(f"Posição {i}: '{simbolo}' | {estado_anterior} → {estado_atual}")
        
        # Se chegou no estado morto, pode parar
        if estado_atual == "q_dead":
            print("💀 Chegou ao estado morto (n seguido de b ou p)")
            break
    
    # Aceita se terminar em um estado final
    if estado_atual in F:
        print(f"✅ Cadeia ACEITA! Estado final: {estado_atual}")
        return True
    else:
        print(f"❌ Cadeia REJEITADA. Estado final: {estado_atual}")
        return False

def testar_exemplos():
    """Testa alguns exemplos para demonstrar o funcionamento"""
    print("=== TESTANDO EXEMPLOS ===")
    
    # Palavras que DEVEM ser aceitas
    aceitas = [
        "amor",      # a-m-o-r (normal)
        "menina",    # m-e-n-i-n-a (n não antes de b/p)
        "uno",       # u-n-o (n não antes de b/p)
        "banana",    # b-a-n-a-n-a (n não antes de b/p)
        "nome",      # n-o-m-e (n no início, ok)
        "anima",     # a-n-i-m-a (n não antes de b/p)
        "meia"       # m-e-i-a (sem n)
    ]
    
    # Palavras que DEVEM ser rejeitadas
    rejeitadas = [
        "anbo",      # a-n-b-o (n antes de b - ERRO!)
        "unpa",      # u-n-p-a (n antes de p - ERRO!)
        "manbo",     # m-a-n-b-o (n antes de b - ERRO!)
        "inpe"       # i-n-p-e (n antes de p - ERRO!)
    ]
    
    print("\n🟢 Palavras que DEVEM ser aceitas:")
    for palavra in aceitas:
        resultado = simular(palavra)
        print("-" * 50)
    
    print("\n🔴 Palavras que DEVEM ser rejeitadas:")
    for palavra in rejeitadas:
        resultado = simular(palavra)
        print("-" * 50)

def main():
    """Função principal com loop interativo"""
    print("🤖 AUTÔMATO FINITO - LEITOR DE PALAVRAS")
    print("="*50)
    print("Alfabeto permitido: a, e, i, o, u, b, p, m, n")
    print("Regra: 'n' não pode vir imediatamente antes de 'b' ou 'p'")
    print("="*50)
    
    while True:
        print("\nOpções:")
        print("1 - Testar uma palavra")
        print("2 - Ver exemplos de teste")
        print("3 - Ver definição formal do autômato")
        print("0 - Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        if opcao == "1":
            entrada = input("\nDigite uma palavra: ").strip().lower()
            if entrada:
                resultado = simular(entrada)
                print("\n" + "="*30)
                print(f"RESULTADO: {'ACEITA' if resultado else 'REJEITADA'}")
                print("="*30)
            else:
                print("❌ Entrada vazia!")
                
        elif opcao == "2":
            testar_exemplos()
            
        elif opcao == "3":
            print("\n📋 DEFINIÇÃO FORMAL DO AUTÔMATO:")
            print(f"Q (Estados): {Q}")
            print(f"Σ (Alfabeto): {Sigma}")
            print(f"q₀ (Estado inicial): {q0}")
            print(f"F (Estados finais): {F}")
            print("\nδ (Função de transição):")
            for estado, transicoes in delta.items():
                print(f"  {estado}: {transicoes}")
                
        elif opcao == "0":
            print("👋 Tchau! Obrigado por usar o autômato!")
            break
            
        else:
            print("❌ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()