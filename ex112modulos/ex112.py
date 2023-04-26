from dados import validacao
from moedas import moedas

value = True
while value:
    valor = validacao.validacao(input('Digite um valor: R$').strip().replace(".", ","))
    if isinstance(valor, float):
        print(moedas.resumo(valor, 10, 13))
        break
    else:
        print(valor)
