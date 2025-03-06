# importando o módulo 'os' para que ele interaja com o sistema operacional do computador
import os

# criando um a função para listar os diretórios dentro de um caminho
def listar_diretorios(caminho):
    # verificando se o caminho existe antes de tentar listar os arquivos
    if os.path.exists(caminho):
        print(f"\nListando arquivos em: {caminho}\n")  # mostrando o caminho completo antes de listar os itens da pasta
        # passando por cada item dentro do diretório (tanto arquivo, quanto pasta)
        for item in os.listdir(caminho):
            # imprime cada item encontrado no diretório especificado
            print(item)
    # se o caminho não existir
    else:
        # imprime uma mensagem de erro
        print("Erro: O caminho especificado não existe.")

# gerando uma variável que armazena automaticamente o diretório onde o script se encontra
caminho = os.getcwd()

# chamando a função para listar os diretórios do caminho atual
listar_diretorios(caminho)