def linha(tam=42):
    return '-' * tam

def cabecalho():
    print(linha())
    print("MENU PRINCIPAL".center(42))
    print(linha())

def menu():
    print('''1 - Ver pessoas cadastradas
2 - Cadastrar nova Pessoa
3 - Sair do Sistema
 ''')
    
def sistema():
    op = 0
    while op != 3:
        cabecalho()
        menu()
        op = int(input("Qual é sua op: "))