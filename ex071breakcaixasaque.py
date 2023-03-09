while True:
    n = input('Quanto deseja sacar? R$')
    if n.isdigit():
        n = int(n)
        notas_50 = int(n/50)
        if notas_50 > 0:
            print(f'{notas_50} notas de 50')
        notas_20 = int((n-(50 * notas_50)) / 20)
        if notas_20 > 0:
            print(f'{notas_20} notas de 20')
        notas_10 = int((n % 50) % 20 / 10)
        if notas_10 > 0:
            print(f'{notas_10} notas de 10')
        notas_1 = n % 50 % 20 % 10
        if notas_1 > 0:
            print(f'{notas_1} notas de 1')
        break
