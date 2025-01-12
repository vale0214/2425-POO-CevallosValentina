# Class Producto
class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        """
        Clase que representa un producto en la tienda.
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        """
        Actualiza el stock del producto sumando o restando una cantidad.
        """
        self.stock += cantidad

    def __str__(self):
        """Devuelve una representación en texto del producto."""
        return f"Producto[{self.id_producto}] - {self.nombre}: ${self.precio} (Stock: {self.stock})"


# Class Cliente
class Cliente:
    def __init__(self, id_cliente, nombre):
        """
        Clase que representa a un cliente de la tienda.
        """
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.pedidos = []  # Lista de pedidos realizados por el cliente

    def realizar_pedido(self, pedido):
        """
        Añade un pedido a la lista de pedidos del cliente.
        """
        self.pedidos.append(pedido)

    def __str__(self):
        """Devuelve una representación en texto del cliente."""
        return f"Cliente[{self.id_cliente}] - {self.nombre}"


# Class Pedido
class Pedido:
    def __init__(self, id_pedido, cliente):
        """
        Clase que representa un pedido realizado por un cliente.
        """
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.productos = []  # Lista de productos en el pedido

    def agregar_producto(self, producto, cantidad):
        """
        Añade un producto y su cantidad al pedido, actualizando el stock del producto.
        """
        if producto.stock >= cantidad:
            self.productos.append((producto, cantidad))
            producto.actualizar_stock(-cantidad)  # Reduce el stock del producto
        else:
            print(f"No hay suficiente stock para {producto.nombre}. Disponible: {producto.stock}")

    def calcular_total(self):
        """Calcula el costo total del pedido sumando los precios de los productos."""
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos)
        return total

    def __str__(self):
        """Devuelve una representación en texto del pedido."""
        detalles = [f"{producto.nombre} x{cantidad} (${producto.precio * cantidad})" for producto, cantidad in self.productos]
        return f"Pedido[{self.id_pedido}] - Cliente: {self.cliente.nombre}\nProductos:\n" + "\n".join(detalles) + f"\nTotal: ${self.calcular_total()}"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear algunos productos
    producto1 = Producto(1, "Pantalon", 99.00, 10)
    producto2 = Producto(2, "Blusa", 35.00, 100)
    producto3 = Producto(3, "Zapatos", 150.00, 20)

    # Crear un cliente
    cliente1 = Cliente(1, "Valentina Cevallos")

    # Crear un pedido
    pedido1 = Pedido(20, cliente1)

    # Agregar productos al pedido
    pedido1.agregar_producto(producto1, 1)  # 1 Pantalon
    pedido1.agregar_producto(producto2, 4)  # 2 Blusa
    pedido1.agregar_producto(producto3, 2)  # 3 Zapatos

    # Asignar el pedido al cliente
    cliente1.realizar_pedido(pedido1)

    # Imprimir detalles del pedido
    print(pedido1)

    # Imprimir información del cliente y sus pedidos
    print("\nPedidos del cliente:")
    for pedido in cliente1.pedidos:
        print(pedido)
