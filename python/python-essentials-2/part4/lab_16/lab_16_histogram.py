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
        
        for c in sorted(histogram.keys()):
            print(f'{c}->{histogram[c]}')

    except FileNotFoundError as e: # CORREÇÃO 2: Garantir o 'as e'
        print('FileNotFoundError', e.args)
        # Se você tinha um "raise e" aqui, certifique-se de que o teste 
        # está esperando que essa exceção suba, ou remova o raise para
        # apenas imprimir o erro.
    except IOError as e:
        print('IOError', e.args)
    except BaseException as e:
        print('Error: ', e.args)
    finally:
        # CORREÇÃO 3: Agora stream existe de forma garantida.
        # Se open() falhou, ele é None (logo, avalia como Falso e não tenta fechar).
        if stream is not None: 
            stream.close()

if __name__ == '__main__':
    histogram()