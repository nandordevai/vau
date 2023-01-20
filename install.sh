#!/bin/sh

sudo apt update
sudo apt install python3-pip python-pyaudio flac omxplayer
pip3 install SpeechRecognition
pip3 install PyAudio
pip3 install google-api-python-client
pip3 install oauth2client
pip3 freeze > requirements.txt
