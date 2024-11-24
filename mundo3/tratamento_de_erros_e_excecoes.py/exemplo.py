""" try:    #operação
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except Exception as erro:   # se falhou e exibe o erro
    print(f"Problema encotrado foi {erro.__class__}")
else:   #deu certo
    print(f"O resultado é {r:.1f}")
finally:    #independente se falhou ou deu certo
    print("Volte sempre! Muito obrigado!") """



try:    #operação
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou. ")
except ZeroDivisionError:
    print("Não foi possível dividir um um número por zero! ")
except KeyboardInterrupt:
    print("O usuário prefiriu não informar os dados! ")
except Exception as erro:
    print(f"O erro encontrado foi {erro.__cause__}")
else:   #deu certo
    print(f"O resultado é {r:.1f}")
finally:    #independente se falhou ou deu certo
    print("\nVolte sempre! Muito obrigado!")
