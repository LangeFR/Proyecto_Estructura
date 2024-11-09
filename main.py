import uuid
import json
import os

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

# Ruta completa para guardar los libros
ruta_base_datos = r"C:\Users\DellInspiron5570\Documents\Universidad\Semestres\Semestre 4\Estructura\Corte 3\Proyecto_Estructura\base_de_datos\books.json"

def load_books(filename=ruta_base_datos):
    try:
        with open(filename, 'r') as file:
            books_data = json.load(file)
            return [Libro(**data) for data in books_data]
    except FileNotFoundError:
        return []

def save_books(books, filename=ruta_base_datos):
    # Crear la carpeta si no existe
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as file:
        json.dump([book.__dict__() for book in books], file, indent=4)

def main():
    # Cargar los libros actuales
    books = load_books()
    
    # Crear un nuevo libro de ejemplo
    nuevo_libro = Libro(
        titulo="El Principito",
        autor="Antoine de Saint-Exupéry",
        genero="Ficción",
        anio_publicacion=1943,
        editorial="Reynal & Hitchcock",
        isbn="978-3-16-148410-0"
    )
    
    # Añadir el libro a la lista de libros y guardarlo
    books.append(nuevo_libro)
    save_books(books)
    print("Libro guardado exitosamente.")

if __name__ == "__main__":
    main()
