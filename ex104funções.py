def leiaInt(mensagem):
    numero = input(f"{mensagem}")
    for i in range(0, len(numero)):
        if numero[i] not in "0123456789":
            print(f"\033[91mERRO! Digite um número inteiro válido\033[m")
            return False
    print(f'Você acabou de digitar o número {numero}')
    return True


retorno = False
while retorno == False:
    retorno = leiaInt('Digite um número: ')