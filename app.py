 
tareas = []

def agregar_tarea():
    nombre = input("Ingrese la tarea: ")
    tareas.append(nombre)
    print("Tarea agregada correctamente")

def listar_tareas():
    print("==== LISTA DE TAREAS ====")
    if len(tareas) == 0:
        print("No hay tareas registradas")
    else:
        for tarea in tareas:
            print(tarea)

def main():
    print("====GESTOR DE TAREAS====")
    print("1. Agregar tarea")
    print("2. Lista de tareas")
    print("3. Completar tareas")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        listar_tareas()


if __name__ == "__main__":
    main()
