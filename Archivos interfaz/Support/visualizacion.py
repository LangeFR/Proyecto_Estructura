#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Nov 11, 2024 04:34:41 PM EST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import visualizacion_support

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
    try: visualizacion_support.root.tk.call('source',
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

        top.geometry("600x450+436+171")
        top.minsize(120, 1)
        top.maxsize(1540, 845)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#98e4fe")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top
        self.combobox = tk.StringVar()

        self.Canvas1 = tk.Canvas(self.top)
        self.Canvas1.place(relx=0.483, rely=0.244, relheight=0.562
                , relwidth=0.488)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(cursor="fleur")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="#000000")
        self.Canvas1.configure(insertbackground="#000000")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#d9d9d9")
        self.Canvas1.configure(selectforeground="black")

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.033, rely=0.333, relheight=0.367
                , relwidth=0.408)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#9b0a64")
        self.Frame1.configure(cursor="fleur")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#000000")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.041, rely=0.242, height=21, width=84)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#9b0a64")
        self.Label1.configure(compound='left')
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''Visualizar por:''')

        _style_code()
        self.TCombobox1 = ttk.Combobox(self.Frame1)
        self.TCombobox1.place(relx=0.408, rely=0.242, relheight=0.115
                , relwidth=0.559)
        self.TCombobox1.configure(textvariable=self.combobox)
        self.TCombobox1.configure(takefocus="")

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.082, rely=0.424, height=26, width=57)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#fec210")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="black")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''Ver grafo''')

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.694, rely=0.788, height=26, width=57)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#f97db1")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="black")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="#000000")
        self.Button2.configure(text='''Regresar''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.433, rely=0.044, height=21, width=74)
        self.Label2.configure(activebackground="#d9d9d9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#98e4fe")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="black")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="#000000")
        self.Label2.configure(text='''Visualización''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

def start_up():
    visualizacion_support.main()

if __name__ == '__main__':
    visualizacion_support.main()




