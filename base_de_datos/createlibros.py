import json
import uuid
import random
import os

# Definimos la ruta donde se guardará el archivo JSON
ruta_base_datos = r"C:\Users\DellInspiron5570\Documents\Universidad\Semestres\Semestre 4\Estructura\Corte 3\Proyecto_Estructura\base_de_datos\books.json"

# Géneros terminales (hojas) del árbol
generos = [
    "Space Opera", "Distopia", "Alta Fantasia", "Fantasia Urbana", 
    "Thriller Psicologico", "Policial", "Romance Historico", "Comedia Romantica", 
    "Autobiografia", "Memorias", "Filosofico", "Cientifico", 
    "Historia Antigua", "Historia Moderna", "Desarrollo Personal", "Psicologia Positiva",
    "Cuentos de Hadas", "Fantasia Juvenil", "Misterio Infantil", "Aventura Juvenil"
]

# Listas de autores, editoriales y posibles años de publicación
autores = [
    "Gabriel Garcia Marquez", "Jane Austen", "Isaac Asimov", "Agatha Christie", "H. G. Wells",
    "J. K. Rowling", "J. R. R. Tolkien", "George Orwell", "Virginia Woolf", "Charles Dickens",
    "Leo Tolstoy", "Herman Melville", "Harper Lee", "Mark Twain", "F. Scott Fitzgerald",
    "Stephen King", "Arthur Conan Doyle", "Ernest Hemingway", "Edgar Allan Poe", "Ray Bradbury",
    "Aldous Huxley", "Jules Verne", "Jack London", "Kurt Vonnegut", "Philip K. Dick",
    "John Steinbeck", "T. S. Eliot", "George R. R. Martin", "William Faulkner", "Oscar Wilde",
    "James Joyce", "Dante Alighieri", "Homer", "Emily Dickinson", "Mary Shelley",
    "Bram Stoker", "H. P. Lovecraft", "Margaret Atwood", "Franz Kafka", "Robert Louis Stevenson"
]

editoriales = [
    "Penguin Random House", "HarperCollins", "Macmillan", "Simon & Schuster", "Hachette Book Group",
    "Bloomsbury", "Scholastic", "Pan Macmillan", "Vintage", "Dover Publications",
    "Oxford University Press", "Cambridge University Press"
]

# Generar una lista de años de publicación en un rango de 30 años
anios_publicacion = list(range(1990, 2020))

# Títulos de ejemplo (aseguramos que sean únicos y variados)
titulos_base = [
    "El misterio de", "La sombra de", "Historias de", "Cronicas de", "El despertar de", 
    "La leyenda de", "Secretos de", "Recuerdos de", "Aventuras en", "El viaje a",
    "La guerra de", "El enigma de", "El canto de", "Bajo el cielo de", "El rostro de",
    "El tiempo de", "La caida de", "Los secretos de", "La noche de", "El destino de",
    "En busca de", "La pasion de", "La magia de", "El misterio del", "La marca de",
    "El ultimo de", "La luz de", "El poder de", "La verdad de", "La vida de"
]

# Crear lista para almacenar los libros
libros = []

# Crear 70 libros cumpliendo las condiciones
for _ in range(70):
    titulo = random.choice(titulos_base) + " " + random.choice(["la luna", "el mar", "las estrellas", "la tierra", "los secretos", "las sombras", "el pasado", "el futuro", "los dioses", "los heroes"])
    titulo = titulo[:50]  # Limitar longitud del título si es necesario
    autor = random.choice(autores)
    genero = random.choice(generos)
    anio_publicacion = random.choice(anios_publicacion)
    editorial = random.choice(editoriales)
    isbn = f"{random.randint(100, 999)}-{random.randint(10, 99)}-{random.randint(1000000, 9999999)}-{random.randint(0, 9)}"
    id_libro = str(uuid.uuid4())

    # Crear libro
    libro = {
        "id": id_libro,
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "anio_publicacion": anio_publicacion,
        "editorial": editorial,
        "isbn": isbn
    }

    # Añadir a la lista de libros
    libros.append(libro)

# Crear la carpeta si no existe y guardar el archivo JSON
os.makedirs(os.path.dirname(ruta_base_datos), exist_ok=True)
with open(ruta_base_datos, 'w') as file:
    json.dump(libros, file, indent=4)

print("Archivo JSON con libros generado exitosamente.")
