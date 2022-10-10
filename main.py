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


a  =  """es ist ein Problem mit dem jeder PC und Mac Nutzer im Büro irgendwann konfrontiert wird ein wichtiger Brief soll als PDF gescannt werden oder ein abfotografiertes Dokument archiviert werden das Problem dabei der Scan oder das Foto allein sorgt zwar für eine digitale Kopie des Dokuments dass ich von Menschen den es doch sobald der Computer das Dokument in irgendeiner Form nutzen soll wird es knifflig soll der Text extrahiert oder der Inhalt der Datei indexiert werden stellt sich der Rechner an als wäre kein Text enthalten vor allem in Hinblick auf das papierlose Büro ist das ausgesprochen lästig weshalb es seit geraumer Zeit sogenannte Texterkennungssoftware gibt"""
b = """es ist ein Problem mit dem Reeder PC und Mac Benutzer im Büro hört man konfrontiert wird ein wichtiger Brief soll als PDF getrennt werden oder ein abfotografierte Dokumente archiviert werden das Problem dabei der Scan oder das Foto allein sorgt für eine digitale Kopie des Dokuments dass sich von Menschen die lässt doch sobald der Computer das Dokument in irgendeiner Form sonst sollte hinschicken soll der Text extrahieren oder der Inhalt der Datei indexiert werden stellt nicht mehr Rechte an als wäre kein Text enthalten vor allem im Hinblick auf das papierlose Büro ist das ausgesprochen lästig weshalb es seit geraumer Zeit sogenannte Texterkennungssoftware gibt"""
