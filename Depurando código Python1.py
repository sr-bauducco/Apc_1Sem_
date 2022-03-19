
def par(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
x = int(input())
acumulador = 0
achou_par = False
cont=0
while x > 0:
    achou_par = par(x)
    if achou_par:
        cont += 1
        acumulador = acumulador + x
    x = int(input())

# media_par = acumulador/cont
# print(media_par)
try:
    media_par = acumulador/cont
    print(media_par)
except ZeroDivisionError:
    media_par = 0.0
    print(media_par)