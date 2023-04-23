from datetime import datetime


def voto(year):
    if year < 18:
        return "VOTO NÃO É OBRIGATÓRIO"
    elif 18 <= year <= 65:
        return "VOTO É OBRIGATÓRIO"
    else:
        return "VOTO É OPCIONAL"


agora = datetime.now()
agora_ano = agora.year
nascimento = int(input('Em que ano você nasceu? '))
idade = agora_ano - nascimento
print(f'Com {idade} anos: {voto(idade)}')
