'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''
print("==============================")
print("Analisador de Triângulos")
print("==============================")
a = float(input("Primeiro Segmento: "))
b = float(input("Segundo Segmento: "))
c = float(input("Terceiro Segmento: "))

if a + b > c and a + c > b and b + c > a and a == b and b == c and c == a:
    print("Os segmentos acima PODEM FORMAR um triângulo: EQUILATÉRO")
elif a + b > c and a + c > b and b + c > a and a == b or b == c == c or c == a:
    print("Os segmentos acima PODEM FORMAR um triângulo: ISÓSCELES")
elif a + b > c and a + c > b and b + c > a and a != b and b != c and c != a:
    print("Os segmentos acima PODEM FORMAR um triângulo: ESCALENO")
else:
    print("Os segmentos NÃO PODEM formar um triângulo")