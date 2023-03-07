cidade = input('Digite o nome de uma cidade: ')
n = cidade.strip().split()
if n[0].upper() == 'SANTO':
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')
