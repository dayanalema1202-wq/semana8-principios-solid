# POO Semana 8

**Estudiante:** Dayana Valeria Lema Saldaña  
**Asignatura:** Programación Orientada a Objetos 

---

## Descripción del sistema

Aplicación orientada a objetos en Python para la gestión de un restaurante. El precio de los productos no puede tener más de dos decimales. Las bebidas se clasifican por tipo de servicio, que debe ser uno de los valores reconocidos: frío, caliente, natural, con hielo o tibio. El correo del cliente no puede contener más de un símbolo `@`.

---

## Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
README.md
```

---

## Responsabilidad de cada clase

| Clase / Archivo | Responsabilidad |
|---|---|
| `Producto` | Clase base con codigo, nombre, categoria y precio. El precio no puede tener más de dos decimales. |
| `Bebida` | Extiende `Producto` con cantidad y tipo de servicio. El tipo de servicio debe pertenecer a los valores predefinidos. |
| `Cliente` | Entidad con identificacion, nombre y correo. El correo no puede contener más de un arroba. |
| `Restaurante` | Administra las colecciones de productos y clientes, registra objetos y controla duplicados. |
| `main.py` | Punto de entrada. Muestra los valores válidos de tipo de servicio antes de solicitar el dato. |

---

## Relación entre Producto y Bebida

`Bebida` hereda de `Producto` porque una bebida es un tipo de producto en el restaurante. La herencia permite almacenar ambos en la misma lista `_productos` y llamar a `mostrar_informacion()` de forma uniforme. Cada objeto responde con sus propios datos sin que el servicio necesite distinguir el tipo concreto.

---

## Principios SOLID aplicados

### SResponsabilidad única (SRP)

Cada componente tiene una tarea definida. Los modelos representan entidades y validan sus atributos. El servicio centraliza las operaciones sobre las colecciones. `main.py` gestiona la interacción por consola e informa al usuario qué valores son aceptados. Si se modifica la lista de tipos de servicio válidos, solo cambia `Bebida`.

### Abierto/Cerrado (OCP)

`Bebida` amplía el sistema con `cantidad` y `tipo_servicio` sin modificar `Producto`. El diseño permite incorporar nuevas especializaciones heredando de `Producto` sin que el servicio ni el menú deban cambiar para aceptarlas.

### Sustitución de Liskov (LSP)

Un objeto `Bebida` puede usarse en cualquier lugar donde se espera un `Producto`. El servicio registra y lista ambos tipos de forma uniforme. El método `mostrar_informacion()` se llama sin condiciones adicionales y cada objeto responde correctamente según su implementación.


## Reflexión

Un sistema bien estructurado comunica sus intenciones con claridad. Separar cada responsabilidad en su propio componente reduce la cantidad de cosas que hay que entender al mismo tiempo y facilita encontrar dónde hacer un cambio cuando el proyecto evoluciona. Aprender a diseñar así desde los primeros proyectos es una inversión que se nota en cada línea de código que se escribe después.
