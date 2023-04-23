from random import randint
from time import sleep

print('Valores sorteados')
jogadores = {}
lista_completa = []
sleep(1)
for i in range(0, 4):
    jogadores['jogador'] = f'Jogador {i+1}'
    jogadores['valor'] = randint(1, 6)
    print(f'{jogadores["jogador"]} igual a {jogadores["valor"]}')
    lista_completa.append(jogadores.copy())
    jogadores.clear()
    sleep(1)
lista_completa_ordenada = sorted(lista_completa, key=lambda x: x['valor'], reverse=True)
for c, item_in_lista in enumerate(lista_completa_ordenada):
    print(f'{c+1}° lugar: {item_in_lista["jogador"]} com {item_in_lista["valor"]}')
    