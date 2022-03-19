# Dêivis em fuga
l_inicial = int(input())
count=-1
l = l_inicial
while 0 == 0: 
    n = int(input())
    if n == 0:
        l = l-1
        count +=1
        # print(f'litros{l}')
    elif n == 1:
        x = int(input())
        if x > l:
            l = l_inicial
        else:
            l = l + x
        count +=1
        # print(f'litros{l}')
    elif n == 2:
        y = int(input())
        l = l-y
        if( l<0):
            count+=0
            print(count)
            break
        else:
            count +=1
        # print(f'litros{l}')
    elif n < 0:
        if l > 0:
            print(f'Lar Deivis lar')
            # print(count)
        else:
            print(count)
        break
    