#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

valores = []
v = 0
for cont in range(0, 5):
    valores.append(int(input(f"Digite um valor para a posição {v}: ", )))
    v += 1
print(f"Você digitou os valores {valores}")
print(f"O maior valor digitado foi {max(valores)} nas posições {valores.index(max(valores))}...")
print(f"O menor valor digitado foi {min(valores)} nas posições {valores.index(min(valores))}...")
