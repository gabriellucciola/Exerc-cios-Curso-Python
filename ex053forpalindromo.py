frase = str(input('Digite uma frase: ')).upper().strip().replace(' ', '')
inverso = ''
for letra in range(len(frase)-1, -1, -1):
    inverso += frase[letra]
if frase == inverso:
    print(f'A frase {frase} e o inverso {inverso}\nÉ um políndromo')
else:
    print(f'A frase {frase} e o inverso {inverso}\nNão é um políndromo')