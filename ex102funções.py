def fatorial(num=1, show=False):
    """Shows a result of factorial number
    param: num = value to show the factorial
    param: show = (optional) shows the process to calculate the factorial
    :return: The value of num Factorial"""
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
    if not show:
        return fat
    else:
        for i in range(num, 0, -1):
            print(f'{i} ', end='')
            if i > 1:
                print('x ', end='')
            else:
                print(f'= {fat}')
        return ''


print(fatorial(10, True))
help(fatorial)