import tkinter as tk
import tkinter.ttk as ttk
import json
import os

class Toplevel1:
    def __init__(self, top=None):
        top.geometry("600x500+597+181")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1, 1)
        top.title("Gestión de Libros")
        top.configure(background="#98e4fe")

        self.top = top

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

        # Label Autor
        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.037, rely=0.23, height=21, width=64)
        self.Label2.configure(background="#9b0a64", foreground="#ffffff", text='Autor')

        # Combobox para autocompletar autores
        self.TComboboxAutores = ttk.Combobox(self.Frame1)
        self.TComboboxAutores.place(relx=0.147, rely=0.23, relheight=0.049, relwidth=0.246)
        self.TComboboxAutores.bind("<KeyRelease>", self.filtrar_autores)
        self.TComboboxAutores.bind("<<ComboboxSelected>>", self.mostrar_libros_autor)

        # Label Género
        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.037, rely=0.31, height=21, width=64)
        self.Label3.configure(background="#9b0a64", foreground="#ffffff", text='Género')

        # Combobox para seleccionar género
        self.TCombobox1 = ttk.Combobox(self.Frame1, state='readonly')
        self.TCombobox1.place(relx=0.147, rely=0.31, relheight=0.049, relwidth=0.246)
        self.TCombobox1.bind("<<ComboboxSelected>>", self.mostrar_libros_genero)

        # Label Año
        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.037, rely=0.39, height=21, width=64)
        self.Label4.configure(background="#9b0a64", foreground="#ffffff", text='Año')

        # Combobox Año Publicación
        self.TComboboxAñoPub = ttk.Combobox(self.Frame1, state='readonly')
        self.TComboboxAñoPub.place(relx=0.147, rely=0.39, relheight=0.049, relwidth=0.246)  # Ajustar rely a 0.39
        self.TComboboxAñoPub.bind("<<ComboboxSelected>>", self.mostrar_libros_anio)


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

        # Listbox para mostrar información
        self.Listbox1 = tk.Listbox(self.Frame1)
        self.Listbox1.place(relx=0.532, rely=0.15, relheight=0.6, relwidth=0.393)
        self.Listbox1.bind("<Double-1>", self.mostrar_detalles)

        # Botón Regresar
        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.128, rely=0.85, height=26, width=80)
        self.Button1.configure(background="#fdab02", text='Regresar', command=self.regresar)


        # Ajustar base_path para apuntar a Proyecto_Estructura
        self.base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

        # Cargar datos JSON con rutas corregidas
        self.libros_titulos = self.cargar_json(os.path.join(self.base_path, "base_de_datos", "books.json"))
        self.autores = self.cargar_json(os.path.join(self.base_path, "base_de_datos", "autores.json"))
        self.generos = self.cargar_json(os.path.join(self.base_path, "base_de_datos", "generos.json"))
        self.editoriales = self.cargar_json(os.path.join(self.base_path, "base_de_datos", "editoriales.json"))

        # Llenar Combobox de Autores
        self.autores_nombres = [autor["nombre"] for autor in self.autores]
        self.TComboboxAutores['values'] = self.autores_nombres

        # Llenar Combobox de Géneros
        self.generos_nombres = [genero["nombre"] for genero in self.generos]
        self.TCombobox1['values'] = self.generos_nombres

        # Llenar Combobox de Años de Publicación
        self.años_publicacion = sorted(set(libro["anio_publicacion"] for libro in self.libros_titulos))
        self.TComboboxAñoPub['values'] = self.años_publicacion

    def cargar_json(self, archivo):
        try:
            with open(archivo, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Ruta: ", os.path.abspath(archivo))
            print(f"Archivo {archivo} no encontrado.")
            return []

    def autocompletar_titulos(self, event):
        entrada = self.TEntry1.get().lower()
        coincidencias = [libro["titulo"] for libro in self.libros_titulos if entrada in libro["titulo"].lower()]
        self.Listbox1.delete(0, tk.END)
        for titulo in coincidencias:
            self.Listbox1.insert(tk.END, titulo)

    def filtrar_autores(self, event):
        entrada = self.TComboboxAutores.get().lower()
        coincidencias = [autor for autor in self.autores_nombres if entrada in autor.lower()]
        self.TComboboxAutores['values'] = coincidencias

    def mostrar_libros_autor(self, event):
        autor_seleccionado = self.TComboboxAutores.get()
        for autor in self.autores:
            if autor["nombre"] == autor_seleccionado:
                libros_autor = [libro["titulo"] for libro in self.libros_titulos if libro["autorId"] == autor["id"]]
                self.Listbox1.delete(0, tk.END)
                for libro in libros_autor:
                    self.Listbox1.insert(tk.END, libro)

    def mostrar_libros_genero(self, event):
        genero_seleccionado = self.TCombobox1.get()
        genero_id = next((genero["id"] for genero in self.generos if genero["nombre"] == genero_seleccionado), None)
        if genero_id:
            libros_genero = [libro["titulo"] for libro in self.libros_titulos if libro["generoId"] == genero_id]
            self.Listbox1.delete(0, tk.END)
            for titulo in libros_genero:
                self.Listbox1.insert(tk.END, titulo)

    def mostrar_libros_anio(self, event):
        """Muestra libros publicados en el año seleccionado."""
        anio_seleccionado = self.TComboboxAñoPub.get()
        libros_anio = [libro["titulo"] for libro in self.libros_titulos if str(libro["anio_publicacion"]) == anio_seleccionado]
        self.Listbox1.delete(0, tk.END)
        for titulo in libros_anio:
            self.Listbox1.insert(tk.END, titulo)

    def mostrar_detalles(self, event):
        """Llena la información del libro seleccionado desde la Listbox."""
        seleccion = self.Listbox1.get(self.Listbox1.curselection())
        for libro in self.libros_titulos:
            if libro["titulo"] == seleccion:
                self.TEntry1.delete(0, tk.END)
                self.TEntry1.insert(0, libro["titulo"])
                self.TComboboxAutores.set(self.buscar_por_id(libro["autorId"], self.autores))
                self.TCombobox1.set(self.buscar_por_id(libro["generoId"], self.generos))
                self.TComboboxAñoPub.set(libro["anio_publicacion"])
                self.TEntry4.configure(state='normal')
                self.TEntry4.delete(0, tk.END)
                self.TEntry4.insert(0, libro["isbn"])
                self.TEntry4.configure(state='readonly')
                self.TEntry5.configure(state='normal')
                self.TEntry5.delete(0, tk.END)
                self.TEntry5.insert(0, self.buscar_por_id(libro["editorialId"], self.editoriales))
                self.TEntry5.configure(state='readonly')

    def buscar_por_id(self, id, lista):
        for elemento in lista:
            if elemento["id"] == id:
                return elemento["nombre"]
        return "Desconocido"

    def regresar(self):
        """Lógica para el botón Regresar."""
        print("Botón 'Regresar' presionado.")
        # Cerrar la ventana actual
        self.top.destroy()
        # Importar y llamar al método principal de navegacion.py
        import navegacion
        navegacion.start_up()

if __name__ == '__main__':
    root = tk.Tk()
    app = Toplevel1(top=root)
    root.mainloop()
