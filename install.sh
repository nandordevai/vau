#!/bin/sh

sudo apt-get install python3-pip
sudo apt-get install python-pyaudio
sudo apt-get install flac
pip3 install SpeechRecognition
pip3 freeze > requirements.txt
