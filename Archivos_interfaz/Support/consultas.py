import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from adapters.consultas_adapter import ConsultasAdapter
import tkinter as tk
import tkinter.ttk as ttk


class Toplevel1:
    def __init__(self, top=None):
        # Maximizar la ventana manteniendo la barra superior visible
        top.state('zoomed')  # Funciona en Windows
        # Para otras plataformas, podrías necesitar ajustar esto

        top.title("Gestión de Libros")
        top.configure(background="#98e4fe")

        self.top = top
        self.filtros_activos = {}  # Diccionario para almacenar los filtros activos

        # Inicializar el adaptador
        self.adapter = ConsultasAdapter()

        # Marco exterior para márgenes
        self.outer_frame = tk.Frame(self.top, bg="#98e4fe")
        self.outer_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=50)

        # Marco principal que contendrá los marcos de filtros y resultados
        self.main_frame = tk.Frame(self.outer_frame, bg="#9b0a64")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Crear el marco de filtros a la izquierda con ancho fijo
        self.filters_frame = tk.Frame(self.main_frame, width=300, bg="#9b0a64")
        self.filters_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(10, 20), pady=10)
        self.filters_frame.pack_propagate(False)  # Evita que el marco se ajuste al contenido

        # Título de la ventana dentro del marco de filtros
        self.LabelTitle = tk.Label(self.filters_frame, text='Gestión de Libros', bg="#9b0a64",
                                   fg="#ffffff", font=("Arial", 14, "bold"))
        self.LabelTitle.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='w')

        # Label y Entry para Nombre
        self.Label1 = tk.Label(self.filters_frame, text='Nombre', bg="#9b0a64", fg="#ffffff")
        self.Label1.grid(row=1, column=0, sticky='w', pady=5)
        self.TEntry1 = ttk.Entry(self.filters_frame)
        self.TEntry1.grid(row=1, column=1, pady=5, sticky='ew')
        self.TEntry1.bind("<KeyRelease>", self.autocompletar_titulos)
        self.TEntry1.bind("<FocusIn>", lambda e: self.activar_filtro("titulo"))

        # Label y Combobox para Autor
        self.Label2 = tk.Label(self.filters_frame, text='Autor', bg="#9b0a64", fg="#ffffff")
        self.Label2.grid(row=2, column=0, sticky='w', pady=5)
        self.TComboboxAutores = ttk.Combobox(self.filters_frame)
        self.TComboboxAutores.grid(row=2, column=1, pady=5, sticky='ew')
        self.TComboboxAutores.bind("<KeyRelease>", self.filtrar_autores)
        self.TComboboxAutores.bind("<<ComboboxSelected>>", self.mostrar_libros_autor)
        self.TComboboxAutores.bind("<FocusIn>", lambda e: self.activar_filtro("autor"))

        # Label y Combobox para Género
        self.Label3 = tk.Label(self.filters_frame, text='Género', bg="#9b0a64", fg="#ffffff")
        self.Label3.grid(row=3, column=0, sticky='w', pady=5)
        self.TCombobox1 = ttk.Combobox(self.filters_frame, state='readonly')
        self.TCombobox1.grid(row=3, column=1, pady=5, sticky='ew')
        self.TCombobox1.bind("<<ComboboxSelected>>", self.mostrar_libros_genero)
        self.TCombobox1.bind("<FocusIn>", lambda e: self.activar_filtro("genero"))

        # Label y Combobox para Año de Publicación
        self.Label4 = tk.Label(self.filters_frame, text='Año', bg="#9b0a64", fg="#ffffff")
        self.Label4.grid(row=4, column=0, sticky='w', pady=5)
        self.TComboboxAñoPub = ttk.Combobox(self.filters_frame, state='readonly')
        self.TComboboxAñoPub.grid(row=4, column=1, pady=5, sticky='ew')
        self.TComboboxAñoPub.bind("<<ComboboxSelected>>", self.mostrar_libros_anio)
        self.TComboboxAñoPub.bind("<FocusIn>", lambda e: self.activar_filtro("anio"))

        # Label y Entry para ISBN (solo lectura)
        self.Label5 = tk.Label(self.filters_frame, text='ISBN', bg="#9b0a64", fg="#ffffff")
        self.Label5.grid(row=5, column=0, sticky='w', pady=5)
        self.TEntry4 = ttk.Entry(self.filters_frame, state='readonly')
        self.TEntry4.grid(row=5, column=1, pady=5, sticky='ew')

        # Label y Entry para Editorial (solo lectura)
        self.Label6 = tk.Label(self.filters_frame, text='Editorial', bg="#9b0a64", fg="#ffffff")
        self.Label6.grid(row=6, column=0, sticky='w', pady=5)
        self.TEntry5 = ttk.Entry(self.filters_frame, state='readonly')
        self.TEntry5.grid(row=6, column=1, pady=5, sticky='ew')

        # Botones en el marco de filtros
        self.Button1 = tk.Button(self.filters_frame, text='Regresar', bg="#fdab02", command=self.regresar)
        self.Button1.grid(row=7, column=0, pady=20, sticky='ew')

        self.Button2 = tk.Button(self.filters_frame, text='Nueva Búsqueda', bg="#fdab02", command=self.limpiar_busqueda)
        self.Button2.grid(row=7, column=1, pady=20, sticky='ew')

        # Configurar las columnas del grid en filters_frame para ajustar el ancho
        self.filters_frame.columnconfigure(0, weight=1)
        self.filters_frame.columnconfigure(1, weight=3)

        # Crear el marco de resultados a la derecha
        self.results_frame = tk.Frame(self.main_frame, bg="#98e4fe")
        self.results_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 10), pady=10)

        # Treeview para mostrar información en formato de tabla
        self.Treeview1 = ttk.Treeview(self.results_frame, columns=("Titulo", "Autor", "Genero", "Editorial", "Año", "ISBN"), show='headings')
        self.Treeview1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Definir encabezados de columnas con comandos para ordenamiento
        self.Treeview1.heading("Titulo", text="Título", command=lambda: self.sort_by("Titulo"))
        self.Treeview1.heading("Autor", text="Autor", command=lambda: self.sort_by("Autor"))
        self.Treeview1.heading("Genero", text="Género", command=lambda: self.sort_by("Genero"))
        self.Treeview1.heading("Editorial", text="Editorial", command=lambda: self.sort_by("Editorial"))
        self.Treeview1.heading("Año", text="Año de Publicación", command=lambda: self.sort_by("Año"))
        self.Treeview1.heading("ISBN", text="ISBN", command=lambda: self.sort_by("ISBN"))

        # Definir el ancho y alineación de las columnas
        self.Treeview1.column("Titulo", width=200, anchor='w')
        self.Treeview1.column("Autor", width=150, anchor='w')
        self.Treeview1.column("Genero", width=150, anchor='w')
        self.Treeview1.column("Editorial", width=150, anchor='w')
        self.Treeview1.column("Año", width=100, anchor='center')
        self.Treeview1.column("ISBN", width=150, anchor='center')

        # Agregar scrollbar a la Treeview
        self.scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=self.Treeview1.yview)
        self.Treeview1.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Diccionario para rastrear el orden de ordenamiento de cada columna
        self.sort_order = {
            "Titulo": True,      # True significa ascendente, False descendente
            "Autor": True,
            "Genero": True,
            "Editorial": True,
            "Año": True,
            "ISBN": True
        }

        # Asociar doble clic en la Treeview para mostrar detalles
        self.Treeview1.bind("<Double-1>", self.mostrar_detalles)

        # Llenar Combobox de Autores con opción "Todos"
        self.TComboboxAutores['values'] = ["Todos"] + self.adapter.autores_nombres

        # Llenar Combobox de Géneros con opción "Todos"
        self.TCombobox1['values'] = ["Todos"] + self.adapter.generos_nombres

        # Llenar Combobox de Años de Publicación con opción "Todos"
        self.TComboboxAñoPub['values'] = ["Todos"] + self.adapter.años_publicacion

        # Mostrar todos los libros inicialmente
        self.aplicar_filtros_combinados()

    # Métodos que interactúan con el adaptador
    def autocompletar_titulos(self, event):
        entrada = self.TEntry1.get()
        if entrada.strip() == "":
            self.filtros_activos.pop("titulo", None)
        else:
            self.filtros_activos["titulo"] = entrada  # Actualizar filtro de título
        print(f"[DEBUG] Filtro 'titulo' actualizado a: '{entrada}'")
        self.aplicar_filtros_combinados()

    def filtrar_autores(self, event):
        entrada = self.TComboboxAutores.get().lower()
        coincidencias = [autor for autor in self.adapter.autores_nombres if entrada in autor.lower()]
        self.TComboboxAutores['values'] = ["Todos"] + coincidencias
        print(f"[DEBUG] Filtrando autores con entrada: '{entrada}'. Coincidencias: {coincidencias}")
        # No actualiza el filtro aquí, se actualiza al seleccionar

    def mostrar_libros_autor(self, event):
        autor_seleccionado = self.TComboboxAutores.get()
        if autor_seleccionado == "Todos":
            self.filtros_activos.pop("autor", None)
            print(f"[DEBUG] Filtro 'autor' eliminado (se seleccionó 'Todos').")
        else:
            self.filtros_activos["autor"] = autor_seleccionado
            print(f"[DEBUG] Filtro 'autor' actualizado a: '{autor_seleccionado}'")
        self.aplicar_filtros_combinados()

    def mostrar_libros_genero(self, event):
        genero_seleccionado = self.TCombobox1.get()
        if genero_seleccionado == "Todos":
            self.filtros_activos.pop("genero", None)
            print(f"[DEBUG] Filtro 'genero' eliminado (se seleccionó 'Todos').")
        else:
            self.filtros_activos["genero"] = genero_seleccionado
            print(f"[DEBUG] Filtro 'genero' actualizado a: '{genero_seleccionado}'")
        self.aplicar_filtros_combinados()

    def mostrar_libros_anio(self, event):
        anio_seleccionado = self.TComboboxAñoPub.get()
        if anio_seleccionado == "Todos":
            self.filtros_activos.pop("anio", None)
            print(f"[DEBUG] Filtro 'anio' eliminado (se seleccionó 'Todos').")
        else:
            self.filtros_activos["anio"] = anio_seleccionado
            print(f"[DEBUG] Filtro 'anio' actualizado a: '{anio_seleccionado}'")
        self.aplicar_filtros_combinados()

    def aplicar_filtros_combinados(self):
        """Aplica todos los filtros activos y muestra los libros que cumplen con todos los criterios."""
        print(f"[DEBUG] Aplicando filtros combinados: {self.filtros_activos}")
        resultados = set(libro["titulo"] for libro in self.adapter.libros_titulos)  # Empezar con todos los libros

        # Aplicar filtro de título
        titulo = self.filtros_activos.get("titulo", "").strip().lower()
        if titulo:
            print(f"[DEBUG] Aplicando filtro de título: '{titulo}'")
            coincidencias_titulo = set(self.adapter.busqueda_lineal_titulos(titulo))
            print(f"[DEBUG] Coincidencias de título: {coincidencias_titulo}")
            resultados &= coincidencias_titulo

        # Aplicar filtro de autor
        autor = self.filtros_activos.get("autor", "").strip().lower()
        if autor:
            print(f"[DEBUG] Aplicando filtro de autor: '{autor}'")
            autor_id = next((autor_obj["id"] for autor_obj in self.adapter.autores if autor_obj["nombre"].lower() == autor), None)
            if autor_id:
                libros_autor = set(libro["titulo"] for libro in self.adapter.libros_titulos if libro["autorId"] == autor_id)
                print(f"[DEBUG] Libros por autor ID {autor_id}: {libros_autor}")
                resultados &= libros_autor
            else:
                print(f"[DEBUG] No se encontró el autor: '{autor}'")
                resultados.clear()

        # Aplicar filtro de género
        genero = self.filtros_activos.get("genero", "").strip().lower()
        if genero:
            print(f"[DEBUG] Aplicando filtro de género: '{genero}'")
            genero_id = next((genero_obj["id"] for genero_obj in self.adapter.generos if genero_obj["nombre"].lower() == genero), None)
            if genero_id:
                generos_hijos = self.adapter.obtener_generos_hijos(genero_id)
                ids_generos = {genero_id} | {g["id"] for g in generos_hijos}
                libros_genero = set(libro["titulo"] for libro in self.adapter.libros_titulos if libro["generoId"] in ids_generos)
                print(f"[DEBUG] Libros por género ID {genero_id}: {libros_genero}")
                resultados &= libros_genero
            else:
                print(f"[DEBUG] No se encontró el género: '{genero}'")
                resultados.clear()

        # Aplicar filtro de año
        anio = self.filtros_activos.get("anio", "").strip()
        if anio:
            print(f"[DEBUG] Aplicando filtro de año: '{anio}'")
            libros_anio = set(libro["titulo"] for libro in self.adapter.libros_titulos if str(libro["anio_publicacion"]) == anio)
            print(f"[DEBUG] Libros por año '{anio}': {libros_anio}")
            resultados &= libros_anio

        # Mostrar resultados en el Treeview
        self.Treeview1.delete(*self.Treeview1.get_children())
        for titulo in sorted(resultados):
            libro = next((libro for libro in self.adapter.libros_titulos if libro["titulo"] == titulo), None)
            if libro:
                autor_nombre = self.adapter.buscar_por_id(libro["autorId"], self.adapter.autores)
                genero_nombre = self.adapter.buscar_por_id(libro["generoId"], self.adapter.generos)
                editorial_nombre = self.adapter.buscar_por_id(libro["editorialId"], self.adapter.editoriales)
                año = libro["anio_publicacion"]
                isbn = libro["isbn"]
                self.Treeview1.insert("", tk.END, values=(titulo, autor_nombre, genero_nombre, editorial_nombre, año, isbn))
        print(f"[DEBUG] Total de resultados mostrados en Treeview: {len(resultados)}")

    def limpiar_busqueda(self):
        """Limpia todos los campos de búsqueda y detalles del libro."""
        # Limpiar campos de entrada
        self.TEntry1.configure(state="normal")
        self.TEntry1.delete(0, tk.END)
        self.TComboboxAutores.set("Todos")
        self.TCombobox1.set("Todos")
        self.TComboboxAñoPub.set("Todos")

        # Limpiar los detalles del libro seleccionado
        self.TEntry4.configure(state='normal')
        self.TEntry4.delete(0, tk.END)
        self.TEntry4.configure(state='readonly')
        self.TEntry5.configure(state='normal')
        self.TEntry5.delete(0, tk.END)
        self.TEntry5.configure(state='readonly')

        # Limpiar la Treeview
        self.Treeview1.delete(*self.Treeview1.get_children())

        # Restablecer los filtros activos
        self.filtros_activos.clear()
        print("[DEBUG] Todos los filtros activos han sido limpiados.")

        # Mostrar todos los libros
        self.aplicar_filtros_combinados()

    def activar_filtro(self, filtro):
        """Activa un filtro y actualiza su valor en el diccionario."""
        # Este método ya no es necesario en su forma actual, ya que los filtros se actualizan directamente en los métodos de filtro
        print(f"[DEBUG] Filtro activado: {filtro}")
        # No modificar self.filtros_activos aquí

    def mostrar_detalles(self, event):
        seleccion = self.Treeview1.focus()
        if seleccion:
            valores = self.Treeview1.item(seleccion, 'values')
            if valores:
                titulo, autor, genero, editorial, año, isbn = valores
                print(f"[DEBUG] Mostrando detalles para el libro seleccionado: '{titulo}'")
                # Llenar campos
                self.TEntry1.configure(state="normal")
                self.TEntry1.delete(0, tk.END)
                self.TEntry1.insert(0, titulo)
                self.TComboboxAutores.set(autor)
                self.TCombobox1.set(genero)
                self.TComboboxAñoPub.set(año)
                self.TEntry4.configure(state='normal')
                self.TEntry4.delete(0, tk.END)
                self.TEntry4.insert(0, isbn)
                self.TEntry4.configure(state='readonly')
                self.TEntry5.configure(state='normal')
                self.TEntry5.delete(0, tk.END)
                self.TEntry5.insert(0, editorial)
                self.TEntry5.configure(state='readonly')

                # Opcional: Si deseas desactivar los filtros después de seleccionar un libro, puedes hacerlo aquí
                # self.desactivar_todos_los_filtros()

    def sort_by(self, column):
        """Ordena la Treeview por la columna especificada utilizando el método de inserción."""
        print(f"[DEBUG] Ordenando por columna: '{column}' - Ascendente: {self.sort_order[column]}")
        
        # Obtener todos los elementos de la Treeview
        data = [(self.Treeview1.set(child, column), child) for child in self.Treeview1.get_children('')]
        
        # Determinar si la columna es numérica (Año)
        is_numeric = column == "Año"
        
        # Implementar Insertion Sort
        for i in range(1, len(data)):
            key = data[i][0]
            key_child = data[i][1]
            j = i - 1
            while j >= 0:
                current = data[j][0]
                if is_numeric:
                    # Convertir a entero para comparación numérica
                    try:
                        key_val = int(key)
                    except ValueError:
                        key_val = 0
                    try:
                        current_val = int(current)
                    except ValueError:
                        current_val = 0
                else:
                    key_val = key.lower()
                    current_val = current.lower()
                
                if self.sort_order[column]:
                    condition = key_val < current_val
                else:
                    condition = key_val > current_val
                
                if condition:
                    data[j + 1] = data[j]
                    j -= 1
                else:
                    break
            data[j + 1] = (key, key_child)
        
        # Reinsertar los elementos ordenados en la Treeview
        for index, (val, child) in enumerate(data):
            self.Treeview1.move(child, '', index)
        
        # Alternar el orden de sort para la próxima vez que se haga clic
        self.sort_order[column] = not self.sort_order[column]
        print(f"[DEBUG] Orden de sort para columna '{column}' ahora es {'Ascendente' if self.sort_order[column] else 'Descendente'}")

    def buscar_por_id(self, id, lista):
        return self.adapter.buscar_por_id(id, lista)

    def regresar(self):
        """Lógica para el botón Regresar."""
        print("[DEBUG] Botón 'Regresar' presionado.")
        # Cerrar la ventana actual
        self.top.destroy()
        # Importar y llamar al método principal de navegacion.py
        import navegacion
        navegacion.start_up()


if __name__ == '__main__':
    root = tk.Tk()
    app = Toplevel1(top=root)
    root.mainloop()