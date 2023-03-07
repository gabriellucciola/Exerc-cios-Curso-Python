num = int(input('Digite um número maior que 0 para saber se é primo ou não: '))
c = 0
for i in range(1, num+1):
    if num % i == 0:
        c += 1
        if c > 2:
            print(f'O número {num} não é primo')
            break
        elif num == 0 or num == 1:
            print(f'O numero {num} não é classificado como primo nem composto')
if c == 2:
    print(f'O número {num} é primo')
