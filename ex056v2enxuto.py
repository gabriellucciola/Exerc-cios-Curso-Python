idade_homem = 0
nome_homem = ''
cont_novinhas = 0
idade_media = 0
for i in range(1, 6):
    print('-'*10, f'  {i} Pessoa  ', '-'*10)
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).upper().strip()
    if idade_homem < idade:
        idade_homem = idade
        nome_homem = nome
    if sexo == 'F' and idade < 20:
        cont_novinhas += 1
    idade_media += idade
print(f"""A média das idades é {idade_media/5}
{cont_novinhas} das mulheres possuem menos de 20 anos
O homem mais velho é {nome_homem} com {idade_homem} anos""")