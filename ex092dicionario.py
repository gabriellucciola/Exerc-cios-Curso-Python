from datetime import datetime

dados = {}
dados["nome"] = input('Nome: ')
dados["ano"] = int(input('Ano de nascimento: '))
dados["ctps"] = int(input('Carteira de trabalho (0 não tem)'))
if dados['ctps'] != 0:
    agora = datetime.now()
    ano_atual = agora.year
    dados["idade"] = ano_atual-dados["ano"]
    dados["contratação"] = int(input('Ano de contratação: '))
    dados["salário"] = int(input('Salário: '))
    dados['aposentadoria'] = dados['contratação'] - dados['ano'] + 35
    print(dados)
    for item in dados:
        print(f'{item} tem valor {dados[item]}')
else:
    print(dados)
    for item in dados:
        print(f'{item} tem valor {dados[item]}')
