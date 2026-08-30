# Restaurante App - Semana 11

## Datos del estudiante

**Nombre**: Bonner Javier García Guanga

---

# Descripción del sistema

Restaurante App es una aplicación desarrollada en Python utilizando Programación Orientada a Objetos (POO). El sistema permite administrar productos y usuarios de un restaurante, así como registrar ventas realizadas por los usuarios.

La aplicación utiliza archivos JSON para almacenar la información de forma persistente, permitiendo conservar los datos incluso después de cerrar el programa. Al iniciar nuevamente la aplicación, los registros almacenados son recuperados y convertidos nuevamente en objetos para continuar trabajando con la lógica orientada a objetos.

---

## Estructura del proyecto
```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── _init_.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── _init_.py
│   ├── archivo_servicio.py
│   └── restaurante.py
│
├── main.py
└── README.md
``` 
---

## Responsabilidad de los componentes

**modelos/producto.py**: Representa los productos del restaurante. Contiene la información del código, nombre, categoría, precio y stock disponible. También incluye validaciones para evitar datos incorrectos y métodos para convertir los objetos en diccionarios compatibles con JSON.

**modelos/usuario.py**: Representa a los usuarios registrados en el sistema. Contiene la identificación, nombre y correo electrónico, además de las validaciones correspondientes.

**modelos/venta.py**: Representa una venta realizada dentro del restaurante. Relaciona a un usuario con un producto y registra la cantidad vendida.

**servicios/restaurante.py**: Administra las colecciones de productos, usuarios y ventas. Contiene las reglas de negocio para registrar, buscar, actualizar, eliminar y vender productos.

**servicios/archivo_servicio.py**: Se encarga de la persistencia de datos. Permite guardar y recuperar productos, usuarios y ventas mediante archivos JSON.

**main.py**: Es el punto de entrada de la aplicación. Coordina el menú interactivo y la comunicación entre el usuario y los servicios del sistema.

---

## Funcionamiento del stock

Cada producto posee un atributo llamado stock, que representa la cantidad disponible para la venta.

Antes de registrar una venta, el sistema verifica:

- Que el producto exista.
- Que el usuario exista.
- Que la cantidad solicitada sea mayor que cero.
- Que exista stock suficiente.

Si la venta es válida, el stock del producto disminuye automáticamente según la cantidad vendida.

Ejemplo:

Stock inicial: 10 unidades

Venta realizada: 3 unidades

Stock final: 7 unidades

El sistema impide que el stock llegue a valores negativos.

---

## Relación Usuario – Producto mediante Venta

La principal mejora de la Semana 11 consiste en la incorporación de la entidad Venta, que permite relacionar usuarios con productos.

```text 
Flujo de la venta:

Usuario registrado

↓

Producto existente

↓

Validación de stock

↓

Creación de objeto Venta

↓

Registro en colección de ventas

↓

Descuento de stock

↓

Guardado en archivos JSON
```

Cada venta almacena:

- Identificación del usuario.
- Código del producto.
- Cantidad vendida.

De esta manera es posible consultar posteriormente todas las ventas realizadas por un usuario específico.

---

## Persistencia de datos

La aplicación utiliza archivos JSON para conservar la información.

**productos.json**: Almacena los productos registrados junto con su stock actualizado.

**usuarios.json**: Almacena los usuarios registrados.

**ventas.json**: Almacena todas las ventas realizadas.

Proceso de guardado:

```text
Objetos Python

↓

Conversión a diccionarios

↓

json.dump()

↓

Archivo JSON

Proceso de carga:

Archivo JSON

↓

json.load()

↓

Diccionarios

↓

Reconstrucción de objetos

↓

Colecciones del sistema
```
---

## Excepciones controladas

El sistema controla diferentes situaciones que pueden producir errores durante la ejecución:

**FileNotFoundError**: Permite iniciar la aplicación aunque el archivo JSON todavía no exista.

**JSONDecodeError**: Controla archivos con formato JSON inválido.

**PermissionError**: Controla problemas de permisos de lectura o escritura.

**KeyError**: Controla registros JSON incompletos o con claves faltantes.

**ValueError**: Controla datos inválidos ingresados por el usuario o valores incorrectos dentro de los modelos.

Estas excepciones permiten que la aplicación continúe funcionando sin finalizar de manera inesperada.

---

## Forma de ejecución

1. Abrir el proyecto en Visual Studio Code.
2. Verificar que la estructura de carpetas sea correcta.
3. Ejecutar el archivo: main.py
4. Utilizar el menú interactivo para gestionar productos, usuarios y ventas.

---

## Pruebas realizadas

Para verificar el correcto funcionamiento del sistema se realizaron las siguientes pruebas:

1. Registro de usuarios.
2. Registro de productos con stock disponible.
3. Búsqueda de productos registrados.
4. Actualización de productos.
5. Eliminación de productos.
6. Registro de ventas.
7. Verificación de disminución de stock después de una venta.
8. Consulta de ventas por usuario.
9. Verificación de creación automática de los archivos JSON.
10. Cierre y reapertura de la aplicación para comprobar la persistencia.
11. Recuperación correcta de productos, usuarios y ventas almacenados.
12. Intento de venta con stock insuficiente para comprobar que la operación sea rechazada.
13. Verificación de que los datos permanecen consistentes después de reiniciar el sistema.

---

## Conclusión

La implementación de la Semana 11 permitió ampliar el sistema mediante la incorporación de relaciones entre objetos utilizando la clase Venta. Además, se fortaleció el manejo de persistencia mediante archivos JSON para productos, usuarios y ventas, manteniendo una arquitectura modular basada en Programación Orientada a Objetos y aplicando buenas prácticas de validación y manejo de excepciones.