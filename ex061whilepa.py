x = int(input('Digite o primeiro valor da PA: '))
y = int(input('Digite a razão da PA: '))
cont = 1
pa = []
pa.append(x)
while cont < 10:
    x += y
    pa.append(x)
    cont += 1
print(pa)
while cont != 0:
    pa_z = []
    cont = 1
    n = int(input('Deseja ver quantos mais? '))
    if n > 0:
        while cont <= n:
            z = x + y
            pa_z.append(z)
            cont += 1
            x = z
        print(pa_z)
    else:
        cont = 0
print('Aplicação finalizada.')
