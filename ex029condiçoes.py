km = int(input('Digite a velocidade em Km/h: '))
if km >= 80:
    print(f'A velocidade ultrapassou o limite, a multa é R${(km-80)*7},00')
