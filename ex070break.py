barato_valor = soma = cont = 0
barato_nome = ''
while True:
    produto = input('Produto: ')
    valor = True
    while valor == True:
        valor = input('Valor: ')
        if valor.replace('.', '', 1).isnumeric():
            valor = float(valor)
            soma += valor
            if valor > 1000:
                cont += 1
            if barato_valor == 0:
                barato_valor = valor
                barato_nome = produto
            elif valor < barato_valor:
                barato_valor = valor
                barato_nome = produto
        else:
            valor = True
    n = 'S'
    while n != 'N' or n != 'S':
        n = input('Deseja cadastrar um novo produto? S/N: ').strip().upper()
        if n == 'N' or n == 'S':
            break
    if n == 'N':
        break
print(f'''O total da compra é R${soma:.2f}
Produtos custam mais de R$1000.00: {cont} 
O produto mais barato foi {barato_nome} e custa R${barato_valor:.2f} ''')
