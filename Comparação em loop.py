# Comparação em loop
def comparacao(a, b):
    if a > b :
        print(f'{a} eh maior que {b}')
    else:
        print(f'{b} eh maior que {a}')
        
n = int(input()) 
lista=[]
while n > 0:
    lista = input().split()
    lista.sort()
    lista = list(map(int,lista))
    # print(lista)
    comparacao(lista[0],lista[1])
    # print(f'{lista[0]} eh maior que {lista [1]}')
    n = n-1
    