# TABUADA
def calcularTabuada(valorTabuada, valorInicial, valorFinal):
    for i in range(valorInicial, valorFinal + 1):    
        print(f"{valorTabuada} x {i} = {valorTabuada * i}")

calcularTabuada(15, 1, 7)