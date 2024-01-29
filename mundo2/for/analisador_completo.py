'''Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
soma = 0
n = 0
maior = 0
menor = 0
cont = 0
for p in range(1,5):
    print(f"--------- {p}ª PESSOA ---------")
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: "))
    soma += idade #para somar todas as idades e fazer uma média
    if sexo in "Mm":
        if p == 1:
            maior = idade
            nome_atual = nome
        else:
            if idade > maior:
                maior = idade
                nome_atual = nome
    if sexo in "Ff":
        if idade < 20:
            cont += 1
print(f"A média de idade do grupo é de {soma/4} anos")
print(f"O homem mais velho tem {maior} e se chama {nome_atual}")
if cont >= 1:
    print(f"Ao todo são {cont} mulheres com menos de 20 anos")
else:
    print("Nenhuma mulher foi inserida no analisador")


