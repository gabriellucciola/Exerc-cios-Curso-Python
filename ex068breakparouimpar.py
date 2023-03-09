import random

cont = 0
print('Vamos começar o jogo de PAR ou IMPAR')
while True:
    pc = random.randint(0, 100)
    player = int(input('Digite um número: '))
    pi = input('Par ou Impar? [P/I]: ').strip().upper()
    if pi == 'I' and (pc + player) % 2 != 0:
        print('-'*30)
        print(f'Você jogou {player} e o computador {pc}. Total de {player + pc} deu IMPAR ')
        print('-'*30)
        print('Você venceu')
        cont += 1
    elif pi == 'I' and (pc + player) % 2 == 0:
        print('-' * 30)
        print(f'Você jogou {player} e o computador {pc}. Total de {player + pc} deu PAR ')
        print('-' * 30)
        print('Você Perdeu')
        break
    elif pi == 'P' and (pc + player) % 2 == 0:
        print('-' * 30)
        print(f'Você jogou {player} e o computador {pc}. Total de {player + pc} deu PAR ')
        print('-' * 30)
        print('Você Venceu')
        cont += 1
    elif pi == 'P' and (pc + player) % 2 != 0:
        print('-' * 30)
        print(f'Você jogou {player} e o computador {pc}. Total de {player + pc} deu IMPAR ')
        print('-' * 30)
        print('Você Perdeu')
        break
print(f'Você venceu {cont} partidas em sequencia')
