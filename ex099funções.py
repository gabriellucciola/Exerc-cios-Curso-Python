from time import sleep

def maior(*nums):
    print('-='*20)
    if not nums:
        print('Nenhum número foi passado')
        return 
    print('Analisando os valores passados...')
    cont = 0
    for num in nums:
        cont += 1
        sleep(.5)
        print(f'{num} ', end='')
    print(f'Foram digitados {cont} valores ao todo')
    print(f'O maior valor é {max(nums)}')

maior(7, 1, 6, 7, 2, 0)
maior(8, 1, 5, 3, 10)
maior(6)
maior(88, 142, 256, 1, 55)
maior()