import random

# Lista que vai conter as listas aleatórias
listas_aleatorias = []

# Quantidade de listas que você quer criar
quantidade_listas = 5

# Tamanho de cada lista
tamanho_lista = 6

# Loop para criar as listas aleatórias
for _ in range(quantidade_listas):
    lista_aleatoria = [random.randint(0, 60) for _ in range(tamanho_lista)]
    listas_aleatorias.append(lista_aleatoria)

# Mostra as listas aleatórias criadas
for i, lista in enumerate(listas_aleatorias):
    print(f"Lista {i + 1}: {lista}")
