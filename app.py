 
tareas = []

def agregar_tarea():
    nombre = input("Ingrese la tarea: ")
    tareas.append({"nombre" : nombre, "completada": False})
    print("Tarea agregada correctamente")

def listar_tareas():
    print("==== LISTA DE TAREAS ====")
    if len(tareas) == 0:
        print("No hay tareas registradas")
    else:
        for i, tarea in enumerate(tareas,1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}. {tarea["nombre"]} - {estado}")
def completar_tarea():
    listar_tareas()
    if len(tareas) == 0:
        return 
    numero = int(input("Numero de tarea a completar: "))
    if 1 <= numero <=len(tareas):
        tareas[numero - 1]["completada"] = True 
        print("Tarea completada correctamente")
    else:
        print("Numero de tarea incorrecto")
def eliminar_tarea():
    listar_tareas()
    if len(tareas) == 0:
        return

    numero = int(input("Numero de tarea a eliminar: "))
    if 1 <= numero <= len(tareas):
        tareas.pop(numero - 1)
        print("Tarea eliminada correctamente")
    else:
        print("Numero de tarea incorrecto")


def main():
    while True:
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
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            break


if __name__ == "__main__":
    main()
