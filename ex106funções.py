from time import sleep


def helppy(função):
    funcão_biblioteca = input(f'\033[m{função}').strip()
    if funcão_biblioteca == 'fim':
        sleep(0.5)
        print('\033[43;30m~'*21)
        print('Finalizado o programa')
        print('~'*21)
        return False
    sleep(1)
    print('\033[46;30m~'*(len(texto1)+len(funcão_biblioteca)))
    print(f'Acessando o manual da função {funcão_biblioteca}')
    print('~'*(len(texto1)+len(funcão_biblioteca)))
    sleep(1)
    print('\033[43;30m')
    help(funcão_biblioteca)
    sleep(0.5)
    return True


cont = True
texto = 'Sistema de ajuda PyHELP'
texto1 = 'Acessando o manual da função '
while cont:
    print(f'''\033[42;36m{'~'*len(texto)}
Sistema de ajuda PyHELP
{'~'*len(texto)}''')
    cont = helppy('Biblioteca ou função > ')


