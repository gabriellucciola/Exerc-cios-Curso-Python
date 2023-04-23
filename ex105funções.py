def notas(*nota, sit=False):
    """Programa para analisar a nota e a situação de vários alunos
    :param nota: uma ou mais notas de alunos (aceita várias)
    :param sit: valor opcional, mostra a situação da média das notas
    :return: dicionário com várias informações referentes as notas informadas"""
    soma_notas = 0
    for valor in nota:
        soma_notas += valor
    media = soma_notas/len(nota)
    if media < 5:
        situação = 'RUIM'
    elif 5 <= media < 7:
        situação = 'RAZOÁVEL'
    else:
        situação = 'BOA'
    notas_dict = {'total': len(nota), 'maior': max(nota), 'menor': min(nota), 'média': media, 'situação': situação}
    if sit == False:
        del notas_dict['situação']
        return notas_dict
    else:
        return notas_dict


resp = notas(9.5, 6.3, 7.8, 2.5, sit=True)
print(resp)
help(notas)
