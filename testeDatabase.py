import os, sys
import MySQLdb

con = MySQLdb.connect("localhost","root","root","testepy")

cur = con.cursor()

cur.execute("SELECT * FROM chamados WHERE func_alocado = 'Allan Moura Melão'")

print (cur.fetchone())
