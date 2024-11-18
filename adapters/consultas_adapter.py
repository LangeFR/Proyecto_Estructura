import json
import os
import unicodedata

class ConsultasAdapter:
    def __init__(self):
        # Ajustar base_path para apuntar a Proyecto_Estructura
        self.base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        # Cargar datos JSON con rutas corregidas
        self.libros_titulos = self.cargar_json(os.path.join(self.base_path, "base_de_datos", "books.json"))
        self.autores = self.cargar_json(os.path.join(self.base_path, "base_de_datos", "autores.json"))
        self.generos = self.cargar_json(os.path.join(self.base_path, "base_de_datos", "generos.json"))
        self.editoriales = self.cargar_json(os.path.join(self.base_path, "base_de_datos", "editoriales.json"))

        # Inicializar datos adicionales
        self.autores_nombres = [autor["nombre"] for autor in self.autores]
        self.generos_nombres = [genero["nombre"] for genero in self.generos]
        self.hash_libros_por_anio = self.crear_hash_por_anio()
        self.años_publicacion = sorted(self.hash_libros_por_anio.keys())

    def cargar_json(self, archivo):
        try:
            with open(archivo, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"[ERROR] Archivo {archivo} no encontrado.")
            return []

    def crear_hash_por_anio(self):
        """Crea un diccionario que agrupa libros por año de publicación."""
        hash_por_anio = {}
        for libro in self.libros_titulos:
            anio = str(libro["anio_publicacion"])
            if anio not in hash_por_anio:
                hash_por_anio[anio] = []
            hash_por_anio[anio].append(libro["titulo"])
        return hash_por_anio

    def normalizar_texto(self, texto):
        """Normaliza un texto eliminando acentos, convirtiéndolo a minúsculas y eliminando espacios extras."""
        texto = ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')
        texto = texto.lower()
        return texto.strip()

    def busqueda_lineal_titulos(self, entrada):
        print(f"[DEBUG] Entrada recibida para búsqueda lineal: '{entrada}'")
        entrada = self.normalizar_texto(entrada)
        print(f"[DEBUG] Entrada normalizada: '{entrada}'")
        
        resultados = []
        for libro in self.libros_titulos:
            titulo_normalizado = self.normalizar_texto(libro["titulo"])
            if entrada in titulo_normalizado:
                print(f"[DEBUG] Coincidencia encontrada: '{libro['titulo']}'")
                resultados.append(libro["titulo"])
        
        print(f"[DEBUG] Total de resultados encontrados: {len(resultados)}")
        return resultados

    def obtener_generos_hijos(self, genero_padre_id):
        """Obtiene todos los géneros hijos de un género padre recursivamente."""
        hijos = [genero for genero in self.generos if genero.get("generoPadreId") == genero_padre_id]
        for hijo in hijos:
            hijos.extend(self.obtener_generos_hijos(hijo["id"]))
        return hijos

    def buscar_por_id(self, id, lista):
        for elemento in lista:
            if elemento["id"] == id:
                return elemento["nombre"]
        return "Desconocido"

    # Puedes agregar más métodos aquí según sea necesario
