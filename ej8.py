#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

directorio=raw_input('Introduce un directorio: ')
if not os.access(directorio,0):
	print 'El directorio no existe.'
	exit()

ficheros=os.listdir(directorio)
for archivo in ficheros:
	if archivo[-3:]=='.sh':
		print archivo
#Otra forma
x=0
while x<len(ficheros):
        if ficheros[x][-3:]=='.sh':
                print ficheros[x]
        x=x+1
