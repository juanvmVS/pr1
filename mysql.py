#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector

cnx=mysql.connector.connect(user='root',database='sakila',host='192.168.1.59',password='oracle')
cursor=cnx.cursor()

query=("SELECT  city from city")

cursor.execute(query)

for ciudad in cursor:
	print ciudad
cursor.close()
cnx.close()
