from utils.menu import menu
from utils.jsonHandler import *
from utils.categorias import *
from utils.utilListas import *


MENU_PIZZERIA = "./Database/menu.json" # se asigna MENU... como una constante de la ruta 
PIZZERIA_BILL = "./Database/bills.json"
principal_options = ("Pizzas", "Bebidas", "Nueva factura", "Ver facturas anteriores", "Administrar menu", "Salir\n") # Se crea una tupla donde se almacenan las opcines principales
total = 0
pedido = []

def main():
    i = 0
    while True:
        
        menu_data = readFile(MENU_PIZZERIA) # se asigna a menu_data el menu del restaurante usando la funcion readFile
        choise = menu("B I E N V E N I D O   A   C A R N I V O R O", principal_options) # Se pasa a menu los argumentos requeridos
        print(f"Opcion elegida: {choise}")
        match choise: 
            case 1: 
                mostrar_pizzas("PIZZAS", menu_data["pizzas"], pedido)
                limpiar_pantalla() 
             
            case 2:
                mostrar_categorias("BEBIDAS", menu_data["bebidas"], pedido) 
                limpiar_pantalla()
            
            case 3:
                nueva_factura(PIZZERIA_BILL, pedido, ) 
                limpiar_pantalla()

            case 4:
                findName = input("Ingrese el nombre del cliente a buscar --> ")
                dataBill = readFile(PIZZERIA_BILL)
                info = findFile(dataBill, "name", findName)
                if len(info.keys()) == 0:
                    print("Cliente no encontrado ❎")
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
            
            case 5:
                editarMenu(MENU_PIZZERIA)
                limpiar_pantalla()
            case 6:
                print("-"*20)
                print("==  chaito bro 🌚 ==")
                print("-"*20)
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrucion forzada por usuario")