# -*- coding: utf-8 -*-

def ftp():
	from ftplib import FTP
	ftp=FTP()
	ftp.connect('192.168.1.59',23,-999)
	ftp.login('oracle','oracle')
	
