# Buscar/encontrar indice de un diccionario
from datetime import datetime
def findFile(dataList, key, value):
    info = {} # -> Crea un diccionario vacio para almacenar la informacion requerida
    for i in range(len(dataList)): # Recorre la lista en busca del indice (i) que se requiere 
        if dataList[i].get(key) == value: # si lo encunetra, obtiene la llave y el valor/data de esa llave
            info["index"] = i # Se le asigna a i el indice encontrado 
            info["data"] = dataList[i] # Se asigna a dataList la data encontrada en el indice (i)
            break
    return info 

def fechaFactura():
    hoy = datetime.now().strftime("%d/%m/%Y")
    return hoy
    
