#!/usr/bin/env python3

import speech_recognition as sr
import pyaudio
from os import path
import pyttsx
import sounddevice as sd
import soundfile as sf

def tts(data):
    engine = pyttsx.init()
    engine.say(data)
    engine.runAndWait()

def play():
    (data,fs)=sf.read('hii.wav')
    sd.play(data,fs)
    sd.wait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    print("ok\n")

    # recognize speech using Google Speech Recognition
    try:
        data = r.recognize_google(audio)
	strdata= data.encode('utf-8')
        print("Google Speech Recognition thinks you said \n " + strdata)
	return strdata
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
	return 'Error'
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
	return 'Error'

    print("\nok\n")

if __name__=='__main__':
    tts('Hello')
    #tts('Good Morning')
    #play()
    x=listen()
