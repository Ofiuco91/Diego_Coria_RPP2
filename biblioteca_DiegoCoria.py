import json

def menu(): #genero el menu de opciones
    opcion = input("""------ Menu de opciones -----------
                1) Cargar archivo
                2) Imprimir lista
                3) Asignar incremento
                4) Filtrar por tipo
                5) Mostrar servicios
                6) Guardar servicios
                7) Salir.
                   Opcion...""")
    return opcion

def cargar_archivo(archivo):
    #cargo el archivo ingresando el nombre por parametro
    try:
        with open(archivo, "r") as archivo: #selecciono para que se abra en formato "read"
            servicios = json.load(archivo) #lo cargo
        return servicios
    except FileNotFoundError:
        print("El archivo no existe.")
        return None
    
def guardar_archivo(nombre_archivo, servicios):
    # recibe un nombre y una lista y las guarda 

    with open(nombre_archivo, 'w') as archivo:
        json.dump(servicios, archivo, indent=4)

def imprimir_lista(lista):
    #genero un for para que recorra las listas y las vaya imprimiendo en orden
    print("id_servicio //descripcion                                          // tipo                         //precio unitario                  // cantidad    //cliente")
    for i in lista:
        print(f"{i["id_servicio"]:<2}            {i["descripcion"]:<50}   {i["tipo"]:<30}     {i["precioUnitario"]:<20}             {i["cantidad"]:<10}    {i["cliente"]:<10}")
   
def asignar_incremento(servicios):
    #recibe una lista y le asignara un 10% mas al precio unitario 
    for servicio in servicios:
        servicio["precioUnitario"] = round((lambda p: p * 1.10)(float(servicio["precioUnitario"])),1) #hago que aparezca con un solo decimal
    return servicios



def filtar_por_tipo(servicios, tipo):
    #Recibe una lista y un string, los clasifica por tipo y retorna la lista
    filtrados = []
    for servicio in servicios:
        if servicio["tipo"] == tipo:
            filtrados.append(servicio)
        

    return filtrados

def ordenar_servicios_ascendente(servicios):
    #Recibe una lista y ordena los clientes
    return sorted(servicios, key=lambda x: x["cliente"])




