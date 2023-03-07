x = int(input('Digite o primeiro número da PA: '))
y = int(input('Digite a razão da PA: '))
print('Os 10 primeiros números da PA são:')
pa = []
for i in range(0, 10):
    pa.append(x)
    x += y
print(pa)