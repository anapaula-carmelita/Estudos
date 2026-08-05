def histogram():
    stream = None
    try:
        filename = input('Enter the filename: ')
        histogram = {}
        stream = open(filename, "rt", encoding = "utf-8")
        
        c = stream.read(1)

        while(c != ''):
            
            letra = c.lower()
            if letra.isalpha():
                # Pega o valor atual (ou 0 se não existir) e soma 1
                histogram[letra] = histogram.get(letra, 0) + 1
            
            c = stream.read(1)
        
        ordened_list = sorted(histogram.items(), key=lambda x: x[1], reverse=True)

        stream.close()

        stream = open(filename+'.hist', "w", encoding = "utf-8")
        for c in ordened_list:
            stream.write(f'{c[0]}->{c[1]}\n')

    except FileNotFoundError as e: 
        print('FileNotFoundError', e.args)
        
    except IOError as e:
        print('IOError', e.args)
    except BaseException as e:
        print('Error: ', e.args)
    finally:
        # Se open() falhou, ele é None (logo, avalia como Falso e não tenta fechar).
        if stream is not None: 
            stream.close()

if __name__ == '__main__':
    histogram()