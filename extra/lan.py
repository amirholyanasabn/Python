from gtts import gTTS
from playsound import playsound

audio = 'speech.mp3'
language = "de"
text = input("Please enter your text : ")
sp = gTTS(text=text, lang=language, slow=False)
sp.save(audio)
playsound(audio)
