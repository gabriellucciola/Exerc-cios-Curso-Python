def validacao(valor):
    if valor.replace(".", ",").count(",") > 1:
        return f"Erro: \"{valor}\" é um preço inválido"
    for digito in valor:
        if digito not in "0123456789,":
            return f"Erro: \"{valor}\" é um preço inválido"
    if valor == "":
        return f"Erro: \"{valor}\" é um preço inválido"
    return float(valor.replace(",", "."))
