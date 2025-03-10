class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.detalles = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.detalles[0]} por {self.detalles[1]} (ISBN: {self.isbn}, Categoría: {self.categoria})"


class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # Lista de libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario {ISBN: Libro}
        self.usuarios = {}  # Diccionario {ID: Usuario}

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print("El libro ya está en la biblioteca.")

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no existe en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios:
            self.usuarios[usuario.user_id] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("El usuario ya está registrado.")

    def dar_baja_usuario(self, user_id):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            print(f"Usuario con ID {user_id} eliminado.")
        else:
            print("El usuario no está registrado.")

    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[user_id]
            libro = self.libros[isbn]
            usuario.libros_prestados.append(libro)
            del self.libros[isbn]  # Eliminar de la colección disponible
            print(f"Libro '{libro.detalles[0]}' prestado a {usuario.nombre}.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro  # Volver a agregar a la colección disponible
                    print(f"Libro '{libro.detalles[0]}' devuelto por {usuario.nombre}.")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no encontrado.")

    def buscar_libro(self, **criterios):
        resultados = []
        for libro in self.libros.values():
            if all(getattr(libro, k, None) == v for k, v in criterios.items()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# Pruebas del sistema
biblioteca = Biblioteca()

# Agregar libros
libro1 = Libro("1984", "George Orwell", "Ficción", "12345")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "67890")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Ana Pérez", "001")
usuario2 = Usuario("Carlos Gómez", "002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libro
biblioteca.prestar_libro("001", "12345")

# Listar libros prestados
biblioteca.listar_libros_prestados("001")

# Devolver libro
biblioteca.devolver_libro("001", "12345")

# Buscar libro
print("Resultados de búsqueda:", biblioteca.buscar_libro(categoria="Novela"))
