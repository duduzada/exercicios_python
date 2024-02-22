'''Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.'''


times = ("Palmeiras", "Flamengo", "Internacional", "Grêmio", "São Paulo", "Atlético Mineiro", "Atlético Paranaense", "Cruzeiro", "Botafogo", "Santos", "Bahia", 
         "Fluminense", "Corinthians", "Chapecoense", "Ceará", "Vasco da Gama", "Sport Recife", "América Mineiro", "Vitória", "Paraná")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"Lista de times do Brasileirão: {times}")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"Os 5 primeiros são: {times[0:5]}")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"Os 4 últimos são: {times[-4:]}")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"Times em ordem alfabética: {sorted(times)}")
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print(f"O Chapecoense está na {times.index('Chapecoense') + 1}ª posição")