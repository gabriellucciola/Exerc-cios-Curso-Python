cont = 0
soma = 0
n = 's'
lista = []
while n in 'Ss':
    num = int(input('Digite um valor: '))
    lista.append(num)
    soma += num
    cont += 1
    n = input('Deseja continuar? S/N: ')
lista.sort()
print(f'''A média dos números digitados é {soma/cont}
O maior valor digitado foi {lista[-1]}
O menor valor digitado foi {lista[0]}''')
