from moedas import moedas

num = float(input('Digite o preço: R$'))
print(f'O dobro de {moedas.moeda(num, True)} é {moedas.dobro(num, True)}')
print(f'A metade de {moedas.moeda(num, True)} é {moedas.metade(num, True)}')
print(f'Aumentando 10% temos {moedas.aumentar(num, 10, True)}')
print(f'Diminuindo 13% temos {moedas.diminuir(num, 13, True)}')
