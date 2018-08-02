
from gtts import gTTS
from playsound import playsound
import os
from random import shuffle
import requests




#------------------verification de l'existance des fichiers setup---------------------
def missingInstruction():

    prob=0

    if not(os.path.exists("./music_mp3")) :
        prob+=1
        print ("./music not found")


    if not(os.path.exists("./saves")) :
        prob+=1
        print ("./saves not found")


    if not(os.path.exists("/usr/lib/vocal_player")) :
        prob+=1
        print ("/usr/lib/vocal_player not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction")) :
        prob+=1
	print ("/usr/lib/vocal_player/instruction not found")
        

    if not(os.path.exists("/usr/lib/vocal_player/minute.mp3")):
        prob+=1
        print ("/usr/lib/vocal_player/minute.mp3")
    

    if not(os.path.exists("/usr/lib/vocal_player/time.mp3")):
        prob+=1     
        print ("/usr/lib/vocal_player/time.mp3")  
    

    for i in range (1,61):
        s=str(i)
        if not(os.path.exists("/usr/lib/vocal_player/"+s+".mp3")):
            prob+=1     
            print ("/usr/lib/vocal_player/"+s+".mp3 not found")      
    

    if not(os.path.exists("/usr/lib/vocal_player/midnight.mp3")):
        prob+=1
        print ("./saves not found")             
    

    if not(os.path.exists("/usr/lib/vocal_player/clock.mp3")):
        prob+=1    
        print ("/usr/lib/vocal_player/midnight.mp3")      
    

    if not(os.path.exists("/usr/lib/vocal_player/welcome_to_vocale.mp3")):
        prob+=1        
        print ("/usr/lib/vocal_player/welcome_to_vocale.mp3 not found")      
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/on.mp3")):
        prob+=1       
        print ("/usr/lib/vocal_player/instruction/on.mp3 not found")      
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/first.mp3")):
        prob+=1     
        print ("/usr/lib/vocal_player/instruction/first.mp3")      
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/create.mp3")):
        prob+=1     
        print ("/usr/lib/vocal_player/instruction/create.mp3 not found")  
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/create_0.mp3")):
        prob+=1       
        print ("/usr/lib/vocal_player/instruction/create_0.mp3")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/create_1.mp3")):
        prob+=1       
        print ("/usr/lib/vocal_player/instruction/create_1.mp3")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/create_2.mp3")):
        prob+=1        
        print ("/usr/lib/vocal_player/instruction/create_2.mp3")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option.mp3")):
        prob+=1        
        print ("/usr/lib/vocal_player/instruction/creation_option.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_0.mp3")):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/creation_option_0.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_1.mp3")):
        prob+=1        
        print ("/usr/lib/vocal_player/instruction/creation_option_1.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_2.mp3")):
        prob+=1   
        print ("/usr/lib/vocal_player/instruction/creation_option_2.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_3.mp3")):
        prob+=1    
        print ("/usr/lib/vocal_player/instruction/creation_option_3.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_4.mp3")):
        prob+=1  
        print ("/usr/lib/vocal_player/instruction/creation_option_4.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_6.mp3")):
        prob+=1  
        print ("/usr/lib/vocal_player/instruction/creation_option_6.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play.mp3")):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/play.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_0.mp3")):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/play._0mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_2.mp3")):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/play_2.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_3.mp3")):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/play_3.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_1.mp3")):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/play_1.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_6.mp3")):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/play_6.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_9.mp3")):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/play_9.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_8.mp3")):
        prob+=1   
        print ("/usr/lib/vocal_player/instruction/play_8.mp3 not found")
    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_7.mp3")):   
        prob+=1
        print ("/usr/lib/vocal_player/instruction/play_7.mp3 not found")
    

    if not(os.path.exists('/usr/lib/vocal_player/instruction/save_playlist_option.mp3')):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/save_playlist_option.mp3")
    

    if not(os.path.exists('/usr/lib/vocal_player/instruction/save_playlist.mp3')):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/save_playlist.mp3")
    

    if not(os.path.exists('/usr/lib/vocal_player/instruction/save_cancled.mp3')):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/save_cancled.mp3")
    

    if not(os.path.exists('/usr/lib/vocal_player/instruction/save_succeeded.mp3')):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/save_succeeded.mp3")
    

    if not(os.path.exists('/usr/lib/vocal_player/instruction/slot_exist.mp3')):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/slot_exist.mp3")
    

    if not(os.path.exists('/usr/lib/vocal_player/instruction/pick_saved.mp3')):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/pick_saved.mp3 not found")
    

    if not(os.path.exists('/usr/lib/vocal_player/instruction/pick_saved_cancled.mp3')):
        prob+=1
        print ("/usr/lib/vocal_player/instruction/pick_saved_cancled.mp3 not found")
    
    return(prob)


#----------------verification des dossiers du sauvgarde
def repertoireCheck():
    if not(os.path.exists("./music_mp3")) :
	    os.mkdir("./music_mp3",0755)
    if not(os.path.exists("./saves")) :
	    os.mkdir("./saves",0755)



#------------------fct pour tester la connexion internet---------------------
def checkInternet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
        exit(-4)    
    return False

#------------------fct pour sauvgarder une liste dans fichier---------------------
def saveListe(liste,path):
    fp=open(path,'w')
    fp.writelines(liste)
    fp.close


#------------------fct pour sauvgarder une liste dans un slots---------------------
#sauvegarde dans the least aded
def savePlaylist(play_liste):
    number=input("0:exit \n else exept 5")
    while True:
        d=1
        while (number==5):
                playsound('/usr/lib/vocal_player/instruction/save_playlist_mode.mp3')
                playsound('/usr/lib/vocal_player/instruction/save_playlist.mp3')
                number=input("0:exit \n else exept 5")
        
        if (number==0):
            playsound('/usr/lib/vocal_player/instruction/save_cancled.mp3')
            break
        else :
            if (os.path.exists('./saves/'+str(number))):
                playsound('/usr/lib/vocal_player/instruction/slot_exist.mp3')
                date_modification=os.popen("stat ./saves/"+str(number)+" |grep Modify |cut -d \  -f 2").read()
                heure_modification=os.popen("stat ./saves/"+str(number)+" |grep Modify |cut -d \  -f 3").read()
                print(date_modification)#months sound
                print(heure_modification)
                playsound('/usr/lib/vocal_player/instruction/save_playlist.mp3')
                d=input('press one to ecrase the old one')
            if d==1:
                saveListe(play_liste,'./saves/'+str(number))
                playsound('/usr/lib/vocal_player/instruction/save_succeeded.mp3')
                playsound('/usr/lib/vocal_player/'+str(number)+'.mp3')
                break
            number=input("0:exit \n else exept 5")

#------------------fct pour charger une liste---------------------
def loadList(path):
    if not(os.path.exists(path)) :
        print("path does not exist :/\n")
        return([])
    else:    
        fp=open(path,'r')
        l=fp.readlines()
        fp.close
        return(l)

#------------------fct pour fermer le programme---------------------
def killall():
    f=open("/tmp/ps_pid",'r')
    l=f.readlines()
    f.close()
    f=open("/tmp/music_played",'w')
    f.write("")
    f.close()
    for i in l :
        os.system("kill -9 "+i)

#------------------fct pour ecouter les instruction de la creation d'une liste ---------------------
def createOptionInstruction():
    playsound('/usr/lib/vocal_player/instruction/creation_mode.mp3')
    playsound('/usr/lib/vocal_player/instruction/help.mp3')
    op=input()
    if(op in (0,1,2,3,4,6)):
        playsound('/usr/lib/vocal_player/instruction/creation_option_'+str(op)+'.mp3')
    else:
        playsound('/usr/lib/vocal_player/instruction/creation_option.mp3')

#------------------fct pour creer une liste --------------------------------------------------------  
def createList(musicList) :
    final=[]
    print('dkhal')
    for trackPath in musicList:
        trackPath=trackPath.split("/")
        trackName=trackPath[-1]
        trackName=trackName.replace(".mp3","")
        print(trackName)
        playsound("./music_mp3/name_"+trackName+".mp3")
        x=input("1:take \n2:leave\n3take_all\n0:cancel\n6:selection complet\n4:rehear the name\n5:instruction\n")
        while x not in (0,1,2,6,3) :
            if x==4 :
                playsound("./music_mp3/name_"+trackName+".mp3")
            if x==5 :
                createOptionInstruction()
            x=input("1:take \n2:leave\n3take_all\n0:cancel\n6:selection complet\n4:rehear the name\n5:instruction\n")
        if x==0 :
            return([])
        if x==1 :
            final.append(trackName)
        if x==3 :
            dif=[var for var in musicList if var not in final]  
            shuffle(dif)
            final.extend(dif)
            break
        if x==6 :
            break
    print(final)
    return(final)

#------------------fct pour adapter une chaine de caractere a le shell  ---------------------
def adapt_chaine(chaine):
    liste_des_carac_special=[' ','"','/','<','>','|',':','&','-',"(",")","'"]
    for i in liste_des_carac_special:
        chaine=chaine.replace(i,'\\'+i)
    chaine=chaine.replace('\n','')
    return(chaine)

#------------------fct pour ecouter un fichier mp3  ---------------------
def playMusic():
    os.system("python play.py & python con.py ")

#------------------fct pour choisir un slot  ---------------------
def pickSaved():
    playsound('/usr/lib/vocal_player/instruction/pick_saved.mp3')
    out=os.popen("ls -t ./saves").read()
    slots=out.split("\n")
    slots=slots[:-1]
    print("slots: ",slots)
    saved_number=input()
    while ((str(saved_number)not in slots) or (saved_number==5) or (saved_number==0) ):
        if(saved_number==5):
            playsound('/usr/lib/vocal_player/instruction/pick_saved.mp3')
            for slot in slots:
                playsound("/usr/lib/vocal_player/"+slot+".mp3")
        if (saved_number==0) :
            playsound('/usr/lib/vocal_player/instruction/pick_saved_cancled.mp3')
            break
        if (str(saved_number)not in slots):
            #playsound('/usr/lib/vocal_player/instruction/slot_not_found.mp3')
            print("slot_not_found")
        saved_number=input()
    return(loadList('./saves/'+str(saved_number)))


#------------------fct pour extraire le tag name et le artisite d'apres un fichier mp3---------------------
def getTag(pistePath):
    title=""
    print("before "+pistePath)
    pistePath=adapt_chaine(pistePath)
    print("after "+pistePath)
    title=os.popen("mp3info -p %t "+pistePath).read()
    artist=os.popen("mp3info -p %a "+pistePath).read()
    if (title!=""):
        if (artist!=""):
            return(title+" by "+artist)
    return(title)

#------- obtention des paths du piste musicaux
def findMusicTrack():
    music_founded=os.popen("find ./music -type f -iname \"*.mp3\"").read()
    music_founded=music_founded.split('\n')
    music_founded=music_founded[:-1]
    return(music_founded)

#------- creation des fichiers mp3 contenants les noms des pistes trouver
def createTrackName(musicFounded):
    missingFile=0
    for pistePath in musicFounded :
        pisteTag=getTag(pistePath)
        pistePath=pistePath.split("/")
        pisteName=pistePath[-1]
        pisteName=pisteName.replace(".mp3","")
        if (pisteTag==""):
            pisteTag=pisteName.replace("_"," ")
        if not(os.path.exists("./music_mp3/name_"+pisteName+".mp3")):
            if (checkInternet()==True):
                string=gTTS(text=pisteTag.replace(".mp3",""), lang='en')
                string.save("./music_mp3/name_"+pisteName+".mp3")
            else:
                missingFile+=1
    print(str(missingFile)+" track is missing")

#----------------- get auto instruction option
def autoInstruction():
    playsound('/usr/lib/vocal_player/instruction/on.mp3')
    option=input('5 to automatic')
    saveListe([str(option)+'\n'],'/tmp/auto_op')
    return(option)

#---------------------------------------------------------------------
#--------------------main------------------------------------------------
#-----------------------------------------------------------------------

# --------------------verification des fichier system

while(missingInstruction()!=0):
    print('there is '+str(missingInstruction())+' configuration file/s not found')
    if (checkInternet()==True):
        os.system("sudo python setup.py")
    else:
        exit(-4)

#----------------message de reciption

playsound('/usr/lib/vocal_player/welcome_to_vocale.mp3')
    
#---------les piles des piste musicaux

musicToPlay=[]
music_played=[]


repertoireCheck()
musicFounded=findMusicTrack()
createTrackName(musicFounded)
automatic_instruction=autoInstruction()


playsound('/usr/lib/vocal_player/instruction/first.mp3')

if (automatic_instruction==5):
    playsound('/usr/lib/vocal_player/instruction/auto_on.mp3')
else:
    playsound('/usr/lib/vocal_player/instruction/auto_off.mp3')

if (automatic_instruction==5):
    playsound('/usr/lib/vocal_player/instruction/create.mp3')



op=5
while op not in (0,2,1):
    op=input("0:exit\n1:creation d'une liste\n2:choix parmi les liste predefinie\n5:instructions")
    if (op==5):
        playsound('/usr/lib/vocal_player/instruction/help.mp3')
        op=input("0:exit\n1:creation d'une liste\n2:choix parmi les liste predefinie\n5:instructions")
        if (op==5):
            playsound('/usr/lib/vocal_player/instruction/create.mp3')
        else:
            playsound('/usr/lib/vocal_player/instruction/create_'+str(op)+'.mp3')
        op=5


if op == 0:
    exit(-4)
if op == 1:
    playsound('/usr/lib/vocal_player/instruction/creation_mode.mp3')
    print('1\n')
    if (automatic_instruction==5):
        print('2\n')
        playsound('/usr/lib/vocal_player/instruction/creation_option.mp3')
    musicToPlay=createList(musicFounded)
    print(musicToPlay)
    musicToPlay=musicToPlay[::-1]
    print(musicToPlay)
    x='\n\t'.join(musicToPlay)
    musicToPlay=x.split('\t')
    print(x)
    playsound('/usr/lib/vocal_player/instruction/save_playlist_option.mp3')
    if (input('1:save')==1):
        playsound('/usr/lib/vocal_player/instruction/save_playlist_mode.mp3')
        if (automatic_instruction==5):
            playsound('/usr/lib/vocal_player/instruction/save_playlist.mp3')
        savePlaylist(musicToPlay)

if op == 2:
    musicToPlay=pickSaved()

print(musicToPlay)

saveListe(musicToPlay,'/tmp/music_to_play')

if (automatic_instruction==5):
    playsound("/usr/lib/vocal_player/instruction/play.mp3")

while (os.path.getsize('/tmp/music_to_play') > 0):
    musicToPlay=loadList('/tmp/music_to_play')
    playMusic()

print('fin')
killall()






        


    





