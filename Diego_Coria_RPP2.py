from biblioteca_DiegoCoria import *

while True:
    opcion = menu()
    if opcion == "1":
        nombre_archivo = input("por favor ingrese el nombre del archivo: ")#se debe ingresar el nombre sin aclarar la extension
        nombre_archivo += ".json"
        servicios = cargar_archivo(nombre_archivo) #verificar que no tiene igualdad
    elif opcion == "2":
        imprimir_lista(servicios)
    elif opcion == "3":
        asignar_incremento(servicios)
    elif opcion == "4":
        tipo = input("Ingrese el tipo ingrese mecanica, mantenimiento o neumaticos: ")
        if tipo != "mecanica" and tipo != "mantenimiento" and tipo != "neumaticos":
            print("error, tipo ingresado es inexistente")
        else:
            servicios_filtrados = filtar_por_tipo(servicios, tipo)
            nombre_archivo = input("Ingrese el nombre del archivo para guardar el filtro: ")
            nombre_archivo += ".json"
            guardar_archivo(nombre_archivo, servicios_filtrados)
    elif opcion =="5":
        servicios_ascendente = ordenar_servicios_ascendente(servicios)
        imprimir_lista(servicios_ascendente)
    elif opcion =="6":
        nombre_archivo = input("Ingrese el nombre del archivo para guardar los servicios: ")
        nombre_archivo += ".csv"
        servicios_ascendente = ordenar_servicios_ascendente(servicios)
        guardar_archivo(nombre_archivo, servicios_ascendente)
    elif opcion == "7":
        break
    else:
       print("error, seleccione una opcion del 1 al 7...")

