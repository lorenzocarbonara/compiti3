listaA=[]
listaB=[]
a=True
while a==True:
    print("Inserire le parole che vuoi mettere nella lista, per uscire digitare E")
    parola1=input()
    if parola1=="E":
        a=False
    else:
        listaA.append(parola1)
b=len(listaA)
for i in range(b):
    num2=len(listaA[i])
    listaB.append(num2)
print(listaB)