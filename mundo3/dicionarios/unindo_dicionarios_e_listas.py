'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

todos = []
pessoa = {}
while True:
    pessoa.clear()
    pessoa ['nome'] = str(input("Nome: "))
    while True:
        pessoa ['sexo'] = str(input("Sexo: [M/F] ")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("ERRO! Por favor, digite apenas M ou F.")
    pessoa['idade'] = int(input("Idade: "))
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Responda apenas S ou N. ")
    if resp == 'N':
        break

print("-=" *30)



