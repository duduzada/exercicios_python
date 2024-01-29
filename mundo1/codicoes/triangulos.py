# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("==============================")
print("Analisador de Triângulos")
print("==============================")
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))



if a + b > c and a + c > b and b + c > a:
    print("Os segmentos acima podem formar um triângulo!")
else:
    print("Os segmentos acima não podem formar um triângulo")