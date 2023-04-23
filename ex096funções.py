def área(l, c):
    print(f"A área do terreno {l:.1f}x{c:.1f} é de {l*c}m²")


print("Controle de Terrenos")
print('-'*20)
larg = float(input("LARGURA (m): "))
comp = float(input("COMPRIMENTO (m): "))
área(larg, comp)
