#
#  Nome do arquivo: mysplit.py
#  Descrição: Programa de uma possível solução do LAB 'You own split' do livro Python Essentials 2
#  Autor: Ana Paula da Silva Souza
#  Data: 17/07/2026
#  Versão: 1.0
#  Licença: Apache
#

def mysplit(strng):
    strng = strng.strip()
    lista = [] 
    
    if strng == '':
        return lista

    s =''
    for c in strng:
        if c == ' ':
            lista.append(s)
            s = ''
            continue
        s += c
    if s != ''
        lista.append(s)
    return lista

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit(" "))
print(mysplit(" abc "))
print(mysplit(""))
