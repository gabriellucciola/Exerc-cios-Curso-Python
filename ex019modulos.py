import random
x = str(input('Digite o nome do primeiro aluno: '))
y = str(input('Digite o nome do segundo aluno: '))
z = str(input('Digite o nome do terceiro aluno: '))
w = str(input('Digite o nome do quarto aluno: '))
name_list = [x, y, z, w]
random.shuffle(name_list)
print(f'A lista do sorteio para apresentação é: {name_list}')
