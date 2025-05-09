
from veterinaria import Veterinaria # Se importa la clase Veterinaria para poder gestionar los clientes, mascotas y citas
from cliente import Cliente # Se importa la clase Cliente para poder gestionar los clientes
from mascota import Mascota # Se importa la clase Mascota para poder gestionar las mascotas 
from cita import CitaFactory # Se importa la clase CitaFactory para poder gestionar las citas



# Menú interactivo poder validar las opciones de la veterinaria
def menu():
    veterinaria = Veterinaria()

    while True:
        print("\n----- BIENVENIDA A LA VETERINARIA HUELLA FELIZ -----")
        print("1. Registrar cliente")
        print("2. Registrar mascota")
        print("3. Gestion de citas")
        print("4. Historial")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1": # Se valida la opcion 1 para registrar un cliente
            nombre = input("Nombre del cliente: ")
            telefono = input("Teléfono del cliente: ")
            cliente = Cliente(nombre, telefono)
            veterinaria.agregar_cliente(cliente)

        elif opcion == "2": # Se valida la opcion 2 para registrar una mascota y asociarla al cliente registrado
            nombre_cliente = input("Nombre del cliente: ")
            cliente = veterinaria.buscar_cliente(nombre_cliente)
            if cliente:
                nombre_mascota = input("Nombre de la mascota: ")
                especie = input("Especie de la mascota: ")
                raza = input("Raza de la mascota: ")
                mascota = Mascota(nombre_mascota, especie, raza)
                cliente.agregar_mascota(mascota)
                print(f"Mascota {nombre_mascota} registrada con éxito.")
            else:
                print("Error: Cliente no encontrado.")

        elif opcion == "3": # Este es un submenu para gestionar las citas de la veterinaria
            print("\n----- GESTION DE CITAS -----")
            print("1. Programar cita")
            print("2. Cancelar cita")
            print("3. Mostrar citas programadas")
            print("4. Mostrar clientes y mascotas")
            print("5. Volver al menu principal")
            
            sub_opcion = input("Seleccione una opcion: ") # Se valida la opcion 1 para programar una cita 
            if sub_opcion == "1":
                nombre_cliente = input("Nombre del cliente: ")
                cliente = veterinaria.buscar_cliente(nombre_cliente)
                if cliente:
                    nombre_mascota = input("Nombre de la mascota: ")
                    mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
                    if mascota:
                        fecha = input("Fecha de la cita (YYYY-MM-DD): ")
                        servicio = input("Servicio a realizar: ")
                        cita = CitaFactory.crear_cita(cliente, mascota, fecha, servicio)
                        if cita:
                            veterinaria.agregar_cita(cita)
                    else:
                        print("Error: Mascota no encontrada.")
            elif sub_opcion == "2": # Se valida la opcion 2 para cancelar una cita mostrar las citas programadas y cancelarlas
                fecha = input("Fecha de la cita a cancelar (YYYY-MM-DD): ")
                nombre_mascota = input("Nombre de la mascota: ")
                veterinaria.cancelar_cita(fecha, nombre_mascota)
            elif sub_opcion == "3":
                veterinaria.mostrar_citas()
            elif sub_opcion == "4":
                veterinaria.mostrar_clientes()
            elif sub_opcion == "5":
                continue
            else:
                print("Opción no válida. Intente de nuevo.")

        elif opcion == "4": # Se valida la opcion 4 para mostrar el historial de las citas 
            nombre_cliente = input("Nombre del cliente: ")
            cliente = veterinaria.buscar_cliente(nombre_cliente)
            if cliente:
                nombre_mascota = input("Nombre de la mascota: ")
                mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
                if mascota:
                    print(f"\nHistorial de servicios de {nombre_mascota}:")
                    mascota.historial.mostrar_historial()
                else:
                    print("Error: Mascota no encontrada.")
            else:
                print("Error: Cliente no encontrado.")

        elif opcion == "5": # Se valida la opcion 5 para salir del programa
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__": # Se ejecuta el menu principal
    menu()
