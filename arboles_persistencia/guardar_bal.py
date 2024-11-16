import json
import sys
import os
# Obtener el directorio actual (scripts/)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navegar al directorio padre (Proyecto_Estructura/)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
models_dir = os.path.join(project_root, 'models')
if models_dir not in sys.path:
    sys.path.append(models_dir)
from balanced_tree import BalancedTree

def cargar_libros_desde_json(ruta_archivo):
    """Cargar libros desde un archivo JSON."""
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

# Función para guardar el árbol en un archivo JSON
def guardar_arbol_en_json(arbol, ruta):
    arbol_dict = arbol.to_dict()
    with open(ruta, 'w', encoding='utf-8') as file:
        json.dump(arbol_dict, file, ensure_ascii=False, indent=4)

# Función principal para probar
def main():
    ruta_libros = "base_de_datos/books.json"
    # Crear un árbol balanceado e insertar elementos
    arbol = BalancedTree()
    libros = cargar_libros_desde_json(ruta_libros)

    for libro in libros:
        arbol.insert(libro["anio_publicacion"], libro["id"])

    # Guardar el árbol en un archivo JSON
    guardar_arbol_en_json(arbol, "arbol_balanceado_con_ids.json")
    print("Árbol balanceado guardado en arbol_balanceado_con_ids.json")

if __name__ == "__main__":
    main()
