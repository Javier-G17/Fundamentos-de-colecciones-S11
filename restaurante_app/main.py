
from modelos.producto import Producto
from modelos.usuario import Usuario 
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
from pathlib import Path

# Tupla utilizada para almacenar las opciones fijas del menú.
OPCIONES_MENU = (
    ("1", "Registrar producto"),
    ("2", "Buscar producto"),
    ("3", "Actualizar producto"),
    ("4", "Eliminar producto"),
    ("5", "Listar productos"),
    ("6", "Registrar usuario"),
    ("7", "Listar usuarios"),
    ("8", "Listar categorias unicas"),
    ("0", "Salir"),
)


def pedir_texto(mensaje: str) -> str:
    return input(mensaje).strip()


def mostrar_menu() -> None:
    print("\n===== RESTAURANTE APP =====")

    for numero, descripcion in OPCIONES_MENU:
        print(f"{numero}. {descripcion}")


def registrar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:

    print("\n--- Registrar producto ---")

    codigo = pedir_texto("Codigo: ")
    nombre = pedir_texto("Nombre: ")
    categoria = pedir_texto("Categoria: ")
    precio = float(pedir_texto("Precio: "))
   
    try:
        
        producto = Producto(codigo, nombre, categoria, precio)

        registrado = restaurante.registrar_producto(producto)
        if registrado:

            archivo_servicio.guardar_productos(restaurante.listar_productos())

            print("Producto registrado correctamente.")

        else:
            print("El codigo ya se encuentra registrado.")

    except ValueError as error:
        print(error)

def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- Buscar producto ---")

    codigo = pedir_texto("Codigo del producto: ")

    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print(producto)

def actualizar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:

    print("\n--- Actualizar producto ---")

    codigo = pedir_texto("Codigo del producto: ")

    if (restaurante.buscar_producto(codigo)is None):
        print("Producto no encontrado.")
        return

    nuevo_nombre = pedir_texto("Nuevo nombre: ")
    nueva_categoria = pedir_texto("Nueva categoria: ")
    nuevo_precio = float(pedir_texto("Nuevo precio: "))
    try:
        actualizado = restaurante.actualizar_producto(
                codigo,
                nuevo_nombre,
                nueva_categoria,
                nuevo_precio,
            )

        if actualizado:
            archivo_servicio.guardar_productos(restaurante.listar_productos())
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    except ValueError as error:
        print(error)


def eliminar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:

    print("\n--- Eliminar producto ---")

    codigo = pedir_texto("Codigo del producto: ")

    eliminado = restaurante.eliminar_producto(codigo)

    if eliminado:
        archivo_servicio.guardar_productos(restaurante.listar_productos())
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


def listar_productos(restaurante: Restaurante) -> None:

    print("\n--- Lista de productos ---")

    productos = (restaurante.listar_productos())

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    for indice, producto in enumerate(productos):
        print(f"{indice + 1}. {producto}")

    primer_producto = productos[0]

    print(f"\nPrimer producto registrado: " f"{primer_producto.nombre}"
    )

    print(f"Total de productos: "f"{restaurante.contar_productos()}")


def registrar_usuario(restaurante: Restaurante) -> None:
    
    print("\n--- Registrar usuario ---")

    identificacion = pedir_texto("Identificacion: ")

    nombre = pedir_texto("Nombre: ")

    correo = pedir_texto("Correo: ")

    try:
        usuario = Usuario(
            identificacion,
            nombre,
            correo,
        )

        registrado = restaurante.registrar_usuario(usuario)

        if registrado:
            print("Usuario registrado correctamente.")
        else:
            print("La identificacion ya se encuentra registrada.")

    except ValueError as error:
        print(error)


def listar_usuarios(restaurante: Restaurante) -> None:

    print("\n--- Lista de usuarios ---")

    usuarios = restaurante.listar_usuarios()

    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return

    for indice, usuario in enumerate(usuarios):
        print(f"{indice + 1}. {usuario}")


def listar_categorias_unicas(restaurante: Restaurante) -> None:

    print("\n--- Categorias unicas ---")

    categorias = restaurante.obtener_categorias_unicas()

    if len(categorias) == 0:
        print("No hay categorias registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")

    categoria_consultada = pedir_texto("\nConsultar categoria (Enter para omitir): ")

    if categoria_consultada:
        if (categoria_consultada in categorias):
            print("La categoria existe.")
        else:
            print("La categoria no existe.")


def ejecutar_menu() -> None:
    ruta_productos = Path(__file__).resolve().parent / "datos" / "productos.json"
    archivo_servicio = ArchivoServicio(str(ruta_productos))
    restaurante = Restaurante(archivo_servicio.cargar_productos())



    # Diccionario que relaciona cada opción del menú, con la funcion que debe ejecutarse
    opciones = {
        "1": lambda r: registrar_producto(r, archivo_servicio),
        "2": buscar_producto,
        "3": lambda r: actualizar_producto(r, archivo_servicio),
        "4": lambda r: eliminar_producto(r, archivo_servicio),
        "5": listar_productos,
        "6": registrar_usuario,
        "7": listar_usuarios,
        "8": listar_categorias_unicas,
    }

    print("Opciones disponibles:", ", ".join(opciones.keys()), "y 0 para salir.")

    while True:
        mostrar_menu()

        opcion = pedir_texto("Seleccione una opcion: ")

        if opcion == "0":
            print("Gracias por usar Restaurante App.")
            break

        accion = opciones.get(opcion)

        if accion is None:
            print("Opcion invalida.")
        else:
            accion(restaurante)
    


if __name__ == "__main__":
    ejecutar_menu()