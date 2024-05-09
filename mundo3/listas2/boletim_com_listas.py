'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''
lista = []

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = str(input("Quer continuar? [S/N]"))
    if resp in "Nn":
        break
print('===========================================')
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('===========================================')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('===========================================')
    op = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if op == 999:
        print('FINALIZANDO...')
        break
    if op <= len(lista) - 1:
        print(f'Notas de {lista[op][0]} são {lista[op][1]}')