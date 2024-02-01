'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos'''

op = ''
sexo = ''
cont = 0
while True:
    print("----------------------------------------")
    print("          CADASTRE UMA PESSOA ")
    print("----------------------------------------")
    
    idade = int(input("Idade: "))
    while sexo not in ['M','F']:
        sexo = str(input("Sexo: [M/F] ")).upper().strip()[0]
    while op not in ['S','N']:
        op = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
        if op == 'N':
            print()
            break
    if idade >= 18:
        cont+=1
print("acabou")
    

    
