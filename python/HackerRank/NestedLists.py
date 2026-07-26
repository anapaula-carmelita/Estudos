if __name__ == '__main__':
    records = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records[name] = score
    
    lista = list(records.values())
    m = min(lista)
    lista = [x for x in lista if x != m]
    m = min(lista)
    lista = []
    for key in records.keys():
        if records[key] == m:
            lista.append(key)
    lista.sort()
    for name in lista:
        print(name)
    
    
