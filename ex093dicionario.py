dados = {}
lista = []
soma = 0
dados['nome'] = input('Nome do jogador: ').strip()
num_partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, num_partidas):
    gols = int(input(f'Quantos gols na partida {c}? '))
    soma += gols
    lista.append(gols)
print('-='*30)
dados['gols'] = lista
dados['total'] = soma
print(dados)
print('-='*30)
for item in dados:
    print(f'O campo {item} tem o valor {dados[item]}')
print('-='*30)
for c, item in enumerate(dados['gols']):
    print(  f'  => Na partida {c}, fez {item} gols.')
print(f'Foi um total de {soma} gols.')