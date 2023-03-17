lista_geral = []
sub_lista = []
lista_nomes = []
lista_media = []
lista_notas = []
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1:').replace(',', '.'))
    nota2 = float(input('Nota 2: ').replace(',', '.'))
    media = (nota1 + nota2)/2
    lista_nomes.append(nome)
    lista_media.append(media)
    lista_notas.append(nota1)
    lista_notas.append(nota2)
    sub_lista.append(lista_nomes[:])
    sub_lista.append(lista_notas[:])
    sub_lista.append(lista_media[:])
    lista_geral.append(sub_lista[:])
    lista_notas.clear()
    lista_media.clear()
    lista_nomes.clear()
    sub_lista.clear()
    n = input('Deseja continuar? S/N: ').upper().strip()
    if n == 'N':
        break
print('_'*40)
print('N°', f'{"Nome":<15} MÉDIA')
print('-'*40)
for j in range(0, len(lista_geral)):
    print(j, f' {lista_geral[j][0][0]:<15}  {lista_geral[j][2][0]}')
print('-'*40)
while True:
    q = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if q == 999:
        break
    else:
        print(f'Notas de {lista_geral[q][0][0]} são {lista_geral[q][1]}')
print('-'*40)
