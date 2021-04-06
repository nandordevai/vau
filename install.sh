#!/bin/sh

sudo apt install python3-pip python-pyaudio flac omxplayer
pip3 install SpeechRecognition
pip3 freeze > requirements.txt
