x = int(input('Digite o valor do imóvel que defesa o financiamento: '))
y = int(input('Digite o seu salário: '))
z = int(input('Digite em quantos meses deseja pagar o financiamento: '))
prestacao = x / z
if prestacao > y * 0.3:
    print(f'Não é possível fazer este financiamento pois o valor da prestação {prestacao:.2f} ultrapassa 30% do salário do contratante')
else:
    print(f'É possível realizar este financiamento com parcelas de R${prestacao:.2f}')
