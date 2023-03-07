peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso/altura**2
if imc < 18.5:
    print(f'IMC = {imc:.2f}, abaixo do peso')
elif imc < 25:
    print(f'IMC = {imc:.2f}, peso ideal')
elif imc < 30:
    print(f'IMC = {imc:.2f}, soprepeso')
elif imc < 40:
    print(f'IMC = {imc:.2f}, obesidade')
else:
    print(f'IMC = {imc:.2f}, obesidade mórbida')
