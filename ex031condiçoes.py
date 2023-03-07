dist = int(input('Digite a distância em Km da viagem: '))
if dist <= 200:
    print(f'O valor da viagem é R${dist*0.5:.2f}')
else:
    print(f'O valor da viagem é R${dist*0.45:.2f}')
