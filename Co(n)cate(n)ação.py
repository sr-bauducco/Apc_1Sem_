# Iteração - Co(n)cate(n)ação - APC 

s,w,n = input().split()
tamanho = len(s)
while (tamanho % int(n)) > 0:
    s=s+w
    tamanho = len(s)
    # print(tamanho)

print(s)
    