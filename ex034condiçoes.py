salario = int(input('Digite o salário do funcionário: '))
if salario > 1250:
    print(f'O salário reajustado será de R${salario*1.1:.2f}')
else:
    print(f'O salário reajustado será de R${salario*1.15:.2f}')
