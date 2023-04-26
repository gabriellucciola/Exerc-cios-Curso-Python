from moedas import moedas

num = float(input('Digite o preço: R$'))
print(f'O dobro de {moedas.moeda(num)} é {moedas.dobro(num)}')
print(f'A metade de {moedas.moeda(num)} é {moedas.metade(num)}')
print(f'Aumentando 10% temos {moedas.aumentar(num, 10)}')
print(f'Diminuindo 13% temos {moedas.diminuir(num, 13)}')