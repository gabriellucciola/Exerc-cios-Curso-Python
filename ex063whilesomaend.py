cont = 0
num = 0
soma = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        cont += 1
        soma += num
print(f'Foram digitados {cont} valores e a soma deles é igual a {soma}')
