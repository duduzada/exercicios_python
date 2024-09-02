#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
cont = 0
jogador["nome"] = str(input("Nome do jogador: "))
jogador["gols"] = []


jogos = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for i in range(0, jogos):
   gols = int(input(f"Quantos gols na partida {i+1}? "))
   cont += gols
   jogador["gols"].append(gols)

jogador["total"] = cont
print("-=" * 30)
print(jogador)
print("-=" * 30)
for k, v in jogador.items():
   print(f"O campo {k} tem o valor {v}")
print("-=" * 30)
print(f"O jogador {jogador['nome']} jogou {jogos} jogos.")
for j in range (0, jogos):
   print(f"Na partida {j+1}, fez {jogador['gols'][j]} gols.")
   