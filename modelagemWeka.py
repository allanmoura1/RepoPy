import MySQLdb, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from unicodedata import normalize

def remover_acentos(txt):	# Função de remoção de acentos

	return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')

listaClasses = {}		# Dicionário de Classes com a frequência das palavras que aparecem

stop_words 	= set(stopwords.words("portuguese"))  # Seta idioma de dicionário de stopwords
tokenizer 	= RegexpTokenizer(r'\w+')			  # Expressão regular para remover pontuação
stemmer 	= nltk.stem.RSLPStemmer()			  # 
cnx 		= MySQLdb.connect("localhost","root","root","testepy")	# Dados para conexão ao banco de dados
cur 		= cnx.cursor()						  # Cursor da conexão

cnx.set_character_set("utf8mb4")				  # Codificação 
cur.execute("SELECT classe_chamado,desc_chamado FROM CHAMADOS")	# Query a ser executada no banco de dados

dados = cur.fetchall()				# Recebe Lista de chamados, com a classe e as descrições

for classe, chamado in dados:		# Percorre a lista de dados (classe e chamando) recebidos do Banco de dados

	descricaoTokenizada = tokenizer.tokenize(chamado)

	for i in descricaoTokenizada: 	# Percorre o vetor da descrição tokenizada

		if i not in stop_words: 	# Verifica se palavra existe no dicionário de stop words

			if not classe in listaClasses.keys():		# Verifica se a classe já existe no dicionario, caso não exista, é adicionada uma lista vazia
				listaClasses[classe] = []

			listaClasses[classe].append(stemmer.stem(remover_acentos(i.lower())))		# Caso exista, a palavra é adicionada a lista de palavras da classe, com os acentos removidos e em caixa baixa

print ("Quantidade de classes: ", len(listaClasses))

for classe, listaPalavras in listaClasses.items():		# Percorre o dicionário de classes 
	print ("Classe: ",classe)
	fdist = nltk.FreqDist(listaPalavras) 				# Armazena a frequência das palavras de acordo com a lista de cada classe

	for palavra, frequencia in fdist.most_common(5): 	# Recebe as 5 palavras mais comuns em cada classe e exibe
		print('%s: %d' % (palavra, frequencia))

cur.close()	# Encerra Cursor
cnx.close()	# Encerra Conexão