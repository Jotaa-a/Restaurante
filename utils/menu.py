# se pasa title y options como argumentos desde main.py 
def menu(title, options):
    ind = 1 # -> se inicia el indice en 1
    choise = 0
    print("===================================================  ")
    print(f" == {title} ==")
    print("===================================================")
    print(" ==  Opciones de menús disponibles   == ")
    print("==")

    # Se recorre/itera la tupla de opciones y se imprime linea a linea
    for item in options:
        print(f"{ind}. {item}") # -> Muestra el indice y cada item de la tupla
        ind +=1 # -> Incrementa 1 en el indice por cada iteracion que realice

    while True:
        # Se valida que el valor ingresado coincida con el pedido (enteros en este caso)

        try:
            # Se valida que el valor ingresado esté dentro del rango de opciones.
            choise = int(input("¿Qué desea hacer? --> "))
            if choise not in range(1,len(options)+1):
                print("Opcion no válida, intente nuevamente...")
            else:
                break
        except ValueError: # -> Si el valor ingresado no coincide con el solicitado, lo solicita nuevamente sin detener el programa
            print("Sea serio ome, ponga un numero caremondá")
    return choise
