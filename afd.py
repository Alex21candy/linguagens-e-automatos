# Autômato Finito Determinístico (AFD)
# Linguagem: cadeias sobre {b, c, d} que
# - começam com 'b'
# - possuem pelo menos um 'c'
# - possuem pelo menos um 'd'

# Definição do AFD como 5-tupla M = (Q, Σ, δ, q0, F)

# Conjunto de estados
Q = {"q0", "q_dead", "q1", "q_c", "q_d", "q_cd"}

# Alfabeto
Sigma = {"b", "c", "d"}

# Estado inicial
q0 = "q0"

# Conjunto de estados finais
F = {"q_cd"}

# Função de transição δ (dicionário de dicionários)
delta = {
    "q0":     {"b": "q1", "c": "q_dead", "d": "q_dead"},
    "q_dead": {"b": "q_dead", "c": "q_dead", "d": "q_dead"},
    "q1":     {"b": "q1", "c": "q_c", "d": "q_d"},
    "q_c":    {"b": "q_c", "c": "q_c", "d": "q_cd"},
    "q_d":    {"b": "q_d", "c": "q_cd", "d": "q_d"},
    "q_cd":   {"b": "q_cd", "c": "q_cd", "d": "q_cd"},
}


def simular(cadeia: str) -> bool:
    """Simula o AFD para a cadeia fornecida"""
    estado_atual = q0
    print(f"Estado inicial: {estado_atual}")

    for simbolo in cadeia:
        if simbolo not in Sigma:
            print(f"Símbolo inválido '{simbolo}' encontrado. Rejeitando...")
            return False

        estado_atual = delta[estado_atual][simbolo]
        print(f"Lendo '{simbolo}' → indo para {estado_atual}")

    # Aceita se terminar em um estado final
    if estado_atual in F:
        print(f"Cadeia aceita! Estado final: {estado_atual}")
        return True
    else:
        print(f"Cadeia rejeitada. Estado final: {estado_atual}")
        return False


if __name__ == "__main__":
    entrada = input("Digite uma cadeia (somente b, c, d): ").strip()
    resultado = simular(entrada)
    print("Resultado:", "ACEITA" if resultado else "REJEITADA")
