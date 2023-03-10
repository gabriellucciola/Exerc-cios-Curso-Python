colocacao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians',
             'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
             'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás',
             'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará SC', 'Atlético-GO',
             'Avai', 'Juventude')
print('-='*15)
print(f'Lista de times do Brasileirão: {colocacao}')
print('-='*15)
print('Os 5 primeiros são: ', end='')
for i in range(0, 5):
    if i < 4:
        print(colocacao[i], end=' -> ')
    elif i == 4:
        print(colocacao[i])
print('-='*15)
print('Os 4 últumos são: ', end='')
for i in range(-1, -5, -1):
    if i > -4:
        print(colocacao[i], end=' -> ')
    elif i == -4:
        print(colocacao[i])
print('-='*15)
print(f'Times em ordem alfabética: {sorted(colocacao)}')
print('-='*15)
print(f'Santos está na {colocacao.index("Santos")+1}ª colocação')
print('-='*15)
#end
