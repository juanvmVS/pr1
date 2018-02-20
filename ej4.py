#!/usr/bin/env python
# -*- coding: utf-8 -*-
x=int(raw_input('Introduce tu año de nacimiento: '))

edad=2018-x
if edad<0:
	print 'No seas mentiroso!'
elif edad>-1 and edad<18:
	print 'Eres menor de edad.'
elif edad>17 and edad<31:
	print 'Eres joven.'
elif edad>30 and edad<46:
	print 'Eres maduro.'
else:
	print 'Viejuno!'
