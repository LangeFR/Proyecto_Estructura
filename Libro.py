class Libro:
    def __init__(self, titulo, autor, genero, anio_publicacion, editorial=None, isbn=None):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.editorial = editorial
        self.isbn = isbn

    def __str__(self):
        return f"'{self.titulo}' by {self.autor} ({self.anio_publicacion}) - Genre: {self.genero}"

    def __repr__(self):
        return (f"Libro(titulo={self.titulo}, autor={self.autor}, "
                f"genero={self.genero}, anio_publicacion={self.anio_publicacion}, "
                f"editorial={self.editorial}, isbn={self.isbn})")
