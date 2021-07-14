#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#LIBRERÍAS-------------------------------------------------------------------------
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
from os import listdir
from os.path import isfile, isdir
import Mod_ListaDeRenglones
#--------------------------------------------------------------------------
global renglones
global listaPrecodigo
global codigoSalida
global recursosLabel

#--------------------------------------------------------------------------
#directorioInicial=u"D:/Karpeta/1_-_Programacion/1_-_Python/Proyectos_-_Iniciados/Programas_2/Asistente_TKinter"
directorioInicial=os.getcwd()
directorioRecursos=directorioInicial+'/Recursos'
directorioVentanasCreadas=directorioInicial+'/Mis_ventanas'

preCodigo=Mod_ListaDeRenglones.ListaDeRenglones()
preCodigo.importar(directorioInicial+u"/Recursos/pre-codigo.txt")
postCodigo=Mod_ListaDeRenglones.ListaDeRenglones()
postCodigo.importar(directorioInicial+u"/Recursos/post-codigo.txt")
#codigoSalida=Mod_ListaDeRenglones.ListaDeRenglones()
#codigoSalida.renglones=listaPrecodigo.renglones
#--------------------------------------------------------------------------

#codigoSalida.exportar("Mis_ventanas/prueba.py")

#FUNCIONES-------------------------------------------------------------------------
def devuelveMedidas():
 info=ventana.winfo_geometry() 
 print(info)
def generar():

 codigoSalida=Mod_ListaDeRenglones.ListaDeRenglones()
 codigoSalida.renglones=preCodigo.renglones

 if boolLabel.get()==True:
  recursosLabel=Mod_ListaDeRenglones.ListaDeRenglones()
  recursosLabel.importar(directorioRecursos+u'/recursosLabel.txt')
  codigoSalida.renglones=codigoSalida.renglones+recursosLabel.renglones

 if boolEntry.get()==True:
  recursosEntry=Mod_ListaDeRenglones.ListaDeRenglones()
  recursosEntry.importar(directorioRecursos+u'/recursosEntry.txt')
  codigoSalida.renglones=codigoSalida.renglones+recursosEntry.renglones
 
 if boolButton.get()==True:
  recursosButton=Mod_ListaDeRenglones.ListaDeRenglones()
  recursosButton.importar(directorioRecursos+u'/recursosButton.txt')
  codigoSalida.renglones=codigoSalida.renglones+recursosButton.renglones

 if boolComboBox.get()==True:
  recursosComboBox=Mod_ListaDeRenglones.ListaDeRenglones()
  recursosComboBox.importar(directorioRecursos+u'/recursosComboBox.txt')
  codigoSalida.renglones=codigoSalida.renglones+recursosComboBox.renglones

 if boolSpinBox.get()==True:
  recursosSpinBox=Mod_ListaDeRenglones.ListaDeRenglones()
  recursosSpinBox.importar(directorioRecursos+u'/recursosSpinBox.txt')
  codigoSalida.renglones=codigoSalida.renglones+recursosSpinBox.renglones

 if boolCheckButton.get()==True:
  recursosCheckButton=Mod_ListaDeRenglones.ListaDeRenglones()
  recursosCheckButton.importar(directorioRecursos+u'/recursosCheckButton.txt')
  codigoSalida.renglones=codigoSalida.renglones+recursosCheckButton.renglones

 if boolImagen.get()==True:
  recursosImagen=Mod_ListaDeRenglones.ListaDeRenglones()
  recursosImagen.importar(directorioRecursos+u'/recursosImagen.txt')
  codigoSalida.renglones=codigoSalida.renglones+recursosImagen.renglones

 codigoSalida.renglones=codigoSalida.renglones+postCodigo.renglones

 codigoSalida.exportar(directorioVentanasCreadas+u'/'+nombreArchivo.get()+'.py')

#SET VENTANA-------------------------------------------------------------------------
colorFondo="#424242"
dimensiones="528x320"
colorLetras="#339933"
colorFondoBoton="#424242"
titulo="Asistente TKinter"
ventana=Tk()

#INICIO VENTANA-------------------------------------------------------------------------
ventana.title(titulo)
ventana.geometry(dimensiones)
ventana.configure(background=colorFondo)

#CONTENIDO DE LA VENTANA---------------------------------------------------------------------
#ELEMENTOS---------------------------------------------------------------------

etiquetaElementos=Label(ventana, text="_Elementos__", fg=colorLetras, background=colorFondo)
etiquetaElementos.pack()
etiquetaElementos.place(x=20, y=20)

#-------------------------------------------------------------------------
boolLabel=BooleanVar()
checkLabel=Checkbutton(ventana, text="Label", fg=colorLetras, background=colorFondo, variable=boolLabel)
checkLabel.pack()
checkLabel.place(x=20, y=50)

#-------------------------------------------------------------------------
boolEntry=BooleanVar()
checkEntry=Checkbutton(ventana, text="Entry", fg=colorLetras, background=colorFondo, variable=boolEntry)
checkEntry.pack()
checkEntry.place(x=20, y=80)

#-------------------------------------------------------------------------
boolButton=BooleanVar()
checkButton=Checkbutton(ventana, text="Button", fg=colorLetras, background=colorFondo, variable=boolButton)
checkButton.pack()
checkButton.place(x=20, y=110)

#-------------------------------------------------------------------------
boolComboBox=BooleanVar()
checkComboBox=Checkbutton(ventana, text="ComboBox", fg=colorLetras, background=colorFondo, variable=boolComboBox)
checkComboBox.pack()
checkComboBox.place(x=20, y=140)

#-------------------------------------------------------------------------
boolSpinBox=BooleanVar()
checkSpinBox=Checkbutton(ventana, text="SpinBox", fg=colorLetras, background=colorFondo, variable=boolSpinBox)
checkSpinBox.pack()
checkSpinBox.place(x=20, y=170)

#-------------------------------------------------------------------------
boolCheckButton=BooleanVar()
checkCheckButton=Checkbutton(ventana, text="CheckButton", fg=colorLetras, background=colorFondo, variable=boolCheckButton)
checkCheckButton.pack()
checkCheckButton.place(x=20, y=200)

#-------------------------------------------------------------------------
boolImagen=BooleanVar()
checkImagen=Checkbutton(ventana, text="Imagen", foreground=colorLetras, background=colorFondo, variable=boolImagen)
checkImagen.pack()
checkImagen.place(x=20, y=230)

#MEDIDAS VENTANA-------------------------------------------------------------------
botonMedidas=Button(ventana, text="Medidas", command=devuelveMedidas, foreground=colorLetras, background=colorFondoBoton, width=15, height=2)
botonMedidas.pack()
botonMedidas.place(x=20, y=260)

#AJUSTES------------------------------------------------------------------
etiquetaAjustes=Label(ventana, text="_Ajustes__", fg=colorLetras, background=colorFondo)
etiquetaAjustes.pack()
etiquetaAjustes.place(x=275, y=20)

#-------------------------------------------------------------------------
etiquetaNombreArchivo=Label(ventana, text="_Nombre de archivo__", fg=colorLetras, background=colorFondo)
etiquetaNombreArchivo.pack()
etiquetaNombreArchivo.place(x=245, y=50)

nombreArchivo=StringVar()
nombreArchivoCaja=Entry(ventana, textvariable=nombreArchivo)
nombreArchivoCaja.place(x=385, y=50)

#GENERAR-------------------------------------------------------------------
botonGenerar=Button(ventana, text="► Generar", command=generar, foreground=colorLetras, background=colorFondoBoton, width=15, height=2)
botonGenerar.pack()
botonGenerar.place(x=390, y=80)

#-------------------------------------------------------------------------
imagen=PhotoImage(file=directorioInicial+u"/Imagenes/img.png")
fondo=Label(ventana, image=imagen, background="#424242").place(x=410, y=200)
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------


# FIN VENTANA--------------------------------------------------------------
ventana.mainloop()

