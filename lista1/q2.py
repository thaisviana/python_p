# Faça um programa que mostre os n termos da Série a seguir:
#  	S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.

def show_terms(num):
    numerator = 1
    denominator = 1
    calc = 0
    
    while numerator <= num:
        print(f"{numerator} / {denominator}")
        numerator += 1
        denominator += 2
        calc += numerator / denominator        
    return calc

print(show_terms(20))