"""
	chamados_fase1 -> Recebem o resultado do particionamento do montante inicial, separados pela String "Encerrada", que é o que delimita cada chamado.
	
"""
import os, sys
import MySQLdb

class Chamado(object):

	def __init__(self,id_chamado,classe_chamado,usuario_solicitante,func_alocado,setor_solicitante,desc_chamado,data_solicitacao):
		self.id_chamado 			= id_chamado
		self.classe_chamado			= classe_chamado
		self.usuario_solicitante 	= usuario_solicitante
		self.func_alocado 			= func_alocado
		self.setor_solicitante 		= setor_solicitante
		self.desc_chamado 			= desc_chamado
		self.data_solicitacao		= data_solicitacao


databaseChamados = open("database_chamados.txt", "r").read()

chamados_fase1 = databaseChamados.split("Encerrada") #Quebra a lista de chamados em unidades de chamado

chamados_fase1.pop(-1) #Remoção do ultimo item, que no caso é vazio e gera inconsistencia

#print ("Chamados Catalogados: ",len(chamados_fase1))

cnx = MySQLdb.connect("localhost","root","root","testepy")
cnx.set_character_set("utf8mb4")
cur = cnx.cursor()



for i in chamados_fase1: # Realiza a extração da descrição do chamado. 
		
	string_particionada = []

	string_particionada.append(i.split("\n")[1].split("\t"))
	string_particionada.append(i.split("\n")[2].split("\t"))
	string_particionada.append(i.split("\n")[3].split("\t"))
		
	if len(string_particionada[2][0]) < 160 : #Metrica utilizada para restringir chamados muito extensos

		chamado = Chamado(	string_particionada[0][0],string_particionada[0][1],string_particionada[0][2],
							string_particionada[1][0],string_particionada[1][1],
							string_particionada[2][0],string_particionada[2][1]	)
	
		cur.execute('INSERT INTO CHAMADOS VALUES ("%d","%s","%s","%s","%s","%s","%s")' % (int(chamado.id_chamado),chamado.classe_chamado,chamado.usuario_solicitante,
																		chamado.func_alocado,chamado.setor_solicitante,chamado.desc_chamado,chamado.data_solicitacao))
		cnx.commit()
	

cur.close() 
cnx.close()

#print ("Total de chamados: ",len(chamados_fase1))











