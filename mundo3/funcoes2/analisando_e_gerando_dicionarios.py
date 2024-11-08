'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e 
vai retornar um dicionário com as seguintes informações:

Quantidade de notas
A maior nota
A menor nota
A média da turma
A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.'''

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita vários)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com vários informações sobre a situação da turma.
    """
    notas_alunos = dict()
    notas_alunos['Total'] = len(n)
    notas_alunos['Maior'] = max(n)
    notas_alunos['Menor'] = min(n)
    notas_alunos['Média'] = sum(n) / len(n)
    if sit == True:
        if notas_alunos['Média'] <= 4:
            notas_alunos['situação'] = 'Ruim'
        elif notas_alunos['Média'] <= 7:
            notas_alunos['situação'] = 'Razoável'
        else:
            notas_alunos['situação'] = 'Bom'
    return notas_alunos


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)



