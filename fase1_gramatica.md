# Fase 1 – Definição do Autômato Finito Determinístico (AFD)

## Linguagem
Cadeias sobre o alfabeto `{a, e, i, o, u, b, p, m, n}` onde:

- A letra **`n` não pode aparecer imediatamente antes de `b` ou `p`**.
- Aceita qualquer palavra válida que respeite essa restrição.

---

## 1. Alfabeto (Σ)

Σ = {a, e, i, o, u, b, p, m, n}

---

## 2. Conjunto de Estados (Q)

Q = {`q0`, `q_normal`, `q_n`, `q_dead`}

- `q0`: estado inicial
- `q_normal`: estado normal (último símbolo não foi `n`)
- `q_n`: acabou de ler `n`
- `q_dead`: estado de erro (quando `n` é seguido por `b` ou `p`)

---

## 3. Estado Inicial

q0

---

## 4. Conjunto de Estados Finais (F)

F = {`q_normal`, `q_n`}

Aceita cadeias que terminem em `q_normal` ou `q_n`. Cadeias que chegam a `q_dead` são rejeitadas.

---

## 5. Função de Transição (δ)

A função de transição é definida como:

### δ(q0, símbolo)

| Símbolo | Destino     |
|---------|-------------|
| a, e, i, o, u | q_normal |
| b, p, m       | q_normal |
| n             | q_n      |

---

### δ(q_normal, símbolo)

| Símbolo | Destino     |
|---------|-------------|
| a, e, i, o, u | q_normal |
| b, p, m       | q_normal |
| n             | q_n      |

---

### δ(q_n, símbolo)

| Símbolo | Destino     |
|---------|-------------|
| a, e, i, o, u | q_normal |
| m             | q_normal |
| b, p          | q_dead   |
| n             | q_n      |

---

### δ(q_dead, símbolo)

Todos os símbolos levam de volta a `q_dead`.

---

## 6. Exemplos de Cadeias

### ✅ Cadeias Aceitas
- `amor`  
- `menina`  
- `uno`  
- `banana`  
- `nome`  
- `anima`  
- `meia`  

### ❌ Cadeias Rejeitadas
- `anbo`   → `n` antes de `b`  
- `unpa`   → `n` antes de `p`  
- `manbo`  → `n` antes de `b`  
- `inpe`   → `n` antes de `p`  

---

## 7. Implementação (Python)

```python
# Alfabeto
Sigma = {"a", "e", "i", "o", "u", "b", "p", "m", "n"}

# Estados
Q = {"q0", "q_normal", "q_n", "q_dead"}

# Estado inicial
q0 = "q0"

# Estados finais
F = {"q_normal", "q_n"}

# Função de transição
delta = {
    "q0": {
        "a": "q_normal", "e": "q_normal", "i": "q_normal", 
        "o": "q_normal", "u": "q_normal",
        "b": "q_normal", "p": "q_normal", "m": "q_normal",
        "n": "q_n"
    },
    "q_normal": {
        "a": "q_normal", "e": "q_normal", "i": "q_normal", 
        "o": "q_normal", "u": "q_normal",
        "b": "q_normal", "p": "q_normal", "m": "q_normal",
        "n": "q_n"
    },
    "q_n": {
        "a": "q_normal", "e": "q_normal", "i": "q_normal", 
        "o": "q_normal", "u": "q_normal",
        "m": "q_normal",
        "b": "q_dead", "p": "q_dead",
        "n": "q_n"
    },
    "q_dead": {
        "a": "q_dead", "e": "q_dead", "i": "q_dead", 
        "o": "q_dead", "u": "q_dead",
        "b": "q_dead", "p": "q_dead", "m": "q_dead", "n": "q_dead"
    }
}

def simular(cadeia: str) -> bool:
    estado_atual = q0
    for simbolo in cadeia:
        if simbolo not in Sigma:
            return False
        estado_atual = delta[estado_atual][simbolo]
        if estado_atual == "q_dead":
            return False
    return estado_atual in F
