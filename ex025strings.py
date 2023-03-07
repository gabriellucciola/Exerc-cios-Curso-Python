frase = input('Digite uma frase: ')
f = frase.upper().count('A')
print(f'A letra "a" aparece {f} vezes')
for i in range(0, len(frase.strip())):
    if frase[i].upper() == 'A':
        print(f'A primeira letra "a" aparece na posição {i+1}')
        i == len(frase.strip())-1
        break
for i in range(len(frase.strip())-1, 0, -1):
    if frase[i].upper() == 'A':
        print(f'A ultima letra "a" aparece na posição {i+1}')
        break
