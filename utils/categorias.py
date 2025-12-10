import os
from utils.jsonHandler import *
from utils.utilListas import *
from tabulate import tabulate
MENU_PIZZERIA = "./Database/menu.json"

def limpiar_pantalla():
    input("\nPresione ENTER para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')
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
            opt_elegida = int(input("¿Que desea ordenar? (0 para salir) --> ")) 
            if 1 <= opt_elegida <= len(items):   
                pedido.append(items[opt_elegida - 1])
                print(f"✓ {items[opt_elegida - 1]['name']} agregado!")
            elif opt_elegida == 0:
                print("Saliendo....")
                break
            else:
                print("-"*20)
                print("Opcion no válida")
                print("-"*20)
        except ValueError:
            print("-"*35)
            print("Solo se admiten valores numéricos")
            print("-"*35)
        

def mostrar_pizzas(categoria_nombre, items, pedido):
    while True:
        print(f"\n=== {categoria_nombre.upper()} ===")
        tabla_datos = []

        for i, pizza in enumerate(items, 1):
            precios = f"p: ${pizza['sizes']['personal']:,} | g: ${pizza['sizes']['grande']:,} | f: ${pizza['sizes']['familiar']:,}"
            tabla_datos.append([i, pizza['name'], precios])

        headers = ("#", "Pizza", "Precios (Personal | Grande | Familiar)")
        print(tabulate(tabla_datos, headers=headers, tablefmt="fancy_grid"))
        print()

        try:
            opt_elegida = int(input("\n¿Que pizza desea ordenar? (0 para salir) --> "))
            if opt_elegida == 0:
                break
            if 1 <= opt_elegida <= len(items):
                pizza_selecionada = items[opt_elegida - 1]
                while True:
                    tabla_dato = []
                    try:
                        item = ("Personal", "Grande", "Familiar")
                        for i, tamaño in enumerate(item, 1):
                            tabla_dato.append([i, tamaño])
                        headers = ("#", "Tamaño",)
                        print(tabulate(tabla_dato, headers=headers, tablefmt="fancy_grid"))
                        tamaño_opt = int(input("Seleccione el tamaño que desea --> "))
                        tamaños = {1: "personal", 2: "grande", 3: "familiar"}

                        if tamaño_opt in tamaños:
                            tamaño = tamaños[tamaño_opt]
                            precio = pizza_selecionada['sizes'][tamaño]
                            pedido.append({
                                "code": pizza_selecionada['code'],
                                "name": f"{pizza_selecionada['name']} ({tamaño.capitalize()})",
                                "price": precio,
                                "active": pizza_selecionada['active']                  
                            })
                            print(f"{pizza_selecionada['name']} ({tamaño}) agregada!")
                            
                            try:
                                if len(pedido)>0:
                                    ad = input("¿Desea ver el menú de adicionales (S/N)? ").lower()
                                    if ad == "s":
                                        menu_data = readFile(MENU_PIZZERIA)
                                        mostrar_categorias("ADICIONALES", menu_data["adicionales"], pedido)    
                                        limpiar_pantalla()
                                        break
                                else: 
                                    print("continuando sin adicionales...")
                                    break
                            except ValueError:
                                print("-"*20)
                                print("Eleccion no válida")
                                print("-"*20)
                            break
                        else:
                            print("-"*20)
                            print("Tamaño no válido")
                            print("-"*20)
                    except ValueError:
                        print("-"*36)
                        print("Solo se admiten valores numéricos")
                        print("-"*36)
            else:
                print("-"*20)
                print("Opcion no válida")
                print("-"*20)
        except ValueError:
            print("-"*36)
            print("Solo se admiten valores numéricos")
            print("-"*36)
    print("Saliendo...")


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
            estado = "✓ Activo" if item.get('active', True) else "Inactivo"
            if 'sizes' in item:
                precios = f"Personal: ${item['sizes']['personal']} | Grande: ${item['sizes']['grande']} | Familiar: ${item['sizes']['familiar']}"
                print(f"  Código: {item['code']:<10} | Nombre: {item['name']:<25} | {precios} | {estado}")
            else:  # ← Bebida o adicional
                print(f"  Código: {item['code']:<10} | Nombre: {item['name']:<25} | Precio: ${item['price']:<10} | {estado}")
   
    prodEdit = input("Codigo del producto a editar: ")
    
    encontrado = False
    categoria_encontrada = None
    info = {}

    for categoria in ["pizzas", "bebidas", "adicionales"]:
        info = findFile(menu_data[categoria], "code", prodEdit)

        if len(info.keys()) > 0:
            encontrado = True
            categoria_encontrada = categoria 
            break

    if not encontrado:
        print("-"*30)
        print("Código no encontrado")
        print("-"*30)
        return   
    print("="*50)
    print(f"Producto encontrado en: {categoria_encontrada}")
    print(f"Código: {info['data']['code']}")
    print(f"Nombre: {info['data']['name']}")
    if 'sizes' in info['data']:
        print(f"Precio personal: ${info['data']['sizes']['personal']}")
        print(f"Precio grande: ${info['data']['sizes']['grande']}")
        print(f"Precio familiar: ${info['data']['sizes']['familiar']}")
    else:
        print(f"Precio: ${info['data']['price']}")
        
    nuevo_codigo = input("\nNuevo código (Enter para mantener el código anterior): ")
    nuevo_nombre = input("Nuevo nombre (Enter para mantener el nombre anterior): ")

    if 'sizes' in info['data']:  # ← Es una pizza
        print("\n=== ACTUALIZAR PRECIOS ===")
        nuevo_precio_personal = input("Nuevo precio Personal (Enter para mantener): ")
        nuevo_precio_mediana = input("Nuevo precio Mediana (Enter para mantener): ")
        nuevo_precio_familiar = input("Nuevo precio Familiar (Enter para mantener): ")
    else:  
        nuevo_precio = input("Nuevo precio (Enter para mantener): ")

    nuevo_estado = input("Nuevo estado ([A]Activo/[I]Inactivo): ")

    if nuevo_codigo:
        menu_data[categoria_encontrada][info['index']]['code'] = nuevo_codigo
    if nuevo_nombre:
        menu_data[categoria_encontrada][info['index']]['name'] = nuevo_nombre
    
    if 'sizes' in info['data']:  # ← Es una pizza
        if nuevo_precio_personal:
            menu_data[categoria_encontrada][info['index']]['sizes']['personal'] = int(nuevo_precio_personal)
        if nuevo_precio_mediana:
            menu_data[categoria_encontrada][info['index']]['sizes']['mediana'] = int(nuevo_precio_mediana)
        if nuevo_precio_familiar:
            menu_data[categoria_encontrada][info['index']]['sizes']['familiar'] = int(nuevo_precio_familiar)
    else:  
        if nuevo_precio:
            menu_data[categoria_encontrada][info['index']]['price'] = int(nuevo_precio)

    if nuevo_estado:              
        menu_data[categoria_encontrada][info['index']]['activo'] = (nuevo_estado.upper() == 'A')

    saveFile(nameFile, menu_data)
    print("-"*35)
    print("\n✓ Menú actualizado exitosamente")   
    print("-"*35)

def validprecio():
    while True:
        try:
            precio = int(input("Nuevo precio:"))
            return precio
        except ValueError:
            print("-"*55)
            print("Precio no válido. Ingrese solo valores numericos...")
            print("-"*55)

def nueva_factura(ruta, pedido, ):
    while True:
        if len(pedido) == 0:
            print("-"*30)
            print("No hay items en el pedido")
            print("-"*30)
            limpiar_pantalla()
            break
        else:
            total = sum(item['price'] for item in pedido)
            factura = {
                "date": fechaFactura(),
                "name": input("Ingrese nombre del cliente -> "),
                "products": pedido,
                "total": total 
            }
            dataBill = readFile(ruta)
            dataBill.append(factura)
            saveFile(ruta, dataBill)

        print("\n=== FACTURA ===")
        print(f"Cliente: {factura['name']}")
        print(f"Fecha: {factura['date']}")
        print("\nProductos:")
        for item in pedido:
            print(f"  ✔ {item['name']} - ${item['price']}")
        print(f"\nTOTAL: ${total}")
        print("-"*35)
        print("\n✓ Factura guardada exitosamente") 
        print("-"*35)              
        pedido.clear()
        break