import os
from utils.menu import menu
from utils.jsonHandler import *
from utils.categorias import *
from utils.utilListas import *

def limpiar_pantalla():
    input("\nPresione ENTER para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')


MENU_DEL_RESTAURANTE = "./Database/menu.json" # se asigna MENU... como una constante de la ruta 
RESTAURANT_BILL = "./Database/bills.json"
principal_options = ("Platillos", "Bebidas", "Adicionales", "Nueva factura", "Ver facturas anteriores", "Administrar menu", "Salir\n") # Se crea una tupla donde se almacenan las opcines principales
pedido = []
total = 0

while True:
    menu_data = readFile(MENU_DEL_RESTAURANTE) # se asigna a menu_data el menu del restaurante usando la funcion readFile
    choise = menu("B I E N V E N I D O   A   C A R N I V O R O", principal_options) # Se pasa a menu los argumentos requeridos
    print(f"Opcion elegida: {choise}")
    match choise: 
        case 1: 
            mostrar_categorias("PLATILLOS", menu_data["platillos"], pedido)
            limpiar_pantalla() 

        case 2:
            mostrar_categorias("BEBIDAS", menu_data["bebidas"], pedido) 
            limpiar_pantalla()

        case 3:
            mostrar_categorias("ADICIONALES", menu_data["adicionales"], pedido)    
            limpiar_pantalla()

        case 4:
            if len(pedido) == 0:
                print("No hay items en el pedido")
            else:
                total = sum(item['price'] for item in pedido)
                factura = {
                    "date": input("Ingrese la fecha de hoy -> "),
                    "name": input("Ingrese nombre del cliente -> "),
                    "products": pedido,
                    "total": total 
                }
                dataBill = readFile(RESTAURANT_BILL)
                dataBill.append(factura)
                saveFile(RESTAURANT_BILL, dataBill)

                print("\n=== FACTURA ===")
                print(f"Cliente: {factura['name']}")
                print(f"Fecha: {factura['date']}")
                print("\nProductos:")
                for item in pedido:
                    print(f"  ✔ {item['name']} - ${item['price']}")
                print(f"\nTOTAL: ${total}")
                print("\n✓ Factura guardada exitosamente")
                limpiar_pantalla()

        case 5:
            findName = input("Ingrese el nombre del cliente a buscar --> ")
            dataBill = readFile(RESTAURANT_BILL)
            info = findFile(dataBill, "name", findName)
            if len(info.keys()) == 0:
                print("❌ Cliente no encontrado")
                limpiar_pantalla()
            else:
                print("\n=== FACTURA ENCONTRADA ===")
                factura = info["data"]
                print(f"Cliente: {factura['name']}")
                print(f"Fecha: {factura['date']}")
                print("\nProductos:")
                for item in factura['products']:
                    print(f"  ✔ {item['name']} - ${item['price']}")
                print(f"\nTOTAL: ${factura['total']}")
                limpiar_pantalla()
        
        case 6:
            editarMenu(MENU_DEL_RESTAURANTE)
            limpiar_pantalla()
        case 7:
            print("-"*20)
            print("==  chaito bro  ==")
            print("-"*20)
            break