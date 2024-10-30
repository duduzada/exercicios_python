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


def soma (a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

soma()




