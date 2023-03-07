nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota2 + nota1)/2
if media < 5:
    print(f'Reprovado com nota {media:.2f}')
elif media >= 5 and media < 7:
    print(f'Recuperação com nota {media}')
else:
    print(f'Aprovado com média {media}')
