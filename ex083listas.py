exp = input('Digite a expressão: ').strip().replace(' ', '')
print(exp)
cont1 = cont2 = k = 0
for x, c in enumerate(exp):
    if c == '(':
        cont1 += 1
    elif c == ')':
        cont2 += 1
    if (exp[x-1] in '+-*/^.' and exp[x] == ')' or exp[0] in ')/^' or exp[len(exp)-1] in '(/^'
        or (exp[x] == ')' and exp[x-1] == '(')):
        print('A expressão está inválida')
        k = 1
        break
if cont1 == cont2 and k != 1:
     print('A expressão é válida')
