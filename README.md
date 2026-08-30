# Restaurante App – Semana 10

## Estudiante

Bonner Javier García Guanga

## Descripción del proyecto

Restaurante App es una aplicación desarrollada en Python utilizando Programación Orientada a Objetos (POO), estructuras de datos y persistencia mediante archivos JSON.

El sistema permite administrar productos y usuarios de un restaurante a través de un menú interactivo ejecutado desde consola. Como mejora de la Semana 10, se incorporó el almacenamiento permanente de productos utilizando un archivo JSON, permitiendo conservar la información incluso después de cerrar la aplicación.

---

## Estructura del proyecto
```text
restaurante_app/
├── datos/
│   └── productos.json
├── modelos/
│   ├── _init_.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── _init_.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
``` 
---

## Responsabilidad de los archivos

modelos/producto.py

Contiene la clase "Producto", encargada de representar la información de cada producto del restaurante.

Atributos:

- Código
- Nombre
- Categoría
- Precio

Además incorpora validaciones mediante propiedades y el método "a_diccionario()", utilizado para convertir el objeto a un formato compatible con JSON.

modelos/usuario.py

Contiene la clase "Usuario", utilizada para representar personas registradas dentro del sistema.

Atributos:

- Identificación
- Nombre
- Correo

Los usuarios permanecen únicamente en memoria durante esta actividad.

servicios/restaurante.py

Administra todas las operaciones relacionadas con los productos y usuarios:

- Registrar productos
- Buscar productos
- Actualizar productos
- Eliminar productos
- Listar productos
- Registrar usuarios
- Buscar usuarios
- Listar usuarios
- Obtener categorías únicas

servicios/archivo_servicio.py

Administra la persistencia de productos mediante JSON.

Funciones principales:

- Cargar productos desde JSON
- Reconstruir objetos Producto
- Guardar productos en JSON

main.py

Coordina la interacción con el usuario.

Responsabilidades:

- Mostrar el menú.
- Solicitar datos.
- Crear objetos.
- Utilizar los servicios.
- Cargar productos al iniciar.
- Guardar productos cuando existan cambios.

---

## Estructuras de datos utilizadas

Listas (list)

Se utilizan para almacenar colecciones dinámicas:

self._productos: list[Producto] = []
self._usuarios: list[Usuario] = []

Permiten registrar, buscar, actualizar, eliminar y listar información.

Tupla (tuple)

Se utiliza para almacenar las opciones fijas del menú.

OPCIONES_MENU = (
    ("1", "Registrar producto"),
    ("2", "Buscar producto"),
)

Diccionario (dict)

Permite asociar opciones del menú con funciones.

opciones = {
    "1": registrar_producto,
    "2": buscar_producto,
}

Conjunto (set)

Se utiliza para mostrar categorías únicas de productos.

categorias: set[str] = set()

---

## Persistencia de datos con JSON

Archivo utilizado

datos/productos.json

Guardado de productos

Cuando se registra, actualiza o elimina un producto:

1. El servicio Restaurante modifica la colección.
2. Los objetos Producto se convierten en diccionarios.
3. ArchivoServicio utiliza "json.dump()".
4. Se actualiza automáticamente el archivo JSON.

Carga de productos

Cuando el programa inicia:

1. ArchivoServicio intenta abrir el archivo JSON.
2. Se utiliza "json.load()".
3. Cada registro se convierte nuevamente en un objeto Producto.
4. Los objetos son entregados a Restaurante.

---

## Manejo de excepciones

El sistema controla diferentes situaciones para evitar que la aplicación se detenga inesperadamente.

FileNotFoundError

Permite iniciar el sistema aunque el archivo JSON aún no exista.

JSONDecodeError

Controla archivos JSON con contenido inválido.

PermissionError

Controla problemas de permisos de lectura o escritura.

KeyError

Controla registros incompletos al reconstruir objetos.

ValueError

Controla datos inválidos durante la creación o actualización de productos y usuarios.

---
```text
Flujo de carga

Inicio del programa
        ↓
Creación de ArchivoServicio
        ↓
Lectura de productos.json
        ↓
json.load()
        ↓
Reconstrucción de objetos Producto
        ↓
Carga en Restaurante
        ↓
Funcionamiento normal del sistema
```
---

Flujo de guardado
```text
Registrar / Actualizar / Eliminar producto
                ↓
Restaurante modifica la colección
                ↓
Conversión a diccionarios
                ↓
json.dump()
                ↓
Actualización de productos.json
```
---

## Funcionalidades implementadas

Productos

- Registrar producto.
- Buscar producto.
- Actualizar producto.
- Eliminar producto.
- Listar productos.
- Persistencia mediante JSON.

Usuarios

- Registrar usuario.
- Listar usuarios.

Categorías

- Mostrar categorías únicas.

---

## Encapsulamiento

Las clases utilizan atributos protegidos:

self._codigo
self._nombre
self._categoria
self._precio

El acceso a estos atributos se realiza mediante propiedades ("@property") y métodos setter, permitiendo aplicar validaciones antes de modificar los datos.

---

## Comprobación de persistencia

Prueba realizada:

1. Ejecutar el programa.
2. Registrar productos.
3. Verificar la creación del archivo JSON.
4. Cerrar el programa.
5. Ejecutarlo nuevamente.
6. Listar productos.
7. Confirmar que los datos se recuperan correctamente.
8. Actualizar o eliminar productos.
9. Reiniciar y verificar que los cambios se conservan.

---

## Ejecución del proyecto

Ubicarse en la carpeta principal del proyecto y ejecutar:

python main.py

---

## Conclusión

Durante esta práctica se incorporó persistencia de datos mediante archivos JSON, permitiendo conservar la información de los productos entre ejecuciones del programa. Además de reforzar los conceptos de Programación Orientada a Objetos, se aplicaron estructuras de datos, manejo de excepciones y separación de responsabilidades mediante una arquitectura modular basada en modelos, servicios y punto de entrada principal.