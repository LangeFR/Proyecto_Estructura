import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from adapters.consultas_adapter import ConsultasAdapter
import tkinter as tk
import tkinter.ttk as ttk


class Toplevel1:
    def __init__(self, top=None):
        top.geometry("800x600+597+181")  # Aumenté el tamaño para acomodar la tabla
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1, 1)
        top.title("Gestión de Libros")
        top.configure(background="#98e4fe")

        self.top = top
        self.filtros_activos = {}  # Cambiado de filtro_activo a un diccionario

        # Inicializar el adaptador
        self.adapter = ConsultasAdapter()

        # Marco principal
        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
        self.Frame1.configure(relief='groove', borderwidth="2", background="#9b0a64")

        # Título de la ventana
        self.LabelTitle = tk.Label(self.Frame1)
        self.LabelTitle.place(relx=0.35, rely=0.03, height=30, width=200)
        self.LabelTitle.configure(background="#9b0a64", foreground="#ffffff", text='Gestión de Libros', font=("Arial", 14, "bold"))

        # Label Nombre
        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.037, rely=0.15, height=21, width=64)
        self.Label1.configure(background="#9b0a64", foreground="#ffffff", text='Nombre')

        # Entry para autocompletar títulos
        self.TEntry1 = ttk.Entry(self.Frame1)
        self.TEntry1.place(relx=0.147, rely=0.15, relheight=0.049, relwidth=0.246)
        self.TEntry1.bind("<KeyRelease>", self.autocompletar_titulos)
        self.TEntry1.bind("<FocusIn>", lambda e: self.activar_filtro("titulo"))

        # Label Autor
        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.037, rely=0.23, height=21, width=64)
        self.Label2.configure(background="#9b0a64", foreground="#ffffff", text='Autor')

        # Combobox para autocompletar autores
        self.TComboboxAutores = ttk.Combobox(self.Frame1)
        self.TComboboxAutores.place(relx=0.147, rely=0.23, relheight=0.049, relwidth=0.246)
        self.TComboboxAutores.bind("<KeyRelease>", self.filtrar_autores)
        self.TComboboxAutores.bind("<<ComboboxSelected>>", self.mostrar_libros_autor)
        self.TComboboxAutores.bind("<FocusIn>", lambda e: self.activar_filtro("autor"))

        # Label Género
        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.037, rely=0.31, height=21, width=64)
        self.Label3.configure(background="#9b0a64", foreground="#ffffff", text='Género')

        # Combobox para seleccionar género
        self.TCombobox1 = ttk.Combobox(self.Frame1, state='readonly')
        self.TCombobox1.place(relx=0.147, rely=0.31, relheight=0.049, relwidth=0.246)
        self.TCombobox1.bind("<<ComboboxSelected>>", self.mostrar_libros_genero)
        self.TCombobox1.bind("<FocusIn>", lambda e: self.activar_filtro("genero"))

        # Label Año
        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.037, rely=0.39, height=21, width=64)
        self.Label4.configure(background="#9b0a64", foreground="#ffffff", text='Año')

        # Combobox Año Publicación
        self.TComboboxAñoPub = ttk.Combobox(self.Frame1, state='readonly')
        self.TComboboxAñoPub.place(relx=0.147, rely=0.39, relheight=0.049, relwidth=0.246)
        self.TComboboxAñoPub.bind("<<ComboboxSelected>>", self.mostrar_libros_anio)
        self.TComboboxAñoPub.bind("<FocusIn>", lambda e: self.activar_filtro("anio"))

        # Label ISBN
        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.037, rely=0.47, height=21, width=64)
        self.Label5.configure(background="#9b0a64", foreground="#ffffff", text='ISBN')

        # Entry para ISBN (solo lectura)
        self.TEntry4 = ttk.Entry(self.Frame1, state='readonly')
        self.TEntry4.place(relx=0.147, rely=0.47, relheight=0.049, relwidth=0.246)

        # Label Editorial
        self.Label6 = tk.Label(self.Frame1)
        self.Label6.place(relx=0.037, rely=0.55, height=21, width=64)
        self.Label6.configure(background="#9b0a64", foreground="#ffffff", text='Editorial')

        # Entry para Editorial (solo lectura)
        self.TEntry5 = ttk.Entry(self.Frame1, state='readonly')
        self.TEntry5.place(relx=0.147, rely=0.55, relheight=0.049, relwidth=0.246)

        # Treeview para mostrar información en formato de tabla
        self.Treeview1 = ttk.Treeview(self.Frame1, columns=("Titulo", "Autor", "Genero", "Editorial", "Año", "ISBN"), show='headings')
        self.Treeview1.place(relx=0.037, rely=0.63, relheight=0.3, relwidth=0.926)

        # Definir encabezados de columnas
        self.Treeview1.heading("Titulo", text="Título")
        self.Treeview1.heading("Autor", text="Autor")
        self.Treeview1.heading("Genero", text="Género")
        self.Treeview1.heading("Editorial", text="Editorial")
        self.Treeview1.heading("Año", text="Año de Publicación")
        self.Treeview1.heading("ISBN", text="ISBN")

        # Definir el ancho de las columnas
        self.Treeview1.column("Titulo", width=150)
        self.Treeview1.column("Autor", width=100)
        self.Treeview1.column("Genero", width=100)
        self.Treeview1.column("Editorial", width=100)
        self.Treeview1.column("Año", width=100)
        self.Treeview1.column("ISBN", width=100)

        # Agregar scrollbar a la Treeview
        self.scrollbar = ttk.Scrollbar(self.Frame1, orient="vertical", command=self.Treeview1.yview)
        self.Treeview1.configure(yscroll=self.scrollbar.set)
        self.scrollbar.place(relx=0.963, rely=0.63, relheight=0.3)

        # Botón Regresar
        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.128, rely=0.95, height=26, width=80)
        self.Button1.configure(background="#fdab02", text='Regresar', command=self.regresar)

        # Botón Nueva Búsqueda
        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.3, rely=0.95, height=26, width=120)
        self.Button2.configure(background="#fdab02", text='Nueva Búsqueda', command=self.limpiar_busqueda)

        # Llenar Combobox de Autores con opción "Todos"
        self.TComboboxAutores['values'] = ["Todos"] + self.adapter.autores_nombres

        # Llenar Combobox de Géneros con opción "Todos"
        self.TCombobox1['values'] = ["Todos"] + self.adapter.generos_nombres

        # Llenar Combobox de Años de Publicación con opción "Todos"
        self.TComboboxAñoPub['values'] = ["Todos"] + self.adapter.años_publicacion

    # Métodos que interactúan con el adaptador
    def autocompletar_titulos(self, event):
        entrada = self.TEntry1.get()
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

        self.Treeview1.delete(*self.Treeview1.get_children())

        # Restablecer los filtros activos
        self.filtros_activos.clear()
        print("[DEBUG] Todos los filtros activos han sido limpiados.")

        # Mostrar todos los libros
        self.aplicar_filtros_combinados()

    # Eliminar el método activar_filtro_por_nombre y sus llamadas

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
