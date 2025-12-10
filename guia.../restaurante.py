import os
def limpiar_pantalla():
    input("\nPresione ENTER para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')


def platillos(totalfinal, pedido):
    while True:
        print("\n - Bienvenido al menú de platillos - ")
        print("1. Carne asada           --------> $30000")
        print("2. Pechuga a la plancha  --------> $27000")
        print("3. Hígado                --------> $24000")
        print("4. Salir")
        plato = int(input("¿Qué platillo le gustaria?"))
        
        if plato == 4:
            print("Su menú ha sido actualizado")
            return totalfinal, pedido
        elif plato == 1:
            totalfinal += 30000
            pedido.append("Carne asada               -- $30000")
            print(f"¡Carne asada agregada! Total Actual: ${totalfinal}")
        elif plato == 2:
            totalfinal += 27000
            pedido.append("pechuga a la plancha      -- $27000")
            print(f"¡Pechuga a la plancha agregada! Total Actual: ${totalfinal}")
        elif plato == 3:
            totalfinal += 24000
            pedido.append("hígado asado              -- $24000")
            print(f"¡Hígado agregada! Total Actual: ${totalfinal}")
        else: 
            print("Opción no válida, Intente nuevamente")


def bebidas(totalfinal, pedido):
    while True:
        print("\n - Bienvenido al menú de bebidas - ")
        print("1. Coca-cola             --------> $5000")
        print("2. Jarra con panleada    --------> $10000")
        print("3. Botella con agua       --------> $2000")
        print("4. Salir")
        beber = int(input("¿Qué bebida le gustaria?"))

        if beber == 4:
                print("Su menú ha sido actualizado")
                return totalfinal, pedido
        elif beber == 1:
            totalfinal += 5000
            pedido.append("Coca-cola                 -- $5000")
            print(f"¡Coca-cola agregada! Total Actual: ${totalfinal}")
        elif beber == 2:
            totalfinal += 10000
            pedido.append("Jarra con panelada        -- $10000")
            print(f"¡Jarra de panelada agregada! Total Actual: ${totalfinal}")
        elif beber == 3:
            totalfinal += 2000
            pedido.append("Botella con agua          -- $2000")
            print(f"¡Botella con agua agregada! Total Actual: ${totalfinal}")
        else:
            print("Opción no válida. Intente nuevamente")


def adicional(totalfinal, pedido):
    while True:
        print("\n - Bienvenido al menú de adicionales - ")
        print("1. Salsa de la casa  --------> $4000")
        print("2. Papitas fritas    --------> $7000")
        print("3. Porcion de arroz  --------> $11000")
        print("4. Salir")
        extra = int(input("¿Qué adicional le gustaria?"))

        if extra == 4:
                print("Su menú ha sido actualizado")
                return totalfinal, pedido
        elif extra == 1:
            totalfinal += 4000
            pedido.append("Salsa de la casa          -- $4000")
            print(f"¡Salsa de la casa agregada! Total Actual: ${totalfinal}")
        elif extra == 2:
            totalfinal += 7000
            pedido.append("Papitas fritas            -- $7000")
            print(f"¡Papitas fritas agregada! Total Actual: ${totalfinal}")
        elif extra == 3:
            totalfinal += 11000
            pedido.append("Porción de arroz          -- $11000")
            print(f"¡Porción de arroz agregada! Total Actual: ${totalfinal}")
        else: 
            print("Opción no válida. Intente nuevamente")

def factura(totalfinal, pedido):
    print("\n============== FACTURA ==============")
    for item in pedido:
        print(item)
    print(f"\nTOTAL A PAGAR: ${totalfinal}")

def menuPrincipal(totalfinal, pedido): 
    while True:
        limpiar_pantalla()
        print("\n--- Bienvenido ---")
        print("1. Menú platillos")  
        print("2. Bebidas")
        print("3. Adicionales")
        print("0. Salir")
        opcion = int(input("¿Cúal menú desea visualisar? ->"))
        if opcion == 0: 
            limpiar_pantalla()
            factura(totalfinal, pedido)
            print("Gracias por utilizar el programa :)")
            break
        elif opcion == 1:
            totalfinal, pedido = platillos(totalfinal, pedido)
        elif opcion == 2:
            totalfinal, pedido = bebidas(totalfinal, pedido)
        elif opcion == 3:
            totalfinal, pedido = adicional(totalfinal, pedido)

pedido = []
totalfinal = 0
menuPrincipal(totalfinal, pedido)


