#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

directorio=raw_input('Introduce un directorio: ')
if not os.access(directorio,0):
	print 'El directorio no existe.'
	exit()

letra=raw_input('Introduce una letra: ')
ficheros=os.listdir(directorio)
for archivo in ficheros:
	if archivo.count(letra)!=0:
		print archivo
	else:
		print 'Ningún archivo contiene la letra '+str(letra)+'.'
		exit()
