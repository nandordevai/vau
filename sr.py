#!/usr/bin/env python3

from threading import Thread
from queue import Queue
from datetime import datetime
import os
import random

import speech_recognition as sr


r = sr.Recognizer()
audio_queue = Queue()
logfile = open('vau.log', 'a')


def write_log(msg):
    d = datetime.isoformat(datetime.now())
    logfile.write('{} {}\n'.format(d, msg))


def recognize_worker():
    write_log('Starting translator')
    while True:
        audio = audio_queue.get()
        if audio is None:
            break
        write_log('Recognizing audio...')
        try:
            text = r.recognize_google(audio, language='hu-HU')
            write_log('got back {}'.format(text))
            num = random.randint(1, 13)
            os.system('omxplayer ./clips/dog/{}.mp3'.format(num))
        except sr.UnknownValueError:
            write_log('Could not recognize')
            num = random.randint(1, 23)
            os.system('omxplayer ./clips/human/{}.mp3'.format(num))
        except sr.RequestError as e:
            write_log('Could not request results ({0})'.format(e))
            audio_queue.task_done()


r.energy_threshold = 100
recognize_thread = Thread(target=recognize_worker)
recognize_thread.daemon = True
recognize_thread.start()
with sr.Microphone(device_index=1) as source:
    try:
        while True:
            audio_queue.put(r.listen(source))
    except KeyboardInterrupt:
        pass

audio_queue.join()
audio_queue.put(None)
recognize_thread.join()
