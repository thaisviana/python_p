#Encontrar números primos é uma tarefa difícil. 
# Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado
#  pelo usuário.

print("Insira um número inteiro:")
numero = int(input())


def teste_de_primalidade(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

for i in range(2,numero):
    if teste_de_primalidade(i):
        print(i, " é primo")