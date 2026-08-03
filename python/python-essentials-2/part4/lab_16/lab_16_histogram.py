try:
    filename = input('Enter the filename: ')
    histogram = {}
    stream = open(filename, "rt", encoding = "utf-8")
    
    c = stream.read(1)

    while(c != ''):
        
        letra = c.lower()
        # Pega o valor atual (ou 0 se não existir) e soma 1
        histogram[letra] = histogram.get(letra, 0) + 1
        
        c = stream.read(1)
    
    for c in sorted(histogram.keys()):
        print(f'{c}->' + str(histogram[c]))

except IOError as e:
    print('IOError', e.args())
except FileNotFoundError as e:
    print('FileNotFoundError', e.args())
except BaseException as e:
    print('Error: ', e.args())
finally:
    stream.close()