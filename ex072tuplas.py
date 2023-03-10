tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quize', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = input('Digite um número de 0 a 20: ')
while True:
    if n.isnumeric() == True:
        n = int(n)
        if n <= 20 and n >= 0:
            break
    n = input('Tente novamente! Digite um número de 0 a 20: ')
print(f'O numero que você digitou foi {tupla[n]}')
