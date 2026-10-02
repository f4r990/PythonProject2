class Descuento:
    def aplicar(self, precio):
        return precio
class DescuentoVIP(Descuento):
    def aplicar(self, precio):
        return precio * 0.8