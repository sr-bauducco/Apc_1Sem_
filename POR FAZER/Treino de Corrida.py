# # Treino de Corrida
n = int(input())
tempo = ""
i =0
voltas=[]
ordem = []
count = 0
while i < n:
    tempo=input()
    voltas.append(tempo)
    i+=1
voltas.sort()
for f in range(0,len(voltas)-1):
        if voltas[f] == voltas[f+1]:
            count +=1
            if f == len(voltas)-2:
                ordem = count+1 
                # print(voltas[f],",",count+1)
        else:
            # print(voltas[f],",",count+1)
            count=0
print(ordem)


















# n= int(input())
# i=0
# voltas=[]
# count=1
# anterior=0
# while i < n:
#     tempo=input()
#     if tempo == anterior :
#         count+=1
#     else:
#         count=0
#     voltas.append(tempo)
#     anterior = tempo
#     i+=1
# # print(voltas)
# print(count)