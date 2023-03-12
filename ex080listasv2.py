lista = []
for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0 or num >= lista[-1]:
        lista.append(num)
    else:
        x = 0
        while x < len(lista):
            if num <= lista[x]:
                lista.insert(x, num)
                break
            x += 1
print(f'Os valores digitados em ordem foram {lista}')
