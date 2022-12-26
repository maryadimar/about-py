#--------------------------------------------
# Dibuat oleh maryadi
# pada 26/12/2022
# script untuk convert teks
# ke sound
#--------------------------------------------

from gtts import gTTS
import os

tts = gTTS(text=input("Input Text :"), lang='id')
tts.save("sound.mp3")
#os.system("mpg321 good.mp3")
