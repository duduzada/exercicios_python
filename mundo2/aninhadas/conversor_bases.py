#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um número inteiro: "))

print("Escolha uma das bases para conversão: ")
print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")

opcao = int(input("Sua opção: "))
if opcao == 1:
    num = bin(num)
    print(num[2::])
elif opcao == 2:
    num = oct(num)
    print(num[2::])
elif opcao == 3:
    num = hex(num)
    print(num[2::])
else:
    print("Por favor digite um número válido!")
