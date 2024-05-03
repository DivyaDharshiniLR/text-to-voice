from gtts import gTTS
import os

text = "HELLO ITS DIVYA "
tts = gTTS(text,lang="en")
tts.save("output.mp3")
os.system("output.mp3")

from translate import Translator
text = "HEY"
Translator = Translator(to_lang="ta")
Translation = Translator.translate(text)
print(Translation)