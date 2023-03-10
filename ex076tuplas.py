produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
            'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
n = len(produtos)
for i in range(0, n, 2):
    x = len(produtos[i])
    print(produtos[i], '.'*(30-x), f'R${produtos[i+1]:.2f}')
print('-'*40)
