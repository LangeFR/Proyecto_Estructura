import json
import sys
import os

# Obtener el directorio actual (scripts/)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navegar al directorio padre (Proyecto_Estructura/)
project_root = os.path.abspath(os.path.join(current_dir, '..'))
print(f"Directorio raíz del proyecto: {project_root}")  # Depuración

# Validar que project_root sea una ruta válida
if not os.path.isdir(project_root):
    raise FileNotFoundError(f"Directorio del proyecto no encontrado: {project_root}")

models_dir = os.path.join(project_root, 'models')
if models_dir not in sys.path:
    sys.path.append(models_dir)

from balanced_tree import BalancedTree

def cargar_libros_desde_json(ruta_archivo):
    """Cargar libros desde un archivo JSON."""
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"Archivo JSON no encontrado: {ruta_archivo}")
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

# Función para guardar el árbol en un archivo JSON
def guardar_arbol_en_json(arbol, ruta):
    arbol_dict = arbol.to_dict()
    with open(ruta, 'w', encoding='utf-8') as file:
        json.dump(arbol_dict, file, ensure_ascii=False, indent=4)

# Función principal para probar
def main():
    try:
        # Ruta absoluta del archivo books.json
        ruta_libros = os.path.join(project_root, "base_de_datos", "books.json")
        print(f"Cargando libros desde: {ruta_libros}")  # Depuración

        # Crear un árbol balanceado e insertar elementos
        arbol = BalancedTree()
        libros = cargar_libros_desde_json(ruta_libros)

        for libro in libros:
            arbol.insert(libro["anio_publicacion"], libro["id"])

        # Ruta para guardar el árbol balanceado
        ruta_arbol = os.path.join(project_root, "arboles_persistencia", "arbol_balanceado_con_ids.json")
        guardar_arbol_en_json(arbol, ruta_arbol)
        print(f"Árbol balanceado guardado en {ruta_arbol}")

    except Exception as e:
        print(f"Error en la ejecución: {e}")
        raise

if __name__ == "__main__":
    main()
