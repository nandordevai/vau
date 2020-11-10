from vosk import Model, KaldiRecognizer
import pyaudio

sample_rate = 44100
chunk = 8000
model = Model("model")
rec = KaldiRecognizer(model, sample_rate)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=2,
                rate=sample_rate, input=True, frames_per_buffer=chunk)
stream.start_stream()

while True:
    data = stream.read(chunk, exception_on_overflow=False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
    else:
        print(rec.PartialResult())

print(rec.FinalResult())
