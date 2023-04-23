from time import sleep


def contador(a, b, c):
    lista_num = list(range(a, b))
    print('-='*20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b and c > 0:
        for c in range(a, b+1, c):
            sleep(0.5)
            print(f'{c} ', end='')
    elif a > b and c > 0:
        for c in range(a, b-1, c*-1):
            sleep(0.5)
            print(f'{c} ', end='')
    elif a < b and c < 0:
        for c in range(a, b+1, c*-1):
            sleep(0.5)
            print(f'{c} ', end='')
    elif a > b and c < 0:
        for c in range(a, b-1, c):
            sleep(0.5)
            print(f'{c} ', end='')
    elif a > b and c == 0:
        for c in range(a, b-1, -1):
            sleep(0.5)
            print(f'{c} ', end='')
    elif a < b and c == 0:
        for c in range(a, b+1, 1):
            sleep(0.5)
            print(f'{c} ', end='')


contador(1, 10, 3)
print('')
contador(20, 10, 3)
print('')
print('Agora é sua vez de personalizar a contagem')
contador(a=int(input("Inicio: ")), b=int(input('Fim: ')), c=int(input('Passo: ')))


