








Abel=0
David=0
Quintana=0
Arroyo=0
Equipo=0
Otros=0
Otroslist=[]
for i in lista_aut:
    if i=='Abel Rojas':
        Abel=Abel+1
    else:
        if i=='David León':
            David=David+1
        else:
            if i=='Miguel Quintana':
                Quintana=Quintana+1
            else:
                if i=='Alejandro Arroyo':
                    Arroyo=Arroyo+1
                else:
                    if i=='Equipo de Ecos':
                        Equipo=Equipo+1
                    else:
                        Otros=Otros+1
                        Otroslist.append(i)
print 'Abel:'+str(Abel)
print 'David: '+str(David)
print 'Quintana: '+str(Quintana)
print 'Arroyo: '+str(Arroyo)
print 'Equipo: '+str(Equipo)
print 'Otros: '+str(Otros)

Otroslist
