class Producto:
    """
    Representa un producto del restaurante.

    Principio SRP:
    Esta clase únicamente administra la información del producto.
    """
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:

        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

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
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = valor

    def convertir_a_diccionario(self) -> dict:
        """
        Convertir el objeto Producto a un dicionario compatible con JSON
        """
        return{
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            }

    def __str__(self) -> str:
            return (
                f"Codigo: {self.codigo} | "
                f"Nombre: {self.nombre} | "
                f"Categoria: {self.categoria} | "
                f"Precio: ${self.precio:.2f}"
            )