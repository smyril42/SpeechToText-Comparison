import speech_recognition as sr
import time
from difflib import SequenceMatcher

start = time.time()

def main():
    with open("resources/original_text.txt", "r") as o:
        original_text = o.read()
    files: list = ["scan_off.wav", "scan_on.wav", "stefan_voice.aup3", "stefan_voice.wav"]
    file: str = "resources/" + files[1]

    r = sr.Recognizer()

    with sr.AudioFile(file)as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="de-DE")
        print(text)

    print(SequenceMatcher(None, text.lower(), original_text.lower()).ratio())

main()

end = time.time()
print("{:.2f}".format(round(end-start, 2)))
