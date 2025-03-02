from vosk import Model, KaldiRecognizer
import pyaudio
import sys
import json
import pyttsx3
import ctypes
import webbrowser
import subprocess
import datetime 
import time
import keyboard
import screen_brightness_control as sbc

# _______________________________________________________________________________chat________________________________________________________________________________________
question= ["how are you","where are you","when is your birthday"]
answer = ["am okay, you too ?","i'm here with tou","my bearthday when 16 from april in 2024"]
#____________________________________________________________________________________________________________________________________________________________________________
#______________________________________________________________________________Webpages______________________________________________________________________________________
youtube = "https://www.youtube.com"
google = "https://www.google.com"
facebook = "https://www.facebook.com/mohammad.nour.71653318"
#____________________________________________________________________________________________________________________________________________________________________________
#_______________________________________________________________________________vedios_______________________________________________________________________________________
media_player = r"\digital_assistant\Windows Media Player\wmlaunch.exe" 
titanic = r"\digital_assistant\videos\Alan Walker - Titanic sin copyright_HD.mp"
#____________________________________________________________________________________________________________________________________________________________________________



def call_v(x):
    subprocess.call([media_player,x])
    time.sleep(4)
    keyboard.press('f11')

def keabord_presser(x):
    keyboard.press_and_release(x)

def brightness_down():
    a = sbc.get_brightness()
    for i in range(0,a[0]+1):
        sbc.set_brightness(a[0]-i)
        time.sleep(0.15)

def brightness_up():
    a = sbc.get_brightness()
    for i in range(a[0]+1,100):
        sbc.set_brightness(i)
        time.sleep(0.15)
# Translate the numbers to month
def the_date():
    date_now = datetime.datetime.now()
    monht = date_now.month
                                
    if monht == 1 : 
        monht = "january"
    elif monht == 2 :
        monht = "february"
    elif monht == 3 :
        monht = "march"
    elif monht == 4 :
        monht = "april"
    elif monht == 5 :
        monht = "may"
    elif monht == 6 :
        monht = "june"
    elif monht == 7 :
        monht = "july"
    elif monht == 8 :
        monht = "august"
    elif monht == 9 :
        monht = "september"
    elif monht == 10 :
        monht = "october"
    elif monht == 11 :
        monht = "november"
    else:
        monht = "december"

    year = date_now.year
    day = date_now.day
    speach(f"we are in {day} frome {monht} in {year} year")

def leave_brawse() :
    keyboard.press_and_release('ctrl+w')

def start_record():
    subprocess.Popen([r"C:\Program Files (x86)\EaseUS\RecExperts\bin\RecExperts.exe","argument1","argument2"])
    time.sleep(5)
    keyboard.press_and_release('esc')
    time.sleep(0.2)
    keyboard.press_and_release('f9')
    time.sleep(4)

def search_clear():
    keyboard.press_and_release('ctrl+a')
    keyboard.press('backspace')

def google_prepration():
    time.sleep(1)
    keyboard.press_and_release('ctrl+l')

def The_time_now():

    time_now = datetime.datetime.now()
    hours = time_now.hour
    minuts = time_now.minute
                                
    speach(f"it's {hours} and {minuts} minuts")
   
def speach(words):
    vois1 = pyttsx3.init()
    voices =vois1.getProperty('voices')
    vois1.setProperty('voice',voices[1].id)
    rate = vois1.getProperty('rate')
    vois1.setProperty('rate', rate-40)
    vois1.say(words)
    vois1.runAndWait()

def windows_sleep():
    ctypes.windll.powrprof.SetSuspendState(0,1,0)

def founded(string_,txt) :
    value = []
    for word in string_.split():
        if word in txt.split() :
            value.append(1)
        else :
            value.append(0)
    if 0 in value :
        return False
    else :
        return True

def initialize_recognizer(model_path):
    """Initialize the speech recognizer with the given model."""
    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)
    return recognizer

def start_audio_stream():
    """Start the audio stream from the microphone."""
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()
    return stream


#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def main():
    try:
        
        recognizer = initialize_recognizer(r"vosk-model-small-en-us-0.15")
        stream = start_audio_stream()

        while True:
            
            data = stream.read(4096, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text","")
                print(text)

                if founded("light",text) or founded("right",text):
                    speach("tell me what you need ?")
                    
                    while True:
            
                        data = stream.read(4096, exception_on_overflow=False)
                        if recognizer.AcceptWaveform(data):
                            result = json.loads(recognizer.Result())
                            text = result.get("text","")
                            print(text)

                            if founded("stop",text)   :
                                speach("i will stop now")
                                break

                            if founded("facebook",text):
                                webbrowser.open_new_tab(facebook)

                            elif founded("you tube",text) :
                                webbrowser.open_new_tab(youtube)
                                text = ""

                            elif founded("google",text):
                                webbrowser.open_new_tab(google)
                                google_prepration()
                                while True:
                                    
                                    data = stream.read(4096, exception_on_overflow=False)
                                    if recognizer.AcceptWaveform(data):
                                        result = json.loads(recognizer.Result())
                                        text = result.get("text","")

                                        if founded("go",text):
                                            keyboard.press_and_release('enter')
                                        elif founded("clear",text):
                                            search_clear()
                                        elif founded("break",text):
                                            break
                                        elif founded("leave",text) :
                                            leave_brawse()
                                            break
                                        else :
                                            keyboard.write(text)
                                
                            elif founded("sleep",text):
                                windows_sleep()
                            elif founded("search",text):
                                subprocess.run(["explorer.exe","shell:::{2559a1f3-21d7-11d4-bdaf-00c04f60b9f0}"])
                                text = ""
                                while True:
                                    data = stream.read(4096, exception_on_overflow=False)
                                    if recognizer.AcceptWaveform(data):
                                        result = json.loads(recognizer.Result())
                                        text = result.get("text","")
                                        if text.lower() == "clear":
                                            search_clear()
                                        elif founded("okay",text):
                                            keyboard.press_and_release('enter')
                                            break
                                        elif text.lower() == "break":
                                            break
                                        else :
                                            keyboard.write(text)
                                        text = ""
                                    print(text)
                            elif founded("what time is it",text):
                                The_time_now() 
                                text = ""
                            elif founded("start recording",text):
                                start_record()
                                while True:
                                    data = stream.read(4096, exception_on_overflow=False)
                                    if recognizer.AcceptWaveform(data):
                                        result = json.loads(recognizer.Result())
                                        text = result.get("text","")
                                        if founded("stop",text) or founded("start",text):
                                            keyboard.press_and_release('f10')
                                            text = ""
                                        
                                        elif founded("stop recording",text):
                                            keyboard.press_and_release('f9')
                                            text = ""
                                            break

                                            
                                    else:
                                        print(text)
                                    text = ""
                                text = ""
                            
                            elif founded("give me the date",text) :
                                the_date()
                                text = ""

                            elif founded("brightness up",text) or founded("whiteness up",text) or founded("greatness up",text):
                                a = sbc.get_brightness()

                                    
                                for i in range(a[0]+1,101):
                                    sbc.set_brightness(i)
                                    time.sleep(0.15)
                                    data = stream.read(4096, exception_on_overflow=False)
                                    if recognizer.AcceptWaveform(data):
                                        result = json.loads(recognizer.Result())
                                        text = result.get("text","")
                                        print(text)
                                        if founded("stop",text):
                                            sbc.set_brightness(i-6)
                                            break
                                    text = ""
                            elif text.lower() == "coby" or text.lower() == "gavi" or text.lower() == "gabi" or text.lower() == "copy" or text.lower() == "hobby":
                                keabord_presser('ctrl+c')
                            elif text.lower() == "paste" or text.lower() == "best" or text.lower() == "based" :
                                keabord_presser('ctrl+v')
                            elif text.lower() == "retreat" or text.lower() == "read read":
                                keabord_presser('ctrl+z')
                            elif text.lower() == "cut" or text.lower() == "got":
                                keabord_presser('ctrl+x')
                            elif text.lower() == "save" :
                                keabord_presser('ctrl+s') 
                            elif text.lower() == "zoom in":
                                keabord_presser('ctrl+shift+=')
                            elif text.lower() == "zoom out":
                                keabord_presser('ctrl+-')
                            elif text.lower() == "open" or text.lower() == "enter" :
                                keabord_presser('enter')
                            elif text.lower() == "screenshot" or text.lower() == "screen" or text.lower() == "shot" :
                                keabord_presser('left windows + shift + r')
                            elif founded("brightness down",text) or text.lower() == "this down" or text.lower() == "fact this down" or text.lower() == "bratton is though" or text.lower() == "write this down" :
                                a = sbc.get_brightness()
                                for i in range(0,a[0]):
                                    a = sbc.get_brightness()
                                    sbc.set_brightness(a[0]-1)
                                    time.sleep(0.15)
                                    data = stream.read(4096, exception_on_overflow=False)
                                    if recognizer.AcceptWaveform(data):
                                        result = json.loads(recognizer.Result())
                                        text = result.get("text","")
                                        print(text)
                                        if text.lower() == "stop":
                                            sbc.set_brightness(a[0]+6)
                                            break
                                    text = ""
                            elif text.lower() == "play titanic":
                                call_v(titanic)
                            
                            elif text.lower() == "play i love you":
                                call_v(i_love_you)
                                
                            elif text.lower() == "play guess where i am":
                                call_v(guess_where_i_am)
                            elif text.lower() == "play the eternal":
                                call_v(the_eternal)
                            elif text.lower() == "play my name":
                                call_v(my_name)



                            elif True:

                                for i in range(0,3) :
                                    if text.lower() == question[i] :
                                        speach(answer[i])
                                        text = ""
                elif text.lower() == "stop" or text.lower() == "stop light" :
                    speach("see you")
                    break





    except KeyboardInterrupt:
        print("Exiting...")
        stream.stop_stream()
        stream.close()
        sys.exit(0)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()