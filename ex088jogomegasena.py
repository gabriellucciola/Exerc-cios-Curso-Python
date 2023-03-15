import random
import time

palpites = []
jogo = []
cont1 = cont2 = 1
print('-'*40)
print(f'{"JOGO NA MEGA SENA":^40}')
print('-'*40)
quant_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, f'  SORTEANDO {quant_jogos} JOGOS  ', '-='*3)
while cont1 <= quant_jogos:
    while cont2 <= 6:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont2 += 1
    cont2 = 1
    palpites.append(jogo[:])
    jogo.clear()
    cont1 += 1
time.sleep(1)
for k, jogo in enumerate(palpites):
    jogo.sort()
    print(f'Jogo {k+1}: {jogo}')
    time.sleep(1)
print(f'{"< BOA SORTE! >":-^40}')
