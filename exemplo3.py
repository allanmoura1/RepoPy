import urllib2
import urllib
from bs4 import BeautifulSoup

user_agent = "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome /7.0.517.41 Safari/534.7"
opener = urllib2.build_opener() 
opener.addheaders = [('User-agent', user_agent)] 
html = opener.open("http://www.google.com.br").read()

soup = BeautifulSoup(html)
divs = [div for link in soup.findAll('div') if div.get("class") == "grupo "]
for div in divs:
  print div.get()""id
  
link = [link for link in soup.findAll('a') if link.get("href").endswith(".mp3")]
for link in link:
    nome_arquivo = link[link.rfind("/"):]
    urllib.urlretrieve(nome_arquivo,"/tmp/"+nome_arquivo)