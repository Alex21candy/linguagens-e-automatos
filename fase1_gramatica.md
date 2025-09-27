# Fase 1 – Definição da Linguagem

## 1. Alfabeto (Σ)
O alfabeto contém apenas consoantes, com pelo menos 3 símbolos distintos:  

Σ = {b, c, d}

## 2. Variáveis (V)
Conjunto de símbolos não terminais:  

V = {S, A, B, C}

## 3. Símbolo Inicial
S

## 4. Produções (P)
As regras de produção da gramática são:  

1. S → bA  
2. A → cB  
3. B → dC  
4. C → bA | ε  
5. A → bA | cB  
6. B → dB | ε  

## 5. Definição da Gramática
A gramática pode ser formalizada como:  

G = (V, Σ, P, S)

## 6. Descrição da Linguagem
Essa linguagem gera cadeias **formadas apenas pelas consoantes b, c e d**, que:  
- sempre começam com a letra **b**  
- possuem obrigatoriamente pelo menos uma ocorrência da letra **c** e uma da letra **d**  
- depois disso, podem repetir sequências de `b`, `c` e `d` livremente.  

Ou seja, é o conjunto de cadeias de {b, c, d} que têm a estrutura mínima **"bcd"**, podendo se repetir ou expandir.

## 7. Exemplos de Cadeias

### Cadeias que pertencem à linguagem
- bcd  
- bcdb  
- bcdcb  
- bcddb  
- bcdc  
- bcdbcd  
- bcdbbcd  

### Cadeias que não pertencem
- bd        (falta o `c`)  
- bc        (falta o `d`)  
- cdb       (não começa com `b`)  
