import datetime

nasc = int(input('Digite o ano que você nasceu: '))
agora = datetime.datetime.now()
ano_atual = agora.year
if ano_atual - nasc < 18:
    print(f'Ainda restam {ano_atual - nasc} para o seu alistamento')
elif ano_atual - nasc == 18:
    print('Está na hora do alistamento')
else:
    print(f'Já passou o tempo do alistamento em {ano_atual - nasc - 18} ano(s)')
