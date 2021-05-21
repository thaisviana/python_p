def calcula_ocorrencia(frase):
    ocorrencias = {}
    for letra in frase.lower():
        if letra.isalpha():
            if letra in ocorrencias:
                ocorrencias[letra] += 1
            else:
                ocorrencias[letra] = 1 
    print(ocorrencias)

calcula_ocorrencia("O rato roeu a roupa do rei de roma")