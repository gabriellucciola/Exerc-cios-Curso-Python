lista_cadastro = []
soma = cont = 0
while True:
    dicionario_pessoas = {'nome': input('Nome: ').strip().capitalize(),
                          'sexo': input('Sexo: ').strip().capitalize(),
                          'idade': int(input('Idade: ').strip().capitalize())}
    lista_cadastro.append(dicionario_pessoas)
    repeat = input('Deseja continuar? [S/N]: ')
    cont += 1
    soma += dicionario_pessoas['idade']
    if repeat in 'Nn':
        break
print('-='*30)
print(f'''- O grupo tem {cont} pessoas
- A média de idade do grupo é {soma/cont}
- As mulheres cadastradas foram: ''', end='')
pessoas = []
for item in lista_cadastro:
    if item['sexo'] in 'Ff':
        print(item['nome'], end='; ')
    if item['idade'] > soma/cont:
        pessoas.append(item['nome'])
print('')
print(f'- Lista de pessoas que estão acima da média: {pessoas}')