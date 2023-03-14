lista_full = []
lista_par = []
lista_impar = []
for i in range(0, 7):
    n = int(input(f'Digite o {i+1}° número: '))
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
lista_par.sort()
lista_impar.sort()
lista_full.append(lista_par[:])
lista_full.append(lista_impar[:])
print(f'Os valores pares digitados foram {lista_full[0]}')
print(f'Os valores impares digitados foram {lista_full[1]}')
