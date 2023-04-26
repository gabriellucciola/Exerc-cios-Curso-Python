def metade(num):
    valor = num/2
    return f"R${valor:.2f}".replace(".", ",")


def dobro(num):
    valor = num*2
    return f"R${valor:.2f}".replace(".", ",")


def aumentar(num, param):
    valor = num + num * param/100
    return f"R${valor:.2f}".replace(".", ",")


def diminuir(num, param):
    valor = num - num * param/100
    return f"R${valor:.2f}".replace(".", ",")


def moeda(num):
    valor = f"R${num:.2f}"
    return valor.replace(".", ",")
