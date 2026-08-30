from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante

OPCIONES_MENU = (
    ("1", "Registrar producto"),
    ("2", "Buscar producto"),
    ("3", "Actualizar producto"),
    ("4", "Eliminar producto"),
    ("5", "Listar productos"),
    ("6", "Registrar usuario"),
    ("7", "Listar usuarios"),
    ("8", "Vender producto"),
    ("9", "Consultar ventas por usuario"),
    ("0", "Salir"),
)


def pedir_texto(mensaje: str) -> str:
    return input(mensaje).strip()


def pedir_entero(mensaje: str) -> int:
    return int(input(mensaje).strip())


def pedir_float(mensaje: str) -> float:
    return float(input(mensaje).strip())


def mostrar_menu() -> None:
    print("\n===== RESTAURANTE APP =====")

    for numero, descripcion in OPCIONES_MENU:
        print(f"{numero}. {descripcion}")


def guardar_productos(
    archivo_servicio: ArchivoServicio,
    restaurante: Restaurante,
) -> None:

    archivo_servicio.guardar_productos(
        restaurante.listar_productos()
    )


def guardar_usuarios(
    archivo_servicio: ArchivoServicio,
    restaurante: Restaurante,
) -> None:

    archivo_servicio.guardar_usuarios(
        restaurante.listar_usuarios()
    )


def guardar_ventas(
    archivo_servicio: ArchivoServicio,
    restaurante: Restaurante,
) -> None:

    archivo_servicio.guardar_ventas(
        restaurante.listar_ventas()
    )


def registrar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio,
) -> None:

    print("\n--- Registrar producto ---")

    try:
        codigo = pedir_texto("Código: ")
        nombre = pedir_texto("Nombre: ")
        categoria = pedir_texto("Categoría: ")
        precio = pedir_float("Precio: ")
        stock = pedir_entero("Stock: ")

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        if restaurante.registrar_producto(producto):
            guardar_productos(
                archivo_servicio,
                restaurante
            )
            print("Producto registrado correctamente.")
        else:
            print("Ya existe un producto con ese código.")

    except ValueError as error:
        print(error)


def buscar_producto(
    restaurante: Restaurante,
) -> None:

    print("\n--- Buscar producto ---")

    codigo = pedir_texto(
        "Código del producto: "
    )

    producto = restaurante.buscar_producto(
        codigo
    )

    if producto is None:
        print("Producto no encontrado.")
    else:
        print(producto)


def actualizar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio,
) -> None:

    print("\n--- Actualizar producto ---")

    codigo = pedir_texto("Código del producto: ")

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    try:
        nuevo_nombre = pedir_texto("Nuevo nombre: ")

        nueva_categoria = pedir_texto("Nueva categoría: ")

        nuevo_precio = pedir_float("Nuevo precio: ")

        nuevo_stock = pedir_entero("Nuevo stock: ")

        actualizado = (restaurante.actualizar_producto(
                codigo,
                nuevo_nombre,
                nueva_categoria,
                nuevo_precio,
                nuevo_stock
            )
        )

        if actualizado:
            guardar_productos(
                archivo_servicio,
                restaurante
            )
            print("Producto actualizado correctamente.")
        else:
            print("No fue posible actualizar.")

    except ValueError as error:
        print(error)


def eliminar_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio,
) -> None:

    print("\n--- Eliminar producto ---")

    codigo = pedir_texto(
        "Código del producto: "
    )

    if restaurante.eliminar_producto(codigo):
        guardar_productos(
            archivo_servicio,
            restaurante
        )
        print("Producto eliminado.")
    else:
        print("Producto no encontrado.")


def listar_productos(
    restaurante: Restaurante,
) -> None:

    print("\n--- Lista de productos ---")

    productos = (
        restaurante.listar_productos()
    )

    if len(productos) == 0:
        print("No existen productos registrados.")
        return

    for producto in productos:
        print(producto)


def registrar_usuario(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio,
) -> None:

    print("\n--- Registrar usuario ---")

    try:
        identificacion = pedir_texto("Identificación: ")

        nombre = pedir_texto("Nombre: ")

        correo = pedir_texto("Correo: ")

        usuario = Usuario(
            identificacion,
            nombre,
            correo
        )

        if restaurante.registrar_usuario(
            usuario
        ):
            guardar_usuarios(
                archivo_servicio,
                restaurante
            )
            print("Usuario registrado correctamente.")
        else:
            print("La identificación ya existe.")

    except ValueError as error:
        print(error)


def listar_usuarios(
    restaurante: Restaurante,
) -> None:

    print("\n--- Lista de usuarios ---")

    usuarios = restaurante.listar_usuarios()

    if len(usuarios) == 0:
        print("No existen usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)


def vender_producto(
    restaurante: Restaurante,
    archivo_servicio: ArchivoServicio,
) -> None:

    print("\n--- Vender producto ---")

    codigo_producto = pedir_texto("Código del producto: ")

    identificacion_usuario = pedir_texto("Identificación del usuario: ")

    try:
        cantidad = pedir_entero("Cantidad: ")

        vendido = restaurante.vender_producto(
            codigo_producto,
            identificacion_usuario,
            cantidad
        )

        if vendido:
            guardar_ventas(
                archivo_servicio,
                restaurante
            )

            guardar_productos(
                archivo_servicio,
                restaurante
            )

            print("Venta registrada correctamente.")
        else:
            print("No fue posible realizar la venta.")

    except ValueError as error:
        print(error)


def consultar_ventas_usuario(restaurante: Restaurante,) -> None:

    print("\n--- Ventas por usuario ---")

    identificacion = pedir_texto("Identificación: ")

    ventas = (restaurante.consultar_ventas_usuario(identificacion))

    if len(ventas) == 0:
        print("El usuario no tiene ventas.")
        return

    for venta in ventas:
        print(venta)


def ejecutar_menu() -> None:

    ruta_datos = (
        Path(__file__).resolve().parent
        / "datos"
    )

    archivo_servicio = ArchivoServicio(str(ruta_datos))

    restaurante = Restaurante(
        archivo_servicio.cargar_productos(),
        archivo_servicio.cargar_usuarios(),
        archivo_servicio.cargar_ventas()
    )

    opciones = {
        "1": lambda: registrar_producto(restaurante, archivo_servicio),
        "2": lambda: buscar_producto(restaurante),
        "3": lambda: actualizar_producto(restaurante, archivo_servicio),
        "4": lambda: eliminar_producto(restaurante,
            archivo_servicio),
        "5": lambda: listar_productos(restaurante),
        "6": lambda: registrar_usuario(restaurante, archivo_servicio),
        "7": lambda: listar_usuarios(restaurante),
        "8": lambda: vender_producto(restaurante, archivo_servicio),
        "9": lambda: consultar_ventas_usuario(restaurante),
    }

    while True:

        mostrar_menu()

        opcion = pedir_texto("Seleccione una opción: ")

        if opcion == "0":
            print("Gracias por usar Restaurante App.")
            break

        accion = opciones.get(opcion)

        if accion is None:
            print("Opción inválida.")
        else:
            accion()



if __name__ == "__main__":
    ejecutar_menu()