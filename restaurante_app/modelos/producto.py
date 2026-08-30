class Producto:
    """
    Representa un producto del restaurante.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int = 0
    ) -> None:

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El codigo no puede estar vacio.")

        self._codigo = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacio.")

        self._nombre = valor.strip()

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La categoria no puede estar vacia.")

        self._categoria = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        try:
            precio = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser numerico.")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")

        self._precio = precio

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int) -> None:

        try:
            stock = int(valor)

        except (TypeError, ValueError):
            raise ValueError("El stock debe ser un numero entero.")

        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")

        self._stock = stock

    @property
    def estado(self) -> str:

        if self.stock > 0:
            return f"Stock disponible: {self.stock}"

        return "Sin stock"

    def vender(self, cantidad: int = 1) -> bool:
        """
        Disminuye el stock cuando se realiza una venta.
        """

        if cantidad <= 0:
            return False

        if self.stock < cantidad:
            return False

        self.stock -= cantidad
        return True

    def convertir_a_diccionario(self) -> dict:
        """
        Convierte el producto en un diccionario
        compatible con JSON.
        """

        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    def __str__(self) -> str:
        return (
            f"Codigo: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoria: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Estado: {self.estado}"
        )