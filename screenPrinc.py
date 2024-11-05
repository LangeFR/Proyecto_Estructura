import tkinter as tk
from tkinter import ttk

# Initialize main window
root = tk.Tk()
root.title("Library Manager")
root.geometry("600x350")
root.configure(bg="#A3D0F8")

# Apply styles for Comboboxes (rounded effect)
style = ttk.Style()
style.theme_use("clam")
style.configure("TCombobox", fieldbackground="#F0F8FF", background="#FFC100", borderwidth=1, relief="flat")

# Title
title_label = tk.Label(root, text="¿Qué deseas hacer?", font=("Arial", 16, "bold"), bg="#A3D0F8")
title_label.pack(pady=10)

# Frame for controls
controls_frame = tk.Frame(root, bg="#8B1C62", width=250, height=250, bd=2, relief="groove")
controls_frame.pack_propagate(False)
controls_frame.place(x=30, y=60)

# Dropdown options
options = ["Opción 1", "Opción 2", "Opción 3"]

# Almacenar section
almacenar_label = tk.Label(controls_frame, text="Almacenar por:", font=("Arial", 12), bg="#FFC100")
almacenar_label.pack(pady=(15, 5))
almacenar_combo = ttk.Combobox(controls_frame, values=options, state="readonly", width=15, style="TCombobox")
almacenar_combo.set("Seleccionar")
almacenar_combo.pack(pady=5)

# Encontrar section
encontrar_label = tk.Label(controls_frame, text="Encontrar por:", font=("Arial", 12), bg="#FFC100")
encontrar_label.pack(pady=5)
encontrar_combo = ttk.Combobox(controls_frame, values=options, state="readonly", width=15, style="TCombobox")
encontrar_combo.set("Seleccionar")
encontrar_combo.pack(pady=5)

# Ordenar section
ordenar_label = tk.Label(controls_frame, text="Ordenar por:", font=("Arial", 12), bg="#FFC100")
ordenar_label.pack(pady=5)
ordenar_combo = ttk.Combobox(controls_frame, values=options, state="readonly", width=15, style="TCombobox")
ordenar_combo.set("Seleccionar")
ordenar_combo.pack(pady=5)

# Button for adding a book
add_book_button = tk.Button(controls_frame, text="Añadir un libro", bg="#FF0099", fg="white", font=("Arial", 10, "bold"), width=15)
add_book_button.pack(pady=15)

# Button for new book inscription
inscription_button = tk.Button(controls_frame, text="Inscribir nuevo libro", bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=15)
inscription_button.pack(pady=5)

# Frame for visualization
visualization_frame = tk.Frame(root, bg="#8B1C62", width=200, height=250, bd=2, relief="groove")
visualization_frame.pack_propagate(False)
visualization_frame.place(x=350, y=60)

visualization_label = tk.Label(visualization_frame, text="VISUALIZACIÓN", font=("Arial", 12), bg="white", width=15, height=8)
visualization_label.pack(expand=True)

# Run the application
root.mainloop()
