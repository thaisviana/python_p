import os

def busca_arquivo(arquivo_nome, caminho_diretorio, lista_resultado):
    for item in os.listdir(caminho_diretorio):
        if os.path.isfile(os.path.join(caminho_diretorio,item)):
            if item == arquivo_nome:
                lista_resultado.append(caminho_diretorio)
                return lista_resultado
        elif os.path.isdir(os.path.join(caminho_diretorio,item)):
            busca_arquivo(arquivo_nome, os.path.join(caminho_diretorio,item), lista_resultado)
    return lista_resultado

caminho_diretorio = '/Users/thaisviana/Documents/infnet/python_p'
arquivo_nome = 'arq_texto.txt'
print(busca_arquivo(arquivo_nome, caminho_diretorio, []))