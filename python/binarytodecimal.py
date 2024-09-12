def toDecimal(binary):
    binary = binary[::-1]
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2**i
    return decimal

str = input("Digite o binário: ")
print (toDecimal(str))

    