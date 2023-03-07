import datetime

agora = datetime.datetime.now()
agora_ano = agora.year
maior = 0
menor = 0
for i in range(0, 7):
    n = int(input('Digite o ano de nascimento: '))
    if agora_ano - n < 21:
        menor += 1
    else:
        maior += 1
print(f'{maior} das 7 pessoas são de maior')
print(f'{menor} das pessoas são de menor')
