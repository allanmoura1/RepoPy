from nltk.tokenize import sent_tokenize, word_tokenize

import os, sys

texto_exemplo = open("loren.txt").read()

print(word_tokenize(texto_exemplo))

for i in word_tokenize(texto_exemplo):
    print (i)

