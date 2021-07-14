#!/usr/bin/env python
# -*- coding: utf-8 -*-

#LIBRERÍAS-----------------------------------------------------------------------
import os

#CLASE PRINCIPAL-----------------------------------------------------------------
class ListaDeRenglones():

 def __init__(self):
  self.renglones=[]

#La lista "renglones" es el dato más importante para definir en éste módulo.
#A partir de ésta lista podemos exportar.
#Si importarmos, lo hacemos en ésta misma lista.
#Si queremos utilizar una lista generada dentro del programa
#bastará con asignarla como valor de "renglones".
#Ej:
#MiObjetoRenglon.renglones=miLista

#MÉTODO: IMPORTAR LISTA DESDE ARCHIVO TXT------------------------------------------------------
 def importar(self, archivo):
  self.cargarArchivo(archivo)

#MÉTODO: CARGAR ARCHIVO EN MEMORIA----------------------------------------------------------
 def cargarArchivo(self, archivo):

#principal-----------------------------------------------------------------------
  f=open(archivo,"r")
  posicion=0

  for renglon in f:

   if renglon=="":    #Éste es un arreglo para las líneas que están vacías
    self.renglones[posicion:posicion]=["\n"]
   else: 
    self.renglones[posicion:posicion]=[renglon] #Copia el renglon incluyendo el salto de línea
   posicion=posicion+1

  f.close()

#arreglo------------------------------------------------------------------------
  ultimoIndice=len(self.renglones)-1
  copia=self.renglones
  indice=0

  while indice<ultimoIndice: # Éste arreglo elimina los saltos de todas las líneas, exceptuando la última

   if copia[indice][-1:]=="\n":
    self.renglones[indice]=(self.renglones[indice][:-1])
   indice=indice+1

#MÉTODO: EXPORTAR LA LISTA COMO ARCHIVO TXT------------------------------------------------------
 def exportar(self, archivo):
  f=open(archivo,"w")

  ultimoIndice=len(self.renglones)-1
  indice=0

  while indice<ultimoIndice:

   f.write(str(self.renglones[indice])+"\n") # Añade salto de líneas hasta la anteúltima linea...,
   indice=indice+1

  f.write(str(self.renglones[indice])) # A la última línea la deja con el salto original
  f.close()

#-------------------------------------------------------------------------------