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
