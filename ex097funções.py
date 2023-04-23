def mensagem(msg):
    print('~'*len(msg))
    print(msg)
    print('~'*len(msg))

m = input("Digite o que quiser: ").strip()
mensagem(m)

