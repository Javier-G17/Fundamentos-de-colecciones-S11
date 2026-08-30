from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class Restaurante:
    """
    Servicio principal encargado de administrar
    productos, usuarios y ventas.
    """

    def __init__(
        self,
        productos_iniciales: list[Producto] | None = None,
        usuarios_iniciales: list[Usuario] | None = None,
        ventas_iniciales: list[Venta] | None = None,
    ) -> None:

        self._productos: list[Producto] = (productos_iniciales.copy() if productos_iniciales else [])

        self._usuarios: list[Usuario] = (usuarios_iniciales.copy() if usuarios_iniciales else [])

        self._ventas: list[Venta] = (ventas_iniciales.copy() if ventas_iniciales else [])

    # ==================================
    # PRODUCTOS
    # ==================================

    def registrar_producto(self, producto: Producto) -> bool:

        if self.buscar_producto(producto.codigo) is not None:
            return False

        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:

        codigo = codigo.strip()

        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def actualizar_producto(
        self,
        codigo: str,
        nuevo_nombre: str,
        nueva_categoria: str,
        nuevo_precio: float,
        nuevo_stock: int,
    ) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        producto.nombre = nuevo_nombre
        producto.categoria = nueva_categoria
        producto.precio = nuevo_precio
        producto.stock = nuevo_stock

        return True

    def eliminar_producto(self, codigo: str) -> bool:

        producto = self.buscar_producto(codigo)

        if producto is None:
            return False

        self._productos.remove(producto)
        return True

    def listar_productos(self) -> list[Producto]:

        return self._productos.copy()

    def contar_productos(self) -> int:

        return len(self._productos)

    # ==================================
    # USUARIOS
    # ==================================

    def registrar_usuario(self, usuario: Usuario) -> bool:

        if self.buscar_usuario(usuario.identificacion) is not None:
            return False

        self._usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:

        identificacion = identificacion.strip()

        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def listar_usuarios(self) -> list[Usuario]:

        return self._usuarios.copy()

    # ==================================
    # VENTAS
    # ==================================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int
    ) -> bool:

        usuario = self.buscar_usuario(identificacion_usuario)

        producto = self.buscar_producto(codigo_producto)

        if usuario is None:
            return False

        if producto is None:
            return False

        if cantidad <= 0:
            return False

        if producto.stock < cantidad:
            return False

        venta = Venta(
            usuario.identificacion,
            producto.codigo,
            cantidad
        )

        self._ventas.append(venta)

        producto.vender(cantidad)

        return True

    def listar_ventas(self) -> list[Venta]:

        return self._ventas.copy()

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> list[Venta]:

        ventas_usuario: list[Venta] = []

        for venta in self._ventas:

            if (venta.usuario_id == identificacion_usuario.strip()):
                ventas_usuario.append(venta)

        return ventas_usuario

    # ==================================
    # CATEGORIAS
    # ==================================

    def obtener_categorias_unicas(self) -> set[str]:

        categorias: set[str] = set()

        for producto in self._productos:
            categorias.add(producto.categoria)

        return categorias

    def existe_categoria(self,categoria: str) -> bool:

        return (categoria.strip()
            in self.obtener_categorias_unicas()
        )