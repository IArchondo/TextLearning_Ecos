def get_text(indexurls):
    lista_text=[]
    catlist=[]
    for url in indexurls:
        textocomp=[]
        time.sleep(1)
        print "--------------------"
        print url
        page=requests.get(url)
        pagesoup=BeautifulSoup(page.content,'html.parser')
        
        categoria=pagesoup.find_all(class_='post_info_categories')
        if len(categoria)!=0:
            strcat=str(categoria).split('tag">')[1].split('</a')[0]
            catlist.append(strcat)
            print '--'+strcat+'--'
        
            if strcat == "Partidos" or strcat=="Equipos" or strcat=="Corporativo" or strcat=="Entrenadores" or strcat=="Futbolistas" or strcat=="Héroes":
                texto=pagesoup.find_all('p', style="text-align: justify")
                if len(texto)==0:
                    texto=pagesoup.find_all('p', style="text-align: justify;")
            else:
                if strcat=="Columnas":
                    texto=pagesoup.find_all(class_='three_fourth')
                
                else:
                    texto=[]
        else:
            texto=[]
            catlist.append('Otros')
            
        for parrafo in texto:
                par=parrafo.get_text()
                print par[0:10]
                textocomp.append(par)
                
        textocomp=' '.join(textocomp)
        lista_text.append(textocomp)
        print '-->Procesado.'
    
    print '*COMPLETADO*'  
    return lista_text,catlist
            


pruebalist=lista_url[0:10]        

resulprueb,catprueb=get_text(pruebalist)

lista_text,lista_cat=get_text(lista_url)

len(lista_text)

lista_text[2052]

len(lista_cat)
resulprueb[1]
catprueb
resulprueb
del texto

urlcolumna='http://www.ecosdelbalon.com/2014/01/fichaje-amrabat-malaga-necesidad-cubierta/'
urlpartidos='http://www.ecosdelbalon.com/2014/05/analisis-tactico-chelsea-1-atletico-de-madrid-3-final-champions-league/'
urlcorporativo='http://www.ecosdelbalon.com/2014/01/los-comentarios-del-27-el-28-de-enero/'
urlprueba='http://www.ecosdelbalon.com/2014/01/historia-estilo-juego-futbol-athletic-club-bilbao-pentland-clemente-bielsa-valverde/'

page=requests.get(urlcolumna)
pagesoup=BeautifulSoup(page.content,'html.parser')
texto=pagesoup.find_all(class_='post_info_categories')
texto
strcat=str(texto).split('tag">')[1].split('</a')[0]
print strcat

if strcat==("Partidos" or "Equipos" or "Corporativo" or "Futbolistas" or "Entrenadores"):
    print 'ahuevo putos'

strcat==("Pene" or "Futbolistas")

strcat=="Entrenadores" or strcat=="Futbolistas"
texto
len(texto)!=0

texto=pagesoup.find_all(class_='three_fourth')
texto

##Guardamos todo en un dataframe y lo reducimos a los que tienen observaciones o nos interesan

lista_text_unicode=[]
for i in lista_text:
    pene=i.encode('utf-8')
    lista_text_unicode.append(pene)

ecos_dfbig=pd.DataFrame({'Date':lista_dat,'Category':lista_cat,'Autor':lista_aut,'URL':lista_url,'Text':lista_text_unicode})
ecos_dfbig.to_csv('ecos_dfbig.csv',index=False)

ecos_df_red=ecos_dfbig.query('Category =="Futbolistas" or Category =="Equipos" or Category =="Partidos" or Category =="Entrenadores"')

ecos_df_red.to_csv('ecos_df_red.csv',index=False)

ecos_df_red.shape

####que comience el text learning
lista_aut_red=ecos_df_red['Autor'].tolist()
lista_text_red=ecos_df_red['Text'].tolist()

#con los features y labels podemos pasar a hacer el text learning
from sklearn.feature_extraction.text import CountVectorizer
count_vect=CountVectorizer(stop_words=spanish_stopwords)
bag_of_words=count_vect.fit_transform(lista_text_red)
print 'Done'
bag_of_words.vocabulary_
count_vect.vocabulary_.get("Messi")

from sklearn.naive_bayes import MultinomialNB
clf=MultinomialNB()
clf.fit(bag_of_words,lista_aut_red)
clf.score()

test=requests.get('http://www.ecosdelbalon.com/2017/04/analisis-victoria-del-barcelona-en-cornella-presion-espanyolista-ausencia-de-errores-cules/')
pagetest=BeautifulSoup(test.content,'html.parser')
textotest=pagetest.find_all('p', style="text-align: justify")

textotests=[]
textotestp=[]
for parrafo in textotest:
    par=parrafo.get_text()
    print par[0:10]
    textotests.append(par)
textotests=' '.join(textotests)
textotestp.append(textotests)

textotestp
bag_of_words_test=count_vect.transform(textotestp)

predicted=clf.predict(bag_of_words_test)
print predicted

print bag_of_words_test

for doc, category in zip(textotestp, predicted):
    print('%r => %s' % (doc, twenty_train.target_names[category]))
