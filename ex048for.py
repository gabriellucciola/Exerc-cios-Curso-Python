soma = 0
cont = 0
for i in range(1, 500):
    if i % 2 != 0 and i % 3 == 0:
        soma += i
        cont += 1
print(f'soma = {soma}')
print(f'Quantidade de números somados: {cont}')
