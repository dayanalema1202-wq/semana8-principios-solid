from modelos.producto import Producto


class Bebida(Producto):

    SERVICIOS_VALIDOS = ("frio", "caliente", "natural", "con hielo", "tibio")

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        cantidad: str,
        tipo_servicio: str,
    ) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.cantidad = self._validar_texto(cantidad, "La cantidad no puede estar vacia.")
        self.tipo_servicio = self._validar_tipo_servicio(tipo_servicio)

    @staticmethod
    def _validar_tipo_servicio(tipo_servicio: str) -> str:
        tipo_limpio = tipo_servicio.strip().lower()
        if not tipo_limpio:
            raise ValueError("El tipo de servicio no puede estar vacio.")
        servicios_validos = ("frio", "caliente", "natural", "con hielo", "tibio")
        if tipo_limpio not in servicios_validos:
            opciones = ", ".join(servicios_validos)
            raise ValueError(f"Tipo de servicio no reconocido. Opciones: {opciones}.")
        return tipo_limpio.capitalize()

    def mostrar_informacion(self) -> str:
        return (
            f"{super().mostrar_informacion()} | "
            f"Cantidad: {self.cantidad} | "
            f"Tipo de servicio: {self.tipo_servicio}"
        )
