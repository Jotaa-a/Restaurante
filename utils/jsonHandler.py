from json import dumps, load

def readFile(fileName): #Recive el nombre o ruta del archivo que se quiere leer
    try:
        fileData = None # fileData contentrá los datos del archivo leido, se inicializa en none para que no exista antes de leer el archivo
        with open(fileName) as f: #con with, el archivo se cierra automaticamente cuando se deje de usar, con open se abre el archivo y con f se renombra temporalmente
            fileData = load(f) # con el load se convierte un archivo .json a un diccionario de python y se almacena en fileData
            f.close()
        return fileData # Se retorna el contenido del json ahora como diccionario 
    except: # En caso de que no encuentre la ruta o que el diccionario esté vacio, devuelve una lista vacia sin cerrar el programa.
        return [] 
    
def saveFile(fileName, data):
    jsonFile = open(fileName, "w", encoding='utf-8')
    jsonFile.write(dumps(data,  indent=4, ensure_ascii=False)) # -> convierte texto a json
    jsonFile.close()
    print("Datos guardados con exito")   
    