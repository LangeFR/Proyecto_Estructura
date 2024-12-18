#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Nov 10, 2024 12:11:08 PM EST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os

_location = os.path.dirname(__file__)

import navegacion_support

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black'
_tabfg2 = 'white'
_bgmode = 'light'
_tabbg1 = '#d9d9d9'
_tabbg2 = 'gray40'

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
        return
    try:
        navegacion_support.root.tk.call('source', os.path.join(_location, 'themes', 'default.tcl'))
    except:
        pass
    style = ttk.Style()
    style.theme_use('default')
    style.configure('.', font="TkDefaultFont")
    if sys.platform == "win32":
        style.theme_use('winnative')
    _style_code_ran = 1


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+468+138")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(True, True)
        top.title("Menú principal")
        top.configure(background="#98e4fe")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        #top.state('zoomed')  # Activa el modo maximizado
        #top.update_idletasks()  # Asegura que las dimensiones se ajusten antes de renderizar

        self.top = top

        # Contenedor principal (Frame)
        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.15, rely=0.15, relheight=0.7, relwidth=0.7)
        
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#9b0a64")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#000000")

        # Estilo
        _style_code()

        # Label estilizado
        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.2, rely=0.05, relheight=0.15, relwidth=0.6)
        self.TLabel1.configure(background="#9b0a64")
        self.TLabel1.configure(foreground="#ffffff")
        self.TLabel1.configure(font="-family {Segoe UI} -size 16 -weight bold")
        self.TLabel1.configure(anchor='center')
        self.TLabel1.configure(text="Selecciona una opción")

        # Botón "Añadir libro"
        self.btnAnadir = tk.Button(self.Frame1)
        self.btnAnadir.place(relx=0.35, rely=0.3, height=36, width=120)
        #self.btnAnadir.place(relx=0.5, rely=0.3, anchor="center", height=36, width=120)
        self.btnAnadir.configure(activebackground="#d9d9d9")
        self.btnAnadir.configure(activeforeground="black")
        self.btnAnadir.configure(background="#ffcc00")
        self.btnAnadir.configure(command=navegacion_support.doAnadir)
        self.btnAnadir.configure(disabledforeground="#a3a3a3")
        self.btnAnadir.configure(font="-family {Segoe UI} -size 10")
        self.btnAnadir.configure(foreground="#000000")
        self.btnAnadir.configure(text="Añadir libro")

        # Botón "Visualizar"
        self.btnVisualizar = tk.Button(self.Frame1)
        self.btnVisualizar.place(relx=0.35, rely=0.5, height=36, width=120)
        #self.btnVisualizar.place(relx=0.5, rely=0.5, anchor="center", height=36, width=120)
        self.btnVisualizar.configure(activebackground="#d9d9d9")
        self.btnVisualizar.configure(activeforeground="black")
        self.btnVisualizar.configure(background="#ffcc00")
        self.btnVisualizar.configure(command=navegacion_support.doVisualizar)
        self.btnVisualizar.configure(disabledforeground="#a3a3a3")
        self.btnVisualizar.configure(font="-family {Segoe UI} -size 10")
        self.btnVisualizar.configure(foreground="#000000")
        self.btnVisualizar.configure(text="Visualizar")

        # Botón "Consultas"
        self.btnConsultar = tk.Button(self.Frame1)
        self.btnConsultar.place(relx=0.35, rely=0.7, height=36, width=120)
        #self.btnConsultar.place(relx=0.5, rely=0.7, anchor="center", height=36, width=120)
        self.btnConsultar.configure(activebackground="#d9d9d9")
        self.btnConsultar.configure(activeforeground="black")
        self.btnConsultar.configure(background="#ffcc00")
        self.btnConsultar.configure(command=navegacion_support.doConsultar)
        self.btnConsultar.configure(disabledforeground="#a3a3a3")
        self.btnConsultar.configure(font="-family {Segoe UI} -size 10")
        self.btnConsultar.configure(foreground="#000000")
        self.btnConsultar.configure(text="Consultas")


def start_up():
    navegacion_support.main()


if __name__ == '__main__':
    navegacion_support.main()


