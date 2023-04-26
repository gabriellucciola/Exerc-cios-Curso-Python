def metade(num, format=False):

    valor = num / 2
    if format:
        valor = num / 2
        return valor
    return f"R${valor:.2f}".replace(".", ",")


def dobro(num, format=False):
    valor = num * 2
    if format:
        valor = num * 2
        return valor
    return f"R${valor:.2f}".replace(".", ",")


def aumentar(num, param, format=False):
    valor = num + num * param / 100
    if format:
        valor = num + num * param / 100
        return valor
    return f"R${valor:.2f}".replace(".", ",")


def diminuir(num, param, format=False):
    valor = num - num * param / 100
    if format:
        valor = num - num * param / 100
        return valor
    return f"R${valor:.2f}".replace(".", ",")


def moeda(num, format=False):
    valor = f"R${num:.2f}"
    if format:
        valor = f"R${num}"
        return valor
    return valor.replace(".", ",")


def resumo(num, aumento, dimin):
    print('-'*30)
    print(f"{'RESUMO DO VALOR':^30}")
    print('-'*30)
    print(f"{'Preço analisado:':<20}", end='')
    print(f"R${num:.2f}".replace(".", ","))
    print(f"{'Dobro do preço:':<20}", end='')
    print(f"R${num*2:.2f}".replace(".", ","))
    print(f"{'Metade do preço:':<20}", end='')
    print(f"R${num/2:.2f}".replace(".", ","))
    print(f"{f'{aumento}% de aumento:':<20}", end='')
    print(f"R${num + num*aumento/100:.2f}".replace(".", ","))
    print(f"{f'{dimin}% de diminuição:':<20}", end='')
    print(f"R${num - num*dimin/100:.2f}".replace(".", ","))
    return ""
