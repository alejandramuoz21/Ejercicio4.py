meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
salir = False
while not False:
    numero = int(input("Dame un nuenro: "))
    if numero == 0:
       salir = True
    else:
        if(numero >= 1 and numero <= len (meses)):
            print(meses[numero - 1])
        else:
            print("Inserta un numero entre 1 y ", len(meses))