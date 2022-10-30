from gtts import gTTS
import os
mytext = input("Enter the statement: ")
language = 'hi'
myobj = gTTS(text=mytext, lang=language, slow=0.25)
myobj.save("D:\\AiSaves\\welcome.mp3")
os.system("D:\\AiSaves\\welcome.mp3")
