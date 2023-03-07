print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Digite o número de termos que deseja ver da sequência de Fibonacci: '))
print('~'*71)
cont = 2
fibonacci = []
x = 0
fibonacci.append(x)
x = 1
fibonacci.append(x)
while cont < n:
    x = x + fibonacci[cont-1]
    fibonacci.append(x)
    cont += 1
print(fibonacci, 'FIM')
#teste