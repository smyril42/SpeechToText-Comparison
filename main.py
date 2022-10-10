import speech_recognition as sr # speech to text library
import time # for measuring the time the program takes
from difflib import SequenceMatcher # for comparing the text with the original
from os import walk

start = time.time() # time counter

def main(): # main funktion
    with open("resources/original_text.txt", "r") as o:  # opens and reads the original text
        original_text = o.read()
    files = next(walk("resources"), (None, None, []))[2]
    file: str = "resources/" + input(f"files in /resources:\n{str(files).strip('[]')}\nAudiofile: resources/")

    r = sr.Recognizer()

    with sr.AudioFile(file)as source: # opens audiofile
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language="de-DE") # converts speech to text
        print(text)

    return SequenceMatcher(None, text.lower(), original_text.lower()).ratio() # compares and returns the text

print(main())

print("Das Programm hat {:.2f} Sekunden gebraucht.".format(round(time.time()-start, 2))) # formats prints the time it took to run
