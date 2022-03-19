# looPa
lista= input().split()
a,r,n = list(map(int, lista))
count=0
soma = 0
while count < n:    
    print(f'{a}')
    soma = soma + a
    a = a+r
    # soma = soma + a
    count += 1
print(soma)
    



