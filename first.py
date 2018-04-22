
#enregistrement sur 3
#mode
#ariste and gendre tri
from gtts import gTTS
from playsound import playsound
import os
from random import shuffle
import requests




#------------------instruction---------------------
def check_instruction():
    prob=0
    if not(os.path.exists("/usr/lib/vocal_player")) :
	    os.system("sudo python setup.py")
    if not(os.path.exists("/usr/lib/vocal_player/instruction")) :
	    os.system("sudo python setup.py")
    if not(os.path.exists("/usr/lib/vocal_player/minute.mp3")):
        prob+=1       
    if not(os.path.exists("/usr/lib/vocal_player/time.mp3")):
        prob+=1       
    for i in range (1,61):
        s=str(i)
        if not(os.path.exists("/usr/lib/vocal_player/"+s+".mp3")):
            prob+=1           
    if not(os.path.exists("/usr/lib/vocal_player/midnight.mp3")):
        prob+=1       
    if not(os.path.exists("/usr/lib/vocal_player/clock.mp3")):
        prob+=1    
    if not(os.path.exists("/usr/lib/vocal_player/welcome_to_vocale.mp3")):
        prob+=1        
    if not(os.path.exists("/usr/lib/vocal_player/instruction/on.mp3")):
        prob+=1       
    if not(os.path.exists("/usr/lib/vocal_player/instruction/first.mp3")):
        prob+=1     
    if not(os.path.exists("/usr/lib/vocal_player/instruction/create.mp3")):
        prob+=1       
    if not(os.path.exists("/usr/lib/vocal_player/instruction/create_0.mp3")):
        prob+=1       
    if not(os.path.exists("/usr/lib/vocal_player/instruction/create_1.mp3")):
        prob+=1       
    if not(os.path.exists("/usr/lib/vocal_player/instruction/create_2.mp3")):
        prob+=1        
    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option.mp3")):
        prob+=1        
    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_0.mp3")):
        prob+=1
    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_1.mp3")):
        prob+=1        
    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_2.mp3")):
        prob+=1   
    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_3.mp3")):
        prob+=1    
    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_4.mp3")):
        prob+=1  
    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_6.mp3")):
        prob+=1  
    if not(os.path.exists("/usr/lib/vocal_player/instruction/play.mp3")):
        prob+=1
    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_0.mp3")):
        prob+=1
    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_2.mp3")):
        prob+=1
    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_3.mp3")):
        prob+=1
    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_1.mp3")):
        prob+=1
    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_6.mp3")):
        prob+=1
    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_9.mp3")):
        prob+=1
    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_8.mp3")):
        prob+=1   
    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_7.mp3")):   
        prob+=1
    if not(os.path.exists('/usr/lib/vocal_player/instruction/save_playlist_option.mp3')):
        prob+=1
    if not(os.path.exists('/usr/lib/vocal_player/instruction/save_playlist.mp3')):
        prob+=1
    if not(os.path.exists('/usr/lib/vocal_player/instruction/save_cancled.mp3')):
        prob+=1
    if not(os.path.exists('/usr/lib/vocal_player/instruction/save_succeeded.mp3')):
        prob+=1
    return(prob)



def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
        exit(-4)    
    return False

def save_liste(liste,path):
    fp=open(path,'w')
    fp.writelines(liste)
    fp.close

def save_playlist(play_liste):
    number=input("0:exit \n else exept 5")
    while (number==5):
            playsound('/usr/lib/vocal_player/instruction/save_playlist_mode.mp3')
            playsound('/usr/lib/vocal_player/instruction/save_playlist.mp3')
            number=input("0:exit \n else exept 5")
        
    if (number==0):
        playsound('/usr/lib/vocal_player/instruction/save_cancled.mp3')
    else :
        #if (os.path.exists('./saves/'+str(saved_number))):
         #   playsound('/usr/lib/vocal_player/instruction/slot_exist')
          #  d=input('other option or same to save')

        save_liste(play_liste,'./saves/'+str(number))
        playsound('/usr/lib/vocal_player/instruction/save_succeeded.mp3')
        playsound('/usr/lib/vocal_player/'+str(number)+'.mp3')


def load_list(path):
    if not(os.path.exists(path)) :
        print("path does not exist :/\n")
        return([])
    else:    
        fp=open(path,'r')
        l=fp.readlines()
        fp.close
        return(l)

def killall():
    f=open("/tmp/ps_pid",'r')
    l=f.readlines()
    f.close()
    f=open("/tmp/music_played",'w')
    f.write("")
    f.close()
    for i in l :
        os.system("kill -9 "+i)

def create_option_instruction():
    playsound('/usr/lib/vocal_player/instruction/creation_mode.mp3')
    playsound('/usr/lib/vocal_player/instruction/help.mp3')
    op=input()
    if(op in (0,1,2,3,4,6)):
        playsound('/usr/lib/vocal_player/instruction/creation_option_'+str(op)+'.mp3')
    else:
        playsound('/usr/lib/vocal_player/instruction/creation_option.mp3')
    
def create_liste(l) :
    final=[]
    for i in l:
        s=i[:-1]
        k=s.split("/")
        s=k[-1]
        s=s.replace(".mp3","")
        playsound("./music_mp3/name_"+s+".mp3")
        x=input("1:take \n2:leave\n3take_all\n0:cancel\n6:selection complet\n4:rehear the name\n5:instruction\n")
        while x not in (0,1,2,6,3) :
            if x==4 :
                playsound("./music_mp3/name_"+s+".mp3")
            if x==5 :
                create_option_instruction()
            x=input("1:take \n2:leave\n3take_all\n0:cancel\n6:selection complet\n4:rehear the name\n5:instruction\n")
        if x==0 :
            return([])
        if x==1 :
            final.append(i)
        if x==3 :
            dif=[var for var in l if var not in final]  
            shuffle(dif)
            final.extend(dif)
            break
        if x==6 :
            break
    return(final)


def adapt_chaine(chaine):
    liste_des_carac_special=[' ','"','/','<','>','|',':','&','-',"(",")",]
    for i in liste_des_carac_special:
        chaine=chaine.replace(i,'\\'+i)
    chaine=chaine.replace('\n','')
    return(chaine)


def play_music():
    os.system("python play.py & python con.py ")

# def choise_saved():
#     #(7androu)
#     saved_number=input()
#     while(saved_number==5 ):
#         #playsound('/usr/lib/vocal_player/instruction/save_choise.mp3')
#         #5 ba3ed 4 numbre de slot last time modified
#     if (saved_number==0) :
#         #playsound('/usr/lib/vocal_player/instruction/save_choise_cancled.mp3')
#     while(not(os.path.exists('./saves/'+str(saved_number))
#         if :
#             return(load_list('./'+str(number)))
#         else: #slotdont exit


def get_tag(name):
    title=""
    print("before "+name)
    name=adapt_chaine(name)
    print("after "+name)
    os.system("mp3info -p %t "+name+">/tmp/title")
    os.system("mp3info -p %a "+name+">/tmp/artist")
    if (os.path.getsize('/tmp/title')>0):
        fp=open('/tmp/title','r')
        title=fp.read()
        fp.close()
        if (os.path.getsize('/tmp/artist')>0):
            fp=open('/tmp/artist','r')
            artist=fp.read()
            fp.close()
            return(title+" by "+artist)
    return(title)
x=check_instruction()
if (not(x==0) ):
    print('there is '+str(x)+' configuration file/s not found')
    if (connected_to_internet()==True):
        os.system("sudo python setup.py")
    else:
        exit(-4)

playsound('/usr/lib/vocal_player/welcome_to_vocale.mp3')
    
#main
music_to_play=[]
music_played=[]
if not(os.path.exists("./music_mp3")) :
	os.mkdir("./music_mp3",'0755')
os.system("find ./music -type f -iname \"*.mp3\">/tmp/musicliste")
f=open("/tmp/musicliste","r")
music_founded=f.readlines()
f.close()
missing_file=0
for i in music_founded :
    s=i[:-1]
    string=get_tag(s)
    k=s.split("/")
    s=k[-1]
    print(s)
    s=s.replace(".mp3","")
    if (string==""):
        string=s.replace("_"," ")
    if not(os.path.exists("./music_mp3/name_"+s+".mp3")):
        if (connected_to_internet()==True):
            string=gTTS(text=string.replace(".mp3",""), lang='en')
            string.save("./music_mp3/name_"+s+".mp3")
        else:
            missing_file+=1

playsound('/usr/lib/vocal_player/instruction/on.mp3')
automatic_instruction=input('5 to automatic')
save_liste([str(automatic_instruction)+'\n'],'/tmp/auto_op')


playsound('/usr/lib/vocal_player/instruction/first.mp3')

if (automatic_instruction==5):
    playsound('/usr/lib/vocal_player/instruction/auto_on.mp3')
else:
    playsound('/usr/lib/vocal_player/instruction/auto_off.mp3')

if (automatic_instruction==5):
    playsound('/usr/lib/vocal_player/instruction/create.mp3')
op=5
while op not in (0,2,1):
    op=input("0:exit\n1:creation d'une liste\n2:choix parmi les liste predefinie\n 5:instructions")
    if (op==5):
        playsound('/usr/lib/vocal_player/instruction/help.mp3')
        op=input("0:exit\n1:creation d'une liste\n2:choix parmi les liste predefinie\n 5:instructions")
        if (op==5):
            playsound('/usr/lib/vocal_player/instruction/create.mp3')
        else:
            playsound('/usr/lib/vocal_player/instruction/create_'+str(op)+'.mp3')
        op=5

if op == 0:
    exit(-4)
if op == 1:
    playsound('/usr/lib/vocal_player/instruction/creation_mode.mp3')
    if (automatic_instruction==5):
        playsound('/usr/lib/vocal_player/instruction/creation_option.mp3')
    music_to_play=create_liste(music_founded)[::-1]
    playsound('/usr/lib/vocal_player/instruction/save_playlist_option.mp3')
    if (input('1:save')==1):
        playsound('/usr/lib/vocal_player/instruction/save_playlist_mode.mp3')
        if (automatic_instruction==5):
            playsound('/usr/lib/vocal_player/instruction/save_playlist.mp3')
        save_playlist(music_to_play)

#if op == 2:
    #choix_liste


save_liste(music_to_play,'/tmp/music_to_play')

if (automatic_instruction==5):
    playsound("/usr/lib/vocal_player/instruction/play.mp3")

while (os.path.getsize('/tmp/music_to_play') > 0):
    music_to_play=load_list('/tmp/music_to_play')
    play_music()

print('fin')
killall()
# for i in music_to_play :
#     print(i)
# print("-------")
# play_list(music_to_play,music_played)
# for i in music_to_play :
#     print(i)

# print("----")

# for i in music_played :
#     print(i)





        


    





