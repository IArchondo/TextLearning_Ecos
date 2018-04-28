import time

months=['01','02','03','04','05','06','07','08','09','10','11','12']
pages=[1,2,3,4,5,6,7]
years=['2014','2015','2016','2017']

indexcomp=[]
for y in years:    
    for m in months:
        for p in pages:
             indexcomp.append('http://www.ecosdelbalon.com/'+str(y)
             +'/'+str(m)+'/page/'+str(p)+'/')

indexcomp
index

indexcom[2]

prob=requests.get(indexcomp[166])
prob.status_code==200

def get_urls_aut_date(index):
    urlbig=[]
    autbig=[]
    datebig=[]
    for url in index:
        time.sleep(1)
        print '-------------------------'
        print url
        web=requests.get(url)
        if web.status_code==200:
            soupweb=BeautifulSoup(web.content,'html.parser')
            urlsweb=soupweb.find_all(class_='post_title')
            authweb=soupweb.find_all(class_='post_info_author')
            dateweb=soupweb.find_all(class_='post_info_date')
            
            for link in urlsweb:
                strlink=str(link)
                urlbien=strlink.split('href="')[1].split('"')[0]
                urlbig.append(urlbien)
            for aut in authweb:
                straut=str(aut)
                autbien=straut.split("Entradas de ")[1].split('"')[0]
                autbig.append(autbien)
            for date in dateweb:
                strdate=str(date)
                datebien=strdate.split('">')[1].split('</')[0]
                datebig.append(datebien)
            print 'Todo bien.'
        
        else:
            print 'Page not found. Not appended.'
    
    print 'Finished'
    return urlbig,autbig,datebig
    

urllistap=get_urls(indexcomp)

lista_url,lista_aut,lista_dat=get_urls_aut_date(indexcomp)

lista_dat[0:20]

ecos_df=pd.DataFrame({'Date':lista_dat,'Autor':lista_aut,'URL':lista_url})
os.chdir('/Users/IArchondo/Desktop/Python/Proyectos personales/Text Learning Ecos')
ecos_df.to_csv('ecos_df.csv',index=False)


tagsfarinos=soupfarinos.find_all(class_='post_info_tags')

tagsfarinos.find_all(tag)

del [prueba,problist,urllista,urllistap,string_list,conseguidor,conseguidorind]

fardate=[]
for i in datefarinos:
    bien=str(i).split('">')[1].split('</')[0]
    fardate.append(bien)

fardate

