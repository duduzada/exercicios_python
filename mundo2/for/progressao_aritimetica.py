'''Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
No final, mostre os 10 primeiros termos dessa progressão.'''
print("========================")
print("10 TERMOS DE UMA PA")
print("========================")
pt = int(input("Primeiro termo: "))
rz = int(input("Razão: "))
decimo = pt + (10 - 1) * rz
for i in range(pt, decimo + rz, rz):
    print(f"{i} ->" ,end=' ')
print("ACABOU")
