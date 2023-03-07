import datetime

nasc = int(input('Digite o ano do seu nascimento: '))
agora = datetime.datetime.now()
ano_agora = agora.year
idade = ano_agora - nasc
if idade <= 9:
    print('Categoria MIRIM')
elif idade <= 14:
    print('Categoria INFANTIL')
elif idade <= 19:
    print('Categoria JUNIOR')
else:
    print('Categoria SÊNIOR')
