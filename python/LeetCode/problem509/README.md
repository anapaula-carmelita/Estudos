# 509. Fibonacci Number — Solução & Análise Detalhada da Gemini

Documentação e análise da solução para o problema **509. Fibonacci Number** do LeetCode.

---

## 📌 Descrição do Problema

Os números de Fibonacci formam uma sequência onde cada número é a soma dos dois precedentes, começando por `0` e `1`.

- **F(0)** = 0
- **F(1)** = 1
- **F(n)** = F(n - 1) + F(n - 2), para `n > 1`

Dado um número inteiro `n`, retorne o valor de **F(n)**.

### Exemplos

* **Exemplo 1:**
  * **Input:** `n = 2`
  * **Output:** `1`
  * **Explicação:** `F(2) = F(1) + F(0) = 1 + 0 = 1.`

* **Exemplo 2:**
  * **Input:** `n = 3`
  * **Output:** `2`
  * **Explicação:** `F(3) = F(2) + F(1) = 1 + 1 = 2.`

* **Exemplo 3:**
  * **Input:** `n = 4`
  * **Output:** `3`
  * **Explicação:** `F(4) = F(3) + F(2) = 2 + 1 = 3.`

---

## 💻 Abordagem Original (Programação Dinâmica com Lista)

### Código Original
```python
class Solution:
    def fib(self, n: int) -> int:
        if n > 0:
            lista = [0 for x in range(n + 1)]
            lista[1] = 1
            for i in range(2, n + 1):
                lista[i] = lista[i - 1] + lista[i - 2] 
            return lista[n]
        else:
            return 0
```

### Análise do Código Original
* **Pontos Fortes:**
  * Utiliza Programação Dinâmica *bottom-up* com tabulação.
  * Evita a recursão ingênua $O(2^N)$.
* **Oportunidades de Otimização:**
  * Aloca uma lista inteira de tamanho $N+1$, consumindo memória proporcional a $N$.
  * A sintaxe `[0 for x in range(n + 1)]` pode ser simplificada para `[0] * (n + 1)`.

---

## 🚀 Solução Otimizada (Espaço Constante $O(1)$)

Como para calcular o próximo termo de Fibonacci dependemos apenas dos **dois últimos valores**, não precisamos manter todo o histórico em uma lista. Podemos usar apenas duas variáveis.

### Código Otimizado
```python
class Solution:
    def fib(self, n: int) -> int:
        # Casos base: F(0) = 0 e F(1) = 1
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b  # Atualiza os dois últimos termos em tempo constante
            
        return b
```

---

## 📊 Comparativo de Complexidade

| Métrica | Código Original | Código Otimizado |
| :--- | :--- | :--- |
| **Complexidade de Tempo (Time Complexity)** | $\mathcal{O}(N)$ | $\mathcal{O}(N)$ |
| **Complexidade de Espaço (Space Complexity)** | $\mathcal{O}(N)$ | **$\mathcal{O}(1)$** |
| **Estrutura de Dados** | `list` de tamanho $N+1$ | Duas variáveis escalares (`a` e `b`) |

---

## 🔑 Principais Aprendizados
1. **Otimização de Espaço:** Quando um algoritmo de Programação Dinâmica só depende dos últimos $k$ estados, é possível reduzir a complexidade de espaço de $O(N)$ para $O(1)$.
2. **Atribuição Múltipla em Python:** A sintaxe `a, b = b, a + b` permite trocar e atualizar variáveis de forma atômica e elegante sem necessidade de uma variável auxiliar temporária.