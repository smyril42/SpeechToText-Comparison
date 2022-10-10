import speech_recognition as sr # speech to text library
import time # for measuring the time the program takes
from difflib import SequenceMatcher # for comparing the text with the original

start = time.time() # time counter

def main(): # main funktion
    with open("resources/original_text.txt", "r") as o:  # opens and reads the original text
        original_text = o.read()
    files: list = ["scan_off.wav", "scan_on.wav"]
    file: str = "resources/" + files[1]

    r = sr.Recognizer()

    with sr.AudioFile(file)as source: # opens audiofile
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="de-DE") # converts speech to text
        print(text)

    print(SequenceMatcher(None, text.lower(), original_text.lower()).ratio()) # compares the text

main()

print("{:.2f}".format(round(time.time()-start, 2))) # formats prints the time it took to run
