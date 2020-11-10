#!/usr/bin/env python3

import speech_recognition as sr
import sys

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    # recognize_google(audio_data: AudioData, key: Union[str, None] = None, language: str = "en-US", , pfilter: Union[0, 1], show_all: bool = False) -> Union[str, Dict[str, Any]]
    print("You said ", r.recognize_google(audio, language='hu-HU'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(
        "Could not request results from Google Speech Recognition service; {0}".format(e))
