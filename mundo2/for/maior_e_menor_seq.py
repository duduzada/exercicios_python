#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
n2 = 2000
n1 = 0
maior = 0
menor = 0
for i in range(1,6):
    p = float(input(f"Peso da {i}ª pessoa: "))
    if p > n1:
        maior = p
        n1 = p 
    if p < n2:
        menor = p
        n2 = p
print(f"O maior peso lido foi {maior}Kg")
print(f"o menor peso lido foi {menor}Kg")


   
     
