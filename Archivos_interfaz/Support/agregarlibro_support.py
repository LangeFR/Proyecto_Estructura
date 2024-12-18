#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Nov 16, 2024 11:04:44 AM EST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import agregarlibro

_debug = True # False to eliminate debug printing from callback functions.

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = agregarlibro.Toplevel1(_top1)
    root.mainloop()

def doAgregar(*args):
    if _debug:
        print('agregarlibro2_support.doAgregar')
        for arg in args:
            print ('    another arg:', arg)
        sys.stdout.flush()

def doRegresar(*args):
    if _debug:
        print('agregarlibro2_support.doRegresar')
        for arg in args:
            print ('    another arg:', arg)
        sys.stdout.flush()

if __name__ == '__main__':
    agregarlibro.start_up()




