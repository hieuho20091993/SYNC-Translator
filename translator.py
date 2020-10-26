from googletrans import Translator

sentence = input()

translator = Translator()

translated_sentence = translator.translate(sentence, src='en', dest='vi')
print (translated_sentence.text)