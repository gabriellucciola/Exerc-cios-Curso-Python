continuar = 'S'
cont1 = cont2 = cont3 = 0
while continuar in 'S':
    idade = sexo = 0
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    while True:
        idade = input('Idade: ')
        if idade.isdigit():
            idade = int(idade)
            if idade > 18:
                cont1 += 1
            break
    while True:
        sexo = input("Sexo M/F: ").upper().strip()
        if sexo == 'M' or sexo == 'F':
            if sexo == 'M':
                cont2 += 1
            break
    if idade < 20 and sexo == 'F':
        cont3 += 1
    while True:
        continuar = input('Deseja fazer um novo cadastro? S/N:').upper().strip()
        if continuar == 'S' or continuar == 'N':
            break
print(f'''{cont1} pessoas tem mais de 18 anos
{cont2} homens foram cadastrados
{cont3} mulheres cadastradas possuem menos de 20 anos''')
