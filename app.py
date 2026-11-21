 
tareas = []

def agregar_tarea():
    nombre = input("Ingrese la tarea: ")
    tareas.append(nombre)
    print("Tarea agregada correctamente")


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
   


if __name__ == "__main__":
    main()
