# -*- coding: utf-8 -*-

import sys

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
