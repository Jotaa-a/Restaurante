from utils.jsonHandler import *
from utils.utilListas import *
from tabulate import tabulate

#      mostrar_categoria("PLATILLOS", menu_data["platillos"], pedido)
def mostrar_categorias(categoria_nombre, items, pedido):
    while True:
        print(f"\n=== {categoria_nombre.upper()} ===")  #
        i = 0
        tabla_datos = []
        for i, opt in enumerate(items, 1):  
            tabla_datos.append([i, opt['name'], f"--> ${opt['price']:,}"])
        headers = ["#", "Producto", "Precio"]
        print(tabulate(tabla_datos, headers=headers, tablefmt="fancy_grid"))
        print()
        try:   
            opt_elegida = int(input("¿Que desea ordenar? --> ")) 
            if 1 <= opt_elegida <= len(items):   
                pedido.append(items[opt_elegida - 1])
                print(f"✓ {items[opt_elegida - 1]['name']} agregado!")
            else:
                print("Opcion no válida")
        except ValueError:
            print("Solo se admiten valores numéricos")
        

def tamaño(type):
    print("== TAMAÑOS ==")
    print("== personal ==")
    print("== Grande ==")
    print("== Familiar ==")
    

def editarMenu(nameFile):
    PASSWORD = "Admon2025"
    menu_data = readFile(nameFile)
    password = input("Ingrese contraseña de adminitrador: ")
    if password != PASSWORD:
        print("Contraseña incorrecta")
        return
    
    for categoria, items in menu_data.items():
        print(f"\n=== {categoria.upper()} ===")
        for item in items:
            estado = "✓ Activo" if item.get('active', True) else "✗ Inactivo"
            print(f"  Código: {item['code']:<10} | Nombre: {item['name']:<25} | Precio: ${item['price']:<10} | {estado}")

    prodEdit = input("Codigo del producto a editar: ")
    
    encontrado = False
    categoria_encontrada = None
    info = {}

    for categoria in ["platillos", "bebidas", "adicionales"]:
        info = findFile(menu_data[categoria], "code", prodEdit)

        if len(info.keys()) > 0:
            encontrado = True
            categoria_encontrada = categoria 
            break

    if not encontrado:
        print("Código no encontrado")
        return   
    
    print(f"Producto encontrado en: {categoria_encontrada}")
    print(f"Código: {info['data']['code']}")
    print(f"Nombre: {info['data']['name']}")
    print(f"Precio: ${info['data']['price']}")
    nuevo_codigo = input("\nNuevo código (Enter para mantener el código anterior): ")
    nuevo_nombre = input("Nuevo nombre (Enter para mantener el nombre anterior): ")
    nuevo_precio = validprecio()
    nuevo_estado = input("Nuevo estado ([A]Activo/[I]Inactivo): ")

    if nuevo_codigo:
        menu_data[categoria_encontrada][info['index']]['code'] = nuevo_codigo
    if nuevo_nombre:
        menu_data[categoria_encontrada][info['index']]['name'] = nuevo_nombre
    if nuevo_precio:
        menu_data[categoria_encontrada][info['index']]['price'] = int(nuevo_precio )
    if nuevo_estado:              
        menu_data[categoria_encontrada][info['index']]['activo'] = (nuevo_estado.upper() == 'A')

    saveFile(nameFile, menu_data)
    print("\n✓ Menú actualizado exitosamente")   

def validprecio():
    while True:
        try:
            precio = int(input("Nuevo precio:"))
            return precio
        except ValueError:
            print("Precio no válido. Ingrese solo valores numericos...")

          