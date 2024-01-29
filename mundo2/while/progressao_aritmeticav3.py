#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('''Gerador de PA
-=--=--=--=--=--=--=-''')
pt = int(input("Primeiro termo: "))
rz = int(input("Razão da PA: "))
decimo = 0
cond = False
cont = 0
while cond == False:
    print(f"{pt} ->", end = ' ')
    decimo += 1
    pt += rz
    cont += 1
    if decimo == 10:
            print("PAUSA", end = ' ')
            decimo = 0
            decimo = int(input("\nQuantos termos você quer mostrar a mais? "))
            if decimo == 0:
                  cond = True
            decimo = 10 - decimo
print(f"Progressão finalizada com {cont} termos mostrados")
print("FIM", end=' ')
