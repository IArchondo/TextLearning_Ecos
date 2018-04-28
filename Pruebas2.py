import requests

page=requests.get("https://raw.githubusercontent.com/dataquestio/web-scraping-pages/master/simple.html")

pagina=page.content

from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

listael=list(soup.children)
 [type(item) for item in list(soup.children)]
 
 list(html.children)
[type(item) for item in list(html.children)]

body=list(html.children)[3]

p=list(body.children)[1]

p.get_text()

 
list(diez.children)[0]

soup=BeautifulSoup(page.content,'html.parser')
soup.find_all('p')


###verdaderos descubrimientos aqui abajo
page=requests.get("http://www.ecosdelbalon.com/2016/12/adam-lallana-liverpool-juego-interiores-boro-karanka/")
soup2=BeautifulSoup(page.content,'html.parser')
texto=soup2.find_all('p', style="text-align: justify")
autor=soup2.find_all(class_="post_info_author")[0].get_text()

textoparrafo=[]
for parrafo in texto:
    textoparrafo.append(parrafo.get_text())

vectorizer=CountVectorizer(stop_words=spanish_stopwords)
bag_of_words=vectorizer.fit(textoparrafo)
bag_of_words=vectorizer.transform(textoparrafo)
print bag_of_words
vectorizer.vocabulary_.get(117)

from nltk.corpus import stopwords

spanish_stopwords=stopwords.words('spanish')


####prueba para conseguir los urls

principal=requests.get("http://www.ecosdelbalon.com/2017/04/page/7/")
soupprin=BeautifulSoup(principal.content,'html.parser')
soupprin.find_all(class_='post_title')
urls=soupprin.find_all(class_='post_title')
urls[1]
urls[2]
urls.dtypes()
type(urls)

cuerda=str(urls[0])

urlsbien=[]
for link in urls:
    strlink=str(link)
    bien=strlink.split('href="')[1].split('"')[0]
    urlsbien.append(bien)

urlsbien
