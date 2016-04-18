import nltk, os, sys

class Chamado(object):

	def __init__(self,id_chamado, classe_chamado,):
		pass



databaseChamados = open("database_chamados.txt", "r").read()
chamados = databaseChamados.split("Encerrada") #Quebra a lista de chamados em unidades de chamado
print ("Chamados Catalogados: ",len(chamados))

descricaoChamado = [] #Lista com todas as descrições extraidas
classeChamado = []

for i in chamados: # Realiza a extração da descrição do chamado

	numero_c = i.split("\n")
	#print ("Classe: ",numero_c[1])
	numero_c[3].split(" ")
	desc_chamado = numero_c[3].split("\t")
	#print ("Descrição do chamado: ",desc_chamado[0])
	if len(desc_chamado[0]) < 160: #Metrica utilizada para restringir chamados muito extensos

		descricaoChamado.append(desc_chamado[0]) # Adiciona descrição extraida a lista de descrições
		#print ("Descrição do chamado: ",desc_chamado[0])


var = "Verificar computador que demora aligar... testar nobreak, testar tomada... se nao achar problema dizer para ele pedir uma revisão eletrica na tomada LOCAL: PROPESQ ao lado da PRPG"

print (len(var))
print ("Total de chamados: ",len(descricaoChamado))









