import os

def finddir(path, dir_name):
    try:
        # Pega todos os arquivos e pastas do caminho passado
        for entry in os.listdir(path):
            # Cria um caminho seguro unindo o caminho atual com o nome da entrada
            current_path = os.path.join(path, entry)
            
            # Precisamos verificar se a entrada é de fato uma PASTA (diretório)
            if os.path.isdir(current_path):
                
                # Se for a pasta que estamos procurando, mostramos o caminho absoluto
                if entry == dir_name:
                    print(os.path.abspath(current_path))
                
                # Chamada recursiva para explorar os subdiretórios!
                finddir(current_path, dir_name)
                
    except PermissionError:
        # Pode ocorrer ao tentar ler pastas do sistema bloqueadas; ignoramos e seguimos.
        pass
    except BaseException as e:
        print("Erro:", e.args())

if __name__ == '__main__':
    finddir('/workspaces/Estudos/python/', 'lab_12')
