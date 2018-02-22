# -*- coding: utf-8 -*-

import sys
import os

def saludar(saludo):
	print saludo

def iniciales(nom,ap1,ap2):
	return 'Iniciales: '+(nom[0]+ap1[0]+ap2[0]).upper()+'.'

def siglas(nom,*apellidos):
	if len(apellidos)<1:
		return 'Falta al menos un apellido.'
	inic=nom[0]
	for apellido in apellidos:
		inic=inic+apellido[0]
	return inic.upper()

#Recibe un directorio. Si lo crea devuelve 0. Si no 1.
def crdir(directorio):
	if os.access(directorio,0):
		return 1
	else:
		os.mkdir(directorio)
		return 0

#Recibe un directorio y muestra los ficheros (no directorios) y el tamaño de cada item.
def lista_ficheros(ruta):
	if not os.access(ruta,0):
		print 'No existe.'
		exit()
	lista=os.listdir(ruta)
	for archivo in lista:
		rt=ruta+'/'+archivo
		if os.path.isfile(rt):
			print archivo+' ---> '+str(os.path.getsize(rt))

#Recibe un directorio y muestra los ficheros (no directorios) mayores del tamaño indicado en K, M o G y muestra el tamaño de cada item.
def lista_fich_tam(ruta,tam):
	if not os.access(ruta,0):
		print 'No existe.'
		exit()
	if tam[-1].upper() not in ('K','M','G'):
		print 'Tamaño incorrecto.'
		exit()
	lista=os.listdir(ruta)
	t=int(tam[:-1])
	if tam[-1]=='K':
		bt=t*1024
	if tam[-1]=='M':
		bt=t*(1024**2)
	else:
		bt=t*(1024**3)
	for archivo in lista:
		rt=ruta+'/'+archivo
		if os.path.isfile(rt) and os.path.getsize(rt)>bt:
			print archivo+' ---> '+str(os.path.getsize(rt))

#Muestra el contenido de un archivo.
def cat(arch):
	if not os.access(arch,0):
		print 'No existe.'
		exit()
	if os.path.isfile(arch):
		archivo=open(arch,'r')
		content=archivo.read()
		print content
		archivo.close()
	else:
		print 'No es un archivo.'
		exit()

#Similar a grep.
def grep(fichero,texto):
	if not os.access(fichero,0):
		print 'No existe.'
		exit ()
	if os.path.isfile(fichero):
		archivo=open(fichero,'r')
		for linea in archivo.readlines():
			if linea.count(texto)>0:
				print linea[:-1]
		archivo.close()
	else:
		print 'No es un archivo.'
		exit ()

#Similar a cp.
def cp(forig,fdest):
	if not os.access(forig,0):
		print 'No existe el orígen.'
		exit()
	if os.access(fdest,0):
		print 'Ya existe destino.'
		exit()
	if not os.path.isfile(forig):
		print 'No es un archivo.'
		exit()
	origen=open(forig,'r')
	destino=open(fdest,'w')
	destino.writelines(origen)
	origen.close()
	destino.close()

#Copia solo las líneas con el texto indicado en el fichero destino en modo append.
def cp_grep(forig,fdest,texto):
	if not os.access(forig,0):
		print 'No existe el orígen.'
		exit()
	if not os.path.isfile(forig):
		print 'No es un archivo.'
		exit()
	origen=open(forig,'r')
	destino=open(fdest,'a')
	for linea in origen.readlines():
		if linea.count(texto)>0:
			destino.write(linea)	
	origen.close()
	destino.close()

