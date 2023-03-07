x = 4
while x != 5:
    while x == 4:
        y = int(input('1º valor: '))
        z = int(input('2° valor: '))
        x = int(input('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa\n'''))
        if x == 1:
            r = y + z
            print(f'Resposta {r}')
            x = 4
        elif x == 2:
            r = y * z
            print(f'Resposta {r}')
            x = 4
        elif x == 3:
            if y > z:
                print(f'{y} é o maior')
            else:
                print(f'{z} é o maior')
            x = 4
        elif x == 5:
            break
print('Aplicação encerrada.')
