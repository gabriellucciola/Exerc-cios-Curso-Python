def leiaInt(mensagem):
    while True:
        numero = input(f"{mensagem}")
        try:
            numero = int(numero)
            return numero
        except:
            print(f"\033[91mERRO! Digite um número inteiro válido\033[m")


def floating(valor):
    while True:
        num = input(f"{valor}").replace(",", ".")
        try:
            for char in num:
                if char not in "0123456789." or len(num) == 1:
                    raise TypeError("Valor digitado é inválido, tente novamnte!")
            if "." not in num:
                raise ValueError("O valor deve conter um ponto flutuante")
            num = float(num)
            return num
        except ValueError as e:
            print(f"\033[91mERRO! {e}\033[m")
        except TypeError as e:
            print(f"\033[91mERRO! {e}\033[m")
        else:
            print(f"\033[91mERRO! Digite um real inteiro válido\033[m")


while True:
    inteiro = leiaInt("Digite um inteiro: ")
    if isinstance(inteiro, int):
        break
while True:
    real = floating('Digite um real: ')
    if isinstance(real, float):
        break
print(f"O valor inteiro digitado foi {inteiro} e o real foi {real}")