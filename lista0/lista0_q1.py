#Faça um programa que peça 3 números inteiros, 
# calcule e mostre a quantidade de números pares 
# e a quantidade de números impares.

pares =0

for i in range(10):
    n = int(input("numero : "))
    pares += 1 if n % 2 == 0  else 0
print(pares, "pares e", 10 - pares, "impares")
