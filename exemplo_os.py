import os
from datetime import datetime
# nome_arquivo = 'arq_texto.txt'
# caminho_absoluto = os.path.abspath(nome_arquivo)

# caminho_radical, caminho_final = os.path.split(caminho_absoluto)

# lista_de_diretorios = []
# while caminho_final:
#     lista_de_diretorios.append(caminho_final)
#     caminho_radical, caminho_final = os.path.split(caminho_radical)
# lista_de_diretorios.append(caminho_radical)
# lista_de_diretorios.reverse()
# print(lista_de_diretorios)

# print(os.path.join(*lista_de_diretorios))

informacoes_do_arquivo = os.stat('arq_texto.txt')
print(datetime.fromtimestamp(informacoes_do_arquivo.st_atime))

