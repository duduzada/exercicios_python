#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos e que são IMPARES de três e que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for i in range(3, 501, 2):
    if i % 3 == 0:
        s += i
        cont += 1
print(f"O somatório de todos os {cont} valores solicitados é {s}")
    