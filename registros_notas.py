lista_estudiantes = []

def registrar_nota():
    print("----- Registrar al Estudiante -----")
    nombre = input("Ingrese el nombre: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))

    estudiante = {
        "nombre": nombre,
        "nota": nota
    }
    lista_estudiantes.append(estudiante)
    print(f"{nombre} ha sido registrado con éxito.")
    print("-"*50)
def mostrar_notas():
        print("-------Lista de Notas Actualizada-------")
        if not lista_estudiantes:
             print("La lista esta vacía.")
        else: 
            for e in lista_estudiantes:
                print(f"Estudiantes: {e['nombre']} | Nota: {e['nota']}")
        print("-"*50)
def buscar_estudiante():
        print("-----Buscar Estudiante-----")
        nombre_buscar = input("Ingrese el nombre a buscar: ")
        for e in lista_estudiantes:
            if e['nombre'] == nombre_buscar:
                print(f"La nota de: {e['nombre']} es {e['nota']}")
                return
            
        print("No se encontro al Estudiante")

def eliminar_estudiante():
        print("\n----- Eliminar Estudiante -----")
        nombre_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
        for e in lista_estudiantes:
            if e['nombre'] == nombre_eliminar:
                 lista_estudiantes.remove(e)
                 print(f"Registro de {nombre_eliminar} eliminado.")
                 return
            
        print("No se encontró al estudiante.")

while True:
     print("-----Sistema Académico de Notas------")
     print("------Menú Principal------")
     print("1.Registrar al Estudiante")
     print("2.Ver la Lista de Notas")
     print("3.Buscar al Estudiante")
     print("4.Eliminar al Estudiante")
     print("5.Salir del Sistema")
     opcion = input("Seleccione una opcion (1,2,3,4,5): ")
     if opcion == "1":
          registrar_nota()
     elif opcion == "2":
          mostrar_notas()
     elif opcion == "3":
          buscar_estudiante()
     elif opcion == "4":
          eliminar_estudiante()
     elif opcion == "5":
          print("Saliendo del Sistema")
          break
     else:
          print("Opcion no Valida")
