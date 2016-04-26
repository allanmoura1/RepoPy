from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

exemplo_texto = "Esse é um exemplo de filtragem de stopwords. Mantenha-se atento a todas as alterações que possam vir a aparecer"

stop_words = set(stopwords.words("portuguese"))

words = word_tokenize(exemplo_texto)

sentencas_filtradas = []

for w in words:
	if w not in stop_words:
		sentencas_filtradas.append(w)

#print (sentencas_filtradas)

#print (sentencas_filtradas)

print (sentencas_filtradas)

