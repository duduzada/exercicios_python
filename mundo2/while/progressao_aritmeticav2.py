#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('''Gerador de PA
-=--=--=--=--=--=--=-''')
pt = int(input("Primeiro termo: "))
rz = int(input("Razão da PA: "))
decimo = 0
while decimo < 10:
    print(f"{pt} ->", end = ' ')
    decimo += 1
    pt += rz
print("FIM", end=' ')

