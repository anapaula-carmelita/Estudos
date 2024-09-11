def toBinary(num):
    binary = 0
    lista = []
    while (num > 0):
        binary = num % 2
        num = num // 2
    print(lista)

    for d in lista:
        print(d, end="")
    print()


n = int(input('Digite um número'))
toBinary(n)