#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

print sys.argv[0]+':'
if len(sys.argv) !=4:
	print 'Argumento/s incorrecto/s.'
	exit()
print 'Iniciales: '+(sys.argv[1][0]+sys.argv[2][0]+sys.argv[3][0]).upper()+'.'

#Otra forma
iniciales=sys.argv[1][0]+sys.argv[2][0]+sys.argv[3][0]
print 'Iniciales: '+iniciales.upper()+'.'
