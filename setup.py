from gtts import gTTS
import os
from datetime import datetime
import requests
print('setup mode')

def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def make_dir():
    if not(os.path.exists("/usr/lib/vocal_player")) :
	    os.mkdir("/usr/lib/vocal_player",0755)
    if not(os.path.exists("/usr/lib/vocal_player/instruction")) :
	    os.mkdir("/usr/lib/vocal_player/instruction",0755)

def time():
    if not(os.path.exists("/usr/lib/vocal_player/minute.mp3")):
        string=gTTS(text="minute", lang='en')
        string.save("/usr/lib/vocal_player/minute.mp3")
        
    ##if not(os.path.exists("/usr/lib/vocal_player/pm.mp3")):
    #    string=gTTS(text="pm", lang='en')
    #    string.save("/usr/lib/vocal_player/pm.mp3")
    if not(os.path.exists("/usr/lib/vocal_player/time.mp3")):
        string=gTTS(text="the time is", lang='en')
        string.save("/usr/lib/vocal_player/time.mp3")
        
    for i in range (1,61):
        s=str(i)
        if not(os.path.exists("/usr/lib/vocal_player/"+s+".mp3")):
            string=gTTS(text=s, lang='en', )
            string.save("/usr/lib/vocal_player/"+s+".mp3")
            
    if not(os.path.exists("/usr/lib/vocal_player/midnight.mp3")):
        string=gTTS(text="midnight", lang='en')
        string.save("/usr/lib/vocal_player/midnight.mp3")
        
    if not(os.path.exists("/usr/lib/vocal_player/clock.mp3")):
        string=gTTS(text="o'clock", lang='en')
        string.save("/usr/lib/vocal_player/clock.mp3")
        

def instruction():
    if not(os.path.exists("/usr/lib/vocal_player/welcome_to_vocale.mp3")):
        string=gTTS(text="welcome to CLL vocale music player.", lang='en')
        string.save("/usr/lib/vocal_player/welcome_to_vocale.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/on.mp3")):
        string=gTTS(text="to hear automaticaly the instructions press 5\n if this your first time please press 5", lang='en')
        string.save("/usr/lib/vocal_player/instruction/on.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/first.mp3")):
        string=gTTS(text="any time you need help press 5.", lang='en')
        string.save("/usr/lib/vocal_player/instruction/first.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/create.mp3")):
        string=gTTS(text="press 0 to exit the program \n press 1 to create new list \n or press 2 to choice between saved listes", lang='en')
        string.save("/usr/lib/vocal_player/instruction/create.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/create_0.mp3")):
        string=gTTS(text="exit the program", lang='en')
        string.save("/usr/lib/vocal_player/instruction/create_0.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/create_1.mp3")):
        string=gTTS(text="create new list", lang='en')
        string.save("/usr/lib/vocal_player/instruction/create_1.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/create_2.mp3")):
        string=gTTS(text="choice between saved listes", lang='en')
        string.save("/usr/lib/vocal_player/instruction/create_2.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option.mp3")):
        string=gTTS(text="press 0 to exit the program \npress 1 to add \npress 2 to skip \npress 3 to add all the rest\n press 4 to rehear the name \n 6 to end selection", lang='en')
        string.save("/usr/lib/vocal_player/instruction/creation_option.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_0.mp3")):
        string=gTTS(text="exit the program", lang='en')
        string.save("/usr/lib/vocal_player/instruction/creation_option_0.mp3")

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_1.mp3")):
        string=gTTS(text="add the track", lang='en')
        string.save("/usr/lib/vocal_player/instruction/creation_option_1.mp3")    

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_2.mp3")):
        string=gTTS(text="skip to next track", lang='en')
        string.save("/usr/lib/vocal_player/instruction/creation_option_2.mp3")

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_3.mp3")):
        string=gTTS(text="add all the rest to playlist", lang='en')
        string.save("/usr/lib/vocal_player/instruction/creation_option_3.mp3")

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_4.mp3")):
        string=gTTS(text="rehear the name", lang='en')
        string.save("/usr/lib/vocal_player/instruction/creation_option_4.mp3") 

    if not(os.path.exists("/usr/lib/vocal_player/instruction/creation_option_6.mp3")):
        string=gTTS(text="end selection", lang='en')
        string.save("/usr/lib/vocal_player/instruction/creation_option_6.mp3")
    
        


    if not(os.path.exists("/usr/lib/vocal_player/instruction/play.mp3")):
        string=gTTS(text="press 0 to exit \npress 2 to pause and resume  \npress 3 to skip to next \npress 1 to back to previous  \npress 6 to volume down \npress 9 to volume up \npress 7 to mute\unmute \npress 8 to hear time  \n", lang='en')
        string.save("/usr/lib/vocal_player/instruction/play.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_0.mp3")):
        string=gTTS(text=" exit the program \n", lang='en')
        string.save("/usr/lib/vocal_player/instruction/play_0.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_2.mp3")):
        string=gTTS(text="pause and resume ", lang='en')
        string.save("/usr/lib/vocal_player/instruction/play_2.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_3.mp3")):
        string=gTTS(text=" skip to next", lang='en')
        string.save("/usr/lib/vocal_player/instruction/play_3.mp3")
        


    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_1.mp3")):
        string=gTTS(text=" back to previous ", lang='en')
        string.save("/usr/lib/vocal_player/instruction/play_1.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_6.mp3")):
        string=gTTS(text="lower the volume ", lang='en')
        string.save("/usr/lib/vocal_player/instruction/play_6.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_9.mp3")):
        string=gTTS(text="volume up ", lang='en')
        string.save("/usr/lib/vocal_player/instruction/play_9.mp3")
        

    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_8.mp3")):
        string=gTTS(text=" hear time ", lang='en')
        string.save("/usr/lib/vocal_player/instruction/play_8.mp3")
        
        
    if not(os.path.exists("/usr/lib/vocal_player/instruction/play_7.mp3")):
        string=gTTS(text=" mute\unmute", lang='en')
        string.save("/usr/lib/vocal_player/instruction/play_7.mp3")


    if not(os.path.exists('/usr/lib/vocal_player/instruction/save_playlist_option.mp3')):
        string=gTTS(text=" if you want to save the liste press 1", lang='en')
        string.save("/usr/lib/vocal_player/instruction/save_playlist_option.mp3")

    if not(os.path.exists('/usr/lib/vocal_player/instruction/save_playlist.mp3')):
        string=gTTS(text=" you have 8 slots to save from 1 to 9 exept the 5 wich will help to rehear this message or use 0 to cancel", lang='en')
        string.save("/usr/lib/vocal_player/instruction/save_playlist.mp3")

    if not(os.path.exists('/usr/lib/vocal_player/instruction/save_cancled.mp3')):
        string=gTTS(text="your playlist will not be saved", lang='en')
        string.save("/usr/lib/vocal_player/instruction/save_cancled.mp3")

    if not(os.path.exists('/usr/lib/vocal_player/instruction/save_succeeded.mp3')):
        string=gTTS(text="playlist saved in slot number", lang='en')
        string.save("/usr/lib/vocal_player/instruction/save_succeeded.mp3")

    if not(os.path.exists('/usr/lib/vocal_player/instruction/auto_on.mp3')):
        string=gTTS(text="auto instruction hearing is on", lang='en')
        string.save("/usr/lib/vocal_player/instruction/auto_on.mp3")

    if not(os.path.exists('/usr/lib/vocal_player/instruction/auto_off.mp3')):
        string=gTTS(text="auto instruction hearing is off", lang='en')
        string.save("/usr/lib/vocal_player/instruction/auto_off.mp3")

    if not(os.path.exists('/usr/lib/vocal_player/instruction/save_playlist_mode.mp3')):
        string=gTTS(text="you are about to save the playlist", lang='en')
        string.save("/usr/lib/vocal_player/instruction/save_playlist_mode.mp3")    
    
    if not(os.path.exists('/usr/lib/vocal_player/instruction/creation_mode.mp3')):
        string=gTTS(text="you are about to create a playlist", lang='en')
        string.save("/usr/lib/vocal_player/instruction/creation_mode.mp3")    
    
    if not(os.path.exists('/usr/lib/vocal_player/instruction/help.mp3')):
        string=gTTS(text="repress 5 to hear all instruction or press one of the other buttons to hear it funcionality", lang='en')
        string.save("/usr/lib/vocal_player/instruction/help.mp3")    
    


if (connected_to_internet()==True):
    make_dir()
    time()
    instruction()
