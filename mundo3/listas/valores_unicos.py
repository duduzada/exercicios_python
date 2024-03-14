'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''

lista = []
while True:
    c = ''
    v = int((input("Digite um valor: ")))
    
    if v in lista:
        print("Valor duplicado, não vou adicionar")
    else:
        lista.append(v)
        print("Valor adicionado com sucesso...")
    while c not in ['S','N']:
        c = str(input("Quer continuar? [S/N]")).upper().strip()[0]
    if c == ('N'):
        break

print(f"Você digitou os valores {lista}")

