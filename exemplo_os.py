import os

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

lista = ['/', 'Users', 'thaisviana', 'Documents', 'infnet', 'python_p', 'arq_texto.txt']
print(lista)
print(*lista)
# print(os.path.join(*lista))

