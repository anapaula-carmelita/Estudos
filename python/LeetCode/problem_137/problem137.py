class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        vistos = set()
        repetidos = set()
        
        # Percorre a string pegando janelas de tamanho 10
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            
            if seq in vistos:
                repetidos.add(seq)
            else:
                vistos.add(seq)
                
        return list(repetidos)