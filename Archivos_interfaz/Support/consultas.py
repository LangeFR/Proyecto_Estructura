import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from adapters.consultas_adapter import ConsultasAdapter
import tkinter as tk
import tkinter.ttk as ttk


class Toplevel1:
    def __init__(self, top=None):
        top.geometry("600x500+597+181")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1, 1)
        top.title("Gestión de Libros")
        top.configure(background="#98e4fe")

        self.top = top
        self.filtro_activo = None

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

        # Listbox para mostrar información
        self.Listbox1 = tk.Listbox(self.Frame1)
        self.Listbox1.place(relx=0.532, rely=0.15, relheight=0.6, relwidth=0.393)
        self.Listbox1.bind("<Double-1>", self.mostrar_detalles)

        # Botón Regresar
        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.128, rely=0.85, height=26, width=80)
        self.Button1.configure(background="#fdab02", text='Regresar', command=self.regresar)

        # Botón Nueva Búsqueda
        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.3, rely=0.85, height=26, width=120)
        self.Button2.configure(background="#fdab02", text='Nueva Búsqueda', command=self.limpiar_busqueda)

        # Llenar Combobox de Autores
        self.TComboboxAutores['values'] = self.adapter.autores_nombres

        # Llenar Combobox de Géneros
        self.TCombobox1['values'] = self.adapter.generos_nombres

        # Llenar Combobox de Años de Publicación
        self.TComboboxAñoPub['values'] = self.adapter.años_publicacion

        # Inicializar filtro activo
        self.filtro_activo = None

    # Métodos que interactúan con el adaptador
    def autocompletar_titulos(self, event):
        entrada = self.TEntry1.get()
        coincidencias = self.adapter.busqueda_binaria_titulos(entrada)
        self.Listbox1.delete(0, tk.END)
        for titulo in coincidencias:
            self.Listbox1.insert(tk.END, titulo)

    def filtrar_autores(self, event):
        entrada = self.TComboboxAutores.get().lower()
        coincidencias = [autor for autor in self.adapter.autores_nombres if entrada in autor.lower()]
        self.TComboboxAutores['values'] = coincidencias

    def mostrar_libros_autor(self, event):
        autor_seleccionado = self.TComboboxAutores.get()
        autor_id = next((autor["id"] for autor in self.adapter.autores if autor["nombre"] == autor_seleccionado), None)
        if autor_id:
            libros_autor = [libro["titulo"] for libro in self.adapter.libros_titulos if libro["autorId"] == autor_id]
            self.Listbox1.delete(0, tk.END)
            for titulo in libros_autor:
                self.Listbox1.insert(tk.END, titulo)

    def mostrar_libros_genero(self, event):
        genero_seleccionado = self.TCombobox1.get()
        genero_id = next((genero["id"] for genero in self.adapter.generos if genero["nombre"] == genero_seleccionado), None)
        if genero_id:
            generos_hijos = self.adapter.obtener_generos_hijos(genero_id)
            ids_generos = [genero_id] + [g["id"] for g in generos_hijos]
            libros_genero = [libro["titulo"] for libro in self.adapter.libros_titulos if libro["generoId"] in ids_generos]
            self.Listbox1.delete(0, tk.END)
            for titulo in libros_genero:
                self.Listbox1.insert(tk.END, titulo)

    def mostrar_libros_anio(self, event):
        anio_seleccionado = self.TComboboxAñoPub.get()
        if anio_seleccionado in self.adapter.hash_libros_por_anio:
            libros_anio = self.adapter.hash_libros_por_anio[anio_seleccionado]
        else:
            libros_anio = []
        self.Listbox1.delete(0, tk.END)
        for titulo in libros_anio:
            self.Listbox1.insert(tk.END, titulo)

    def mostrar_detalles(self, event):
        seleccion = self.Listbox1.get(self.Listbox1.curselection())
        for libro in self.adapter.libros_titulos:
            if libro["titulo"] == seleccion:
                # Llenar campos
                self.TEntry1.delete(0, tk.END)
                self.TEntry1.insert(0, libro["titulo"])
                self.TComboboxAutores.set(self.adapter.buscar_por_id(libro["autorId"], self.adapter.autores))
                self.TCombobox1.set(self.adapter.buscar_por_id(libro["generoId"], self.adapter.generos))
                self.TComboboxAñoPub.set(libro["anio_publicacion"])
                self.TEntry4.configure(state='normal')
                self.TEntry4.delete(0, tk.END)
                self.TEntry4.insert(0, libro["isbn"])
                self.TEntry4.configure(state='readonly')
                self.TEntry5.configure(state='normal')
                self.TEntry5.delete(0, tk.END)
                self.TEntry5.insert(0, self.adapter.buscar_por_id(libro["editorialId"], self.adapter.editoriales))
                self.TEntry5.configure(state='readonly')

                if self.filtro_activo != "titulo":
                    self.TEntry1.delete(0, tk.END)
                    self.TEntry1.insert(0, libro["titulo"])

        self.desactivar_todos_los_filtros()

    def activar_filtro(self, filtro):
        """Activa un filtro y limpia los demás."""
        self.filtro_activo = filtro
        print(f"Filtro activado: {filtro}")

    def desactivar_todos_los_filtros(self):
        """Desactiva todos los filtros."""
        self.TEntry1.configure(state="disabled")
        self.TComboboxAutores.configure(state="disabled")
        self.TCombobox1.configure(state="disabled")
        self.TComboboxAñoPub.configure(state="disabled")

    def limpiar_busqueda(self):
        """Limpia todos los campos de búsqueda y detalles del libro."""
        # Limpiar campos de entrada
        self.TEntry1.configure(state="normal")
        self.TEntry1.delete(0, tk.END)
        self.TComboboxAutores.set("")
        self.TCombobox1.set("")
        self.TComboboxAñoPub.set("")

        # Limpiar los detalles del libro seleccionado
        self.TEntry4.configure(state='normal')
        self.TEntry4.delete(0, tk.END)
        self.TEntry4.configure(state='readonly')
        self.TEntry5.configure(state='normal')
        self.TEntry5.delete(0, tk.END)
        self.TEntry5.configure(state='readonly')

        self.Listbox1.delete(0, tk.END)

        # Restablecer el filtro activo
        self.filtro_activo = None
        print("Campos de búsqueda limpiados.")

        # Volver a habilitar los filtros
        self.activar_filtro_por_nombre()

    def activar_filtro_por_nombre(self):
        """Habilita los filtros nuevamente según el campo activo."""
        if self.filtro_activo == "titulo":
            self.TEntry1.configure(state="normal")
        elif self.filtro_activo == "autor":
            self.TComboboxAutores.configure(state="normal")
        elif self.filtro_activo == "genero":
            self.TCombobox1.configure(state="normal")
        elif self.filtro_activo == "anio":
            self.TComboboxAñoPub.configure(state="normal")
        else:
            # Habilitar todos los campos si no hay un filtro activo
            self.TEntry1.configure(state="normal")
            self.TComboboxAutores.configure(state="normal")
            self.TCombobox1.configure(state="normal")
            self.TComboboxAñoPub.configure(state="normal")

    def buscar_por_id(self, id, lista):
        return self.adapter.buscar_por_id(id, lista)

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
