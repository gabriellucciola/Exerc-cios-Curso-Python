idade_media = 0
nomes = ''
sexos = ''
novinhas = ''
homem_velho = ''
idade_homem = 0
for i in range(0, 5):
    nome = str(input('Digite o nome: ')).strip().capitalize()
    nomes += nome
    nome_copia = nome
    nome_copia1 = nome
    nome = ' '
    nomes += nome
    idade = int(input('Digite a idade: '))
    idade_media += idade
    sexo = str(input('Digite M para masculino e F para feminino: ')).strip().upper()
    sexos += sexo
    if sexo == 'F' and idade < 20:
        novinhas += nome_copia
        if i < 4:
            nome_copia = '; '
            novinhas += nome_copia
    if sexo == 'M' and idade>idade_homem:
        idade_homem = idade
        homem_velho = nome_copia1
print(f"""A idade média das pessoas é {idade_media/5}
As mulheres que possuem menos de 20 anos são: {novinhas} 
O nome do homem mais velho é {homem_velho}""")
