from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    def __init__(self, productos_iniciales: list[Producto] | None = None) -> None:
        self._productos: list[Producto] = productos_iniciales.copy() if productos_iniciales else []
        self._usuarios: list[Usuario] = []
        self._prestamos: dict[str, str] = {}

    def cargar_productos(self, productos: list[Producto]) -> None:
        self._productos = productos.copy()
        self._prestamos.clear()

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
    ) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False

        producto.nombre = nuevo_nombre
        producto.categoria = nueva_categoria
        producto.precio = nuevo_precio
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

    def actualizar_usuario(self, identificacion: str, nuevo_nombre: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False

        usuario.nombre = nuevo_nombre
        return True

    def eliminar_usuario(self, identificacion: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
        if identificacion.strip() in self._prestamos.values():
            return False

        self._usuarios.remove(usuario)
        return True

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    def obtener_categorias_unicas(self) -> set[str]:
        categorias: set[str] = set()
        for producto in self._productos:
            categorias.add(producto.categoria)
        return categorias

    def existe_categoria(self, categoria: str) -> bool:
        return categoria.strip() in self.obtener_categorias_unicas()