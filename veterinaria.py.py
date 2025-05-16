# ==============================
# SISTEMA DE CLÍNICA VETERINARIA
# ==============================
# Este programa aplica Programación Orientada a Objetos (POO),
# representando cada entidad real con una clase:
# - Dueno: dueño de la mascota
# - Mascota: animal de compañía
# - Consulta: cita veterinaria

# Cada clase tiene atributos (datos) y métodos (acciones),
# facilitando la organización y reutilización del código.


# CLASE DUEÑO
class Dueno:
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"{self.nombre} | Tel: {self.telefono} | Dir: {self.direccion}"


# CLASE MASCOTA
class Mascota:
    def __init__(self, nombre, especie, raza, edad, dueno):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.dueno = dueno
        self.consultas = []

    def agregar_consulta(self, consulta):
        self.consultas.append(consulta)

    def mostrar_historial(self):
        if not self.consultas:
            return f"No hay consultas para {self.nombre}."
        historial = f"Historial de {self.nombre}:
"
        for c in self.consultas:
            historial += str(c) + "\n"
        return historial

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self.raza} | {self.edad} años | Dueño: {self.dueno.nombre}"

# CLASE CONSULTA
class Consulta:
    def __init__(self, fecha, motivo, diagnostico, mascota):
        self.fecha = fecha
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.mascota = mascota

    def __str__(self):
        return f"[{self.fecha}] Motivo: {self.motivo} | Diagnóstico: {self.diagnostico}"


# LISTAS DE DATOS
duenos = []
mascotas = []

# FUNCIONES DEL MENÚ
def registrar_mascota():
    print("\n--- Registrar Nueva Mascota ---")
    nombre_mascota = input("Nombre de la mascota: ")
    especie = input("Especie: ")
    raza = input("Raza: ")
    edad = input("Edad: ")
    
    print("Ingrese datos del dueño:")
    nombre_dueno = input("Nombre del dueño: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")

    dueno = Dueno(nombre_dueno, telefono, direccion)
    duenos.append(dueno)

    mascota = Mascota(nombre_mascota, especie, raza, edad, dueno)
    mascotas.append(mascota)
    print("Mascota registrada con éxito.")


def registrar_consulta():
    print("\n--- Registrar Consulta ---")
    if not mascotas:
        print("No hay mascotas registradas.")
        return
    for i, m in enumerate(mascotas):
        print(f"{i + 1}. {m.nombre} - Dueño: {m.dueno.nombre}")
    
    try:
        indice = int(input("Seleccione la mascota (número): ")) - 1
        mascota = mascotas[indice]

        fecha = input("Fecha (dd/mm/aaaa): ")
        motivo = input("Motivo de la consulta: ")
        diagnostico = input("Diagnóstico: ")

        consulta = Consulta(fecha, motivo, diagnostico, mascota)
        mascota.agregar_consulta(consulta)

        print("Consulta registrada con éxito.")
    except (IndexError, ValueError):
        print("Selección inválida.")


def listar_mascotas():
    print("\n--- Mascotas Registradas ---")
    if not mascotas:
        print("No hay mascotas registradas.")
    else:
        for m in mascotas:
            print(m)


def ver_historial():
    print("\n--- Historial de Consultas ---")
    if not mascotas:
        print("No hay mascotas registradas.")
        return
    for i, m in enumerate(mascotas):
        print(f"{i + 1}. {m.nombre} - Dueño: {m.dueno.nombre}")
    
    try:
        indice = int(input("Seleccione la mascota (número): ")) - 1
        mascota = mascotas[indice]
        print(mascota.mostrar_historial())
    except (IndexError, ValueError):
        print("Selección inválida.")


# 🧭 MENÚ PRINCIPAL
def menu():
    while True:
        print("\n=== Clínica Veterinaria 'Amigos Peludos' ===")
        print("1. Registrar Mascota")
        print("2. Registrar Consulta")
        print("3. Listar Mascotas")
        print("4. Ver Historial de Consultas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_mascota()
        elif opcion == "2":
            registrar_consulta()
        elif opcion == "3":
            listar_mascotas()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Ejecutar menú principal
menu()
