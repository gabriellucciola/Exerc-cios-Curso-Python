preco = float(input('Digite o valor do produto: '))
n = int(input("""Escolha a forma de pagamento:
1 - A vista em dineheiro ou cheque
2 - A vista no cartão
3 - Dividido em até 2x no cartão
4 - Dividido em 3x ou mais no cartão\n"""))
if n == 1:
    print(f'O valor do produto com desconto será R${preco*0.9:.2f}')
elif n == 2:
    print(f'O valor do produto com desconto será R${preco*0.95:.2f}')
elif n == 3:
    print(f'O valor do produto será R${preco:.2f}')
elif n == 4:
    print(f'O valor do produto com juros será R${preco*1.2:.2f}')
else:
    print('Valor digitado é inválido, tente novamente!')
