def validacao(valor):
    cont = 0
    cont_num = 0
    if valor == ',':
        return f"\033[31mErro: \"{valor}\" é um preço inválido\033[m"
    if valor.count(",") > 1:
        return f"\033[31mErro: \"{valor}\" é um preço inválido\033[m"
    for digito in valor:
        if digito not in "0123456789,":
            return f"\033[31mErro: \"{valor}\" é um preço inválido\033[m"
        else:
            cont_num += 1
        if digito in ",":
            cont += 1
        if valor == "":
            return f"Erro: \"{valor}\" é um preço inválido"
    if cont == 1 and cont_num == 0:
        return f"\033[31mErro: \"{valor}\" é um preço inválido\033[m"
    return float(valor.replace(",", "."))
