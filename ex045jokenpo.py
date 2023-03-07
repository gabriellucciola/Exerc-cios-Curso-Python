import itertools
import random

print('Vamos começar a jogar jo ken po')
lista = ['pedra', 'papel', 'tesoura']
for i in itertools.count():
    n = str(input("""\nDeseja jogar: 
    1 - Sim
    2 - Não\n"""))
    if n == '1':
        pc = random.choice(lista)
        usuario = str(input("""Escolha sua opção:
        1 - Pedra
        2 - Papel
        3 - Tesoura\n"""))
        if usuario == '1' or usuario == '2' or usuario == '3':
            if pc == 'pedra' and usuario == '1' or pc == 'papel' and usuario == '2' or pc == 'tesoura' and usuario == '3':
                print(f'Minha escolha foi \033[33m{pc}')
                print('Empate\033[m')
            elif pc == 'tesoura' and usuario == '1' or pc == 'papel' and usuario == '3' or pc == 'pedra' and usuario == '2':
                print(f'Minha escolha foi \033[33m{pc}')
                print('Vitória do jogador\033[m')
            else:
                print(f'Minha escolha foi \033[33m{pc}')
                print('Vitória do computador\033[m')
        else:
            print('Opção inválida, inicie novamente')
    elif n == '2':
        print('Jogo encerrado.')
        break
    else:
        print('Opção Inválida, escolha novamente!')
