#pessoas = {"nome": "Gustavo", "sexo":"M", "idade": 22}

#print(pessoas["idade"])
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
#print(pessoas.keys())
#print(pessoas.values())
#print(pessoas.items())

#for k in pessoas.keys():
    #print(k)

#for v in pessoas.values():
    #print(v)


#del pessoas["sexo"] /// deletar sexo

#pessoas["nome"] = "Leandro" /// mudar valor "nome"

#pessoas["peso"] = 98.5 /// adicionar valor "peso" ao dicionário

#for k, v in pessoas.items():
   #print(f"{k} = {v}")

#//////////////////////////////////////////////////////////////////////////
# brasil = []
# estado = {"uf": "Rio de Janeiro", "sigla": "RJ"}
# estado2 = {"uf": "São Paulo", "sigla": "SP"}
# brasil.append(estado)
# brasil.append(estado2)

# print(brasil[0]["uf"])

#//////////////////////////////////////////////////////////////////////////

estado = dict()
brasil = list()
for c in range (0,3):
    estado["uf"] = str(input("Unidade Federativa: "))
    estado["sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy())
#print(brasil)
# for e in brasil:
#     print(e)

# for e in brasil:
#     for k,v in e.items():
#         print(f"O campo {k} tem valor {v}")

for e in brasil:
    for v in e.values():
        print(v, end = " ")
    print()
