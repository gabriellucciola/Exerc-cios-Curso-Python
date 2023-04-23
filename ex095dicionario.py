lista_jogadores = []
gols = []
while True:
    jogadores_indiv = {'nome': input('Nome: ').strip().capitalize()}
    jogadores_indiv['partidas'] = int(input(f"Quantas partidas {jogadores_indiv['nome']} jogou? "))
    soma = 0
    for c in range (0, jogadores_indiv['partidas']):
        gol = int(input(f'Quantos gols no jogo {c}? '))
        gols.append(gol)
        soma += gol
    jogadores_indiv['gols'] = gols[:]
    jogadores_indiv['total_gols'] = soma
    gols.clear()
    lista_jogadores.append(jogadores_indiv)
    cond = input('Deseja continuar? [S/N]: ').upper()
    print('-='*30)
    if cond == 'N':
        break
print(f"Cód {'Nome':<15} {'Gols':<10} {'Total'}")
for c, jogador in enumerate(lista_jogadores):
    print(f"{c:<3} {jogador['nome']:<15} {jogador['gols']!r:<10} {jogador['total_gols']}")
print('-='*30)
while True:
    n = int(input('Deseja ver os dados de qual jogador? [999 encerra]: '))
    if n == 999:
        break
    print(f"-- Levantamento do jogador {lista_jogadores[n]['nome']}")
    for c, x in enumerate(lista_jogadores[n]['gols']):
        print(f"No jogo {c} fez {x}")
