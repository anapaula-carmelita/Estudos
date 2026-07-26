class Solution:
    def fib(self, n: int) -> int:
        if n > 0:
            lista = [0 for x in range(n + 1)]
            lista[1] = 1
            for i in range(2, n + 1):
                lista[i] = lista[i - 1] + lista[i - 2] 
            return lista[n]
        else: return 0

        