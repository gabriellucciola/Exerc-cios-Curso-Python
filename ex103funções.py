def ficha(jogador, gols):
    if jogador == "" and gols != '0':
        print(f'O jogador <desconhecido> fez {gols} gol(s) no campeonato.')
    elif gols == 0 and jogador == "":
        print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')
    else:
        print(f'O jogador {jogador} fez {gols} gol(s) no campeonato.')


jog = input('Jogador: ')
gol = input('Gols: ')
if gol == "":
    gol = 0
ficha(jog, gol)
