## Run these commands in terminal  before executing this program
## $ rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
## and also run this in seperate terminal
## $ rasa run actions

import os
import requests
import speech_recognition as sr     # import the library
import subprocess
from gtts import gTTS
from pygame import mixer

# Starting the mixer
mixer.init()

def play_saved_song():    
    '''Play the ``song1.mp3`` file in audio directory.'''
    # Loading the song
    mixer.music.load("audio/song1.mp3")
    
    # Start playing the song
    mixer.music.play()

    # Unloads the the song
    while mixer.music.get_busy():
        continue
    
    mixer.music.load("audio/song2.mp3")
    os.remove("audio/song1.mp3")


bot_message = "Hello World"
message=""

r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})

print("Bot : ",end=' ')
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

myobj = gTTS(text=bot_message, lang='ur', slow=False)
myobj.save("audio/song1.mp3")
print('\nFile Saved')
play_saved_song()


while bot_message != "Bye" or bot_message!='thanks':

    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # source it will be either Microphone or audio files.
        r.adjust_for_ambient_noise(source,duration=1)
        
        print("\t\t\t\t<<<\tListening\t>>>")
        
        audio = r.listen(source)  # listen to the source
        try:
            message = r.recognize_google(audio, language="en")  # use recognizer to convert our audio into text part.
            print("You : \t{}".format(message))

        except:
            print("Sorry could not recognize your voice")  # In case of voice not recognized  clearly
    if len(message)==0:
        continue
    # print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot : ",end=' ')

    bot_message = ''
    for i in r.json():
        bot_message += i['text']
        print(f"\t{bot_message}")

    if len(bot_message)==0:
        continue
    myobj = gTTS(text=bot_message, lang='ur', slow=False)
    myobj.save("audio/song1.mp3")
    print('\nFile Saved')
    # Playing the converted file
    play_saved_song()
