dados = {}
dados['nome'] = input('Nome: ')
dados['media'] = float(input('Média: '))
if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado'
else: dados['situacao'] = 'Reprovado'
for k, i in dados.items():
    print(f'{k.capitalize()} é igual a {i}')