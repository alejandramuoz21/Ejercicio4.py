lista = []
salir = False
while(not salir):
    num = int(input("Dame un numero: "))
    if(num == 0):
        salir = True
    else:
        lista.append(num)
print(lista)