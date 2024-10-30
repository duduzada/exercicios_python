""" def contador(i, f, p):
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')


contador(0, 100, 10) """


""" def soma(a, b, c):
    s = a + b + c
    print(f"A soma vale {s}")

soma(3, 2, 5) """

""" def soma(a, b, c=0):
    s = a + b + c
    print(f"A soma vale {s}")

soma(8, 4)  """

""" def soma(a, b, c=0):
    s = a + b + c
    print(f"A soma vale {s}")

soma(8, 4)  """

""" 
def soma (a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

soma() """

""" def teste():
    x = 8
    print(f'Na função teste, n vale {2}')
    print(f'Na função teste, x vale {x}')

n = 2
print(f'No programa principal, n vale {n}')
teste()
print(f'No program principal, x vale {x}') """

""" def funcao():
    n1 = 4
    print(f'N1 dentro da função vale {n1}')

n1 = 2
funcao()
print(f'N1 global vale {n1}') """

""" def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}') """


def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'Os resultados foram: {r1}, {r2} e {r3}')

