

# SISTEMA DE ASIENTOS DE CINE - Matrices

# Crear matriz de asientos
def crear_sala():
    print("CREACIÓN DE SALA DE CINE")

    while True:
        try:
            filas = int(input("Número de filas: "))
            columnas = int(input("Número de columnas por fila: "))
            break
        except ValueError:
            print("Por favor ingresa números válidos.")

    sala = [["L" for _ in range(columnas)] for _ in range(filas)]
    print("\n✅ Sala creada exitosamente.\n")

    return sala, filas, columnas


# Mostrar sala completa
def mostrar_sala(sala):
    print("\n ESTADO DE LA SALA\n")
    for fila in sala:
        print(" ".join(fila))
    print()


# Reservar asiento
def reservar_asiento(sala, filas, columnas):
    print("\n RESERVAR ASIENTO")

    try:
        f = int(input("Fila: "))
        c = int(input("Columna: "))
    except ValueError:
        print("Debes ingresar números enteros.\n")
        return

    # Validar rango
    if f < 0 or f >= filas or c < 0 or c >= columnas:
        print("❌ Ese asiento no existe.\n")
        return

    # Verificar disponibilidad
    if sala[f][c] == "L":
        sala[f][c] = "X"
        print("n✅ Asiento reservado con éxito.\n")
    else:
        print("❌ Ese asiento ya está ocupado.\n")


# Liberar asiento
def liberar_asiento(sala, filas, columnas):
    print("\n LIBERAR ASIENTO")

    try:
        f = int(input("Fila: "))
        c = int(input("Columna: "))
    except ValueError:
        print("Debes ingresar números enteros.\n")
        return

    if f < 0 or f >= filas or c < 0 or c >= columnas:
        print("❌ Ese asiento no existe.\n")
        return

    if sala[f][c] == "X":
        sala[f][c] = "L"
        print("n✅ Asiento liberado con éxito.\n")
    else:
        print("❌ Ese asiento ya estaba libre.\n")


# Contar asientos libres y ocupados
def contar_asientos(sala):
    libres = 0
    ocupados = 0

    for fila in sala:
        for asiento in fila:
            if asiento == "L":
                libres += 1
            else:
                ocupados += 1

    print("\n ESTADÍSTICAS")
    print(f"Asientos libres: {libres}")
    print(f"Asientos ocupados: {ocupados}\n")


# ----------------------------------------------
# PROGRAMA PRINCIPAL

sala, filas, columnas = crear_sala()

while True:
    print("🎬 MENÚ DEL CINE")
    print("1. 🍿 Mostrar sala")
    print("2. 🎫 Reservar asiento")
    print("3. 📽️ Liberar asiento")
    print("4. 🎞️ Contar asientos")
    print("5. 🎬 Salir")

    opcion = input("✨ Elige una opción: ")

    if opcion == "1":
        mostrar_sala(sala)
    elif opcion == "2":
        reservar_asiento(sala, filas, columnas)
    elif opcion == "3":
        liberar_asiento(sala, filas, columnas)
    elif opcion == "4":
        contar_asientos(sala)
    elif opcion == "5":
        print("\n✔ Gracias por usar el sistema de cine. ¡Disfruta la función!\n")
        break
    else:
        print("❌ Opción inválida, intenta de nuevo.\n")
