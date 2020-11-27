from googletrans import Translator


translator = Translator()

while 1:
    text = input("Введите текст ")
    translated_text = translator.translate(text, dest='en')
    print(translated_text.text)
   