print(print ("Ejercicio 4 sin funciones"))
print("Ingresar un número entre 0 y 999, luego mostrar la cantidad de dígitos que tiene")

while True:
    n=int(input("Ingresar un valor entre 0 y 999: "))
    if(n>0 and n<999):
        if(n<10):
            print( "EL número ",n," ingresado tiene un dígito ")
        elif(n<100): 
            print( "EL número " ,n, " ingresado tiene dos dígitos")
        else:
            print(n, "Tiene tres dígitos:  ")
    break
    #resolucion de