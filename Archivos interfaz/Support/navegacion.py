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
import os.path

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
    if _style_code_ran: return        
    try: navegacion_support.root.tk.call('source',
                os.path.join(_location, 'themes', 'default.tcl'))
    except: pass
    style = ttk.Style()
    style.theme_use('default')
    style.configure('.', font = "TkDefaultFont")
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
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#98e4fe")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.15, rely=0.111, relheight=0.7, relwidth=0.708)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#9b0a64")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#000000")

        _style_code()
        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.353, rely=0.063, height=17, width=143)
        self.TLabel1.configure(background="#9b0a64")
        self.TLabel1.configure(foreground="#ffffff")
        self.TLabel1.configure(font="-family {Segoe UI} -size 9")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Selecciona una opción''')
        self.TLabel1.configure(compound='left')

        self.btnVisualizar = tk.Button(self.Frame1)
        self.btnVisualizar.place(relx=0.4, rely=0.349, height=36, width=77)
        self.btnVisualizar.configure(activebackground="#d9d9d9")
        self.btnVisualizar.configure(activeforeground="black")
        self.btnVisualizar.configure(background="#ffcc00")
        self.btnVisualizar.configure(command=navegacion_support.doVisualizar)
        self.btnVisualizar.configure(disabledforeground="#a3a3a3")
        self.btnVisualizar.configure(font="-family {Segoe UI} -size 9")
        self.btnVisualizar.configure(foreground="#000000")
        self.btnVisualizar.configure(highlightbackground="#d9d9d9")
        self.btnVisualizar.configure(highlightcolor="#000000")
        self.btnVisualizar.configure(text='''Visualizar''')

        self.btnConsultar = tk.Button(self.Frame1)
        self.btnConsultar.place(relx=0.4, rely=0.54, height=36, width=77)
        self.btnConsultar.configure(activebackground="#d9d9d9")
        self.btnConsultar.configure(activeforeground="black")
        self.btnConsultar.configure(background="#ffcc00")
        self.btnConsultar.configure(command=navegacion_support.doConsultar)
        self.btnConsultar.configure(disabledforeground="#a3a3a3")
        self.btnConsultar.configure(font="-family {Segoe UI} -size 9")
        self.btnConsultar.configure(foreground="#000000")
        self.btnConsultar.configure(highlightbackground="#d9d9d9")
        self.btnConsultar.configure(highlightcolor="#000000")
        self.btnConsultar.configure(text='''Consultas''')

        self.btnOrdenar = tk.Button(self.Frame1)
        self.btnOrdenar.place(relx=0.4, rely=0.73, height=36, width=77)
        self.btnOrdenar.configure(activebackground="#d9d9d9")
        self.btnOrdenar.configure(activeforeground="black")
        self.btnOrdenar.configure(background="#ffcc00")
        self.btnOrdenar.configure(command=navegacion_support.doOrdenar)
        self.btnOrdenar.configure(disabledforeground="#a3a3a3")
        self.btnOrdenar.configure(font="-family {Segoe UI} -size 9")
        self.btnOrdenar.configure(foreground="#000000")
        self.btnOrdenar.configure(highlightbackground="#d9d9d9")
        self.btnOrdenar.configure(highlightcolor="#000000")
        self.btnOrdenar.configure(text='''Ordenar''')

        self.btnAnadir = tk.Button(self.Frame1)
        self.btnAnadir.place(relx=0.4, rely=0.159, height=36, width=77)
        self.btnAnadir.configure(activebackground="#d9d9d9")
        self.btnAnadir.configure(activeforeground="black")
        self.btnAnadir.configure(background="#ffcc00")
        self.btnAnadir.configure(command=navegacion_support.doAnadir)
        self.btnAnadir.configure(disabledforeground="#a3a3a3")
        self.btnAnadir.configure(font="-family {Segoe UI} -size 9")
        self.btnAnadir.configure(foreground="#000000")
        self.btnAnadir.configure(highlightbackground="#d9d9d9")
        self.btnAnadir.configure(highlightcolor="#000000")
        self.btnAnadir.configure(text='''Añadir libro''')

def start_up():
    navegacion_support.main()

if __name__ == '__main__':
    navegacion_support.main()



