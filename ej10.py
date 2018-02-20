#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

print sys.argv[0]+':'
if len(sys.argv) !=2:
	print 'Argumento/s incorrecto/s.'
	exit()
print 'En mayúsculas: '+sys.argv[1].upper()
