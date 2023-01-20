#!/usr/bin/env python3

from datetime import datetime
import os
import random
import time

import speech_recognition as sr


r = sr.Recognizer()
logfile = open('vau.log', mode='a', buffering=1)


def write_log(msg):
    d = datetime.isoformat(datetime.now())
    logfile.write('{} {}\n'.format(d, msg))
    print('{} {}\n'.format(d, msg))


def callback(recognizer, audio):
    os.system('omxplayer ./process.aif > /dev/null 2>&1')
    write_log('Recognizing audio...')
    try:
        text = recognizer.recognize_google_cloud(audio, language='hu-HU')
        write_log('👱 got back {}'.format(text))
        num = random.randint(1, 13)
        os.system('omxplayer ./clips/dog/{}.mp3 > /dev/null 2>&1'.format(num))
    except sr.UnknownValueError:
        write_log('🐶 Could not recognize')
        num = random.randint(1, 23)
        os.system('omxplayer ./clips/human/{}.mp3 > /dev/null 2>&1'.format(num))
    except sr.RequestError as e:
        write_log('Could not request results ({0})'.format(e))
    except Exception as e:
        write_log('Something bad happened: {}'.format(e))


write_log('Starting translator')

r.energy_threshold = 500
r.dynamic_energy_threshold = False
mic = sr.Microphone(device_index=1)
with mic as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(mic, callback, phrase_time_limit=3)
while True:
    time.sleep(0.1)
