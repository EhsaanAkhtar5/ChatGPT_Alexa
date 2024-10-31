from datetime import date
from email import message
from http import client
from urllib import response
import pyaudio
import wave
import keyboard
import time
import speech_recognition as sr
import pyttsx3 as p
import os
import whisper
import openai
import ffmpeg
from openai import OpenAI
from playsound import playsound
from gtts import gTTS
import tempfile


FORMAT = pyaudio.paInt16
CHANNELS = 1
CHUNK = 1024
RATE = 44100
OUTPUT_FILENAME = "test.wav"
client = OpenAI(api_key = 'sk-proj-3iookcy6Z7D7yfkW4hjbT3BlbkFJLveOeKX8EqRfgt8nHnzN')


def whisper_record():
    model = whisper.load_model('base')
    model.transcribe('C:\\Users\\ehsaa\\source\\reposz\ChatGPT Alexa\\ChatGPT Alexa\test.wav',fp16=False)


def record():
    while True:
        try:
            data = stream.read(CHUNK)
            frames.append(data)
        except KeyboardInterrupt:
            break
        if keyboard.is_pressed('space'):
            print('stopping recording')
            time.sleep(0.2)
            break
    stream.stop_stream()
    stream.close()
    audio.terminate()
    time.sleep(1)


def write_audio_file():
    waveFile = wave.open(OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close


def record_text():
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                if 'hey chat' in MyText:
                    Check_Prompt(MyText)
                    break
                return MyText
        except sr.RequestError as e:
            print('could not request results: {0}'.format(e))
        except sr.UnknownValueError:
            print('Unknown error occured')


def Check_Prompt(text):
    print('listening')
    playsound('Blop_Sound_Effect.wav')
    time.sleep(1)
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            response = client.chat.completions.create(model='gpt-3.5-turbo',messages=[{'role':'user','content':MyText}])
            response = response.choices[0].message.content.strip()
            print(response)
            text_to_speach(response)
    except sr.RequestError as e:
        print('could not request results: {0}'.format(e))
    except sr.UnknownValueError:
        print('Unknown error occured')



def chat_gpt_talk(prompt):
    response = client.chat.completions.create(model='gpt-3.5-turbo',messages=[{'role':'user','content':prompt}])
    return response.choices[0].message.content.strip()

def Voice_to_text():
    while True:
        text = record_text()


def read_file():
    f = open('output.txt','r')
    return f.read


def text_to_speach(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    playsound('temp.mp3')
    os.remove('temp.mp3')


if __name__ == "__main__":
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
    r = sr.Recognizer()
    #whisper_record()

    frames = []
    print("start space")
    keyboard.wait('space')
    print("reording press space to stop")
    time.sleep(0.2)
    Voice_to_text()
    #hello = input('Ask chatgpt: ')
    #response = chat_gpt_talk(hello)
    #print(response)


    #record()
    #write_audio_file()


