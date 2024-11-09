import uuid

class Libro:
    def __init__(self, titulo, autor, genero, anio_publicacion, editorial=None, isbn=None, id=None):
        self.id = id or str(uuid.uuid4())  # Genera un nuevo UUID si no se proporciona un ID
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.editorial = editorial
        self.isbn = isbn

    def __dict__(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'autor': self.autor,
            'genero': self.genero,
            'anio_publicacion': self.anio_publicacion,
            'editorial': self.editorial,
            'isbn': self.isbn
        }
