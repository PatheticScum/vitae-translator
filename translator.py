import Translator

data = input('Enter a data to translate.')

translator = Translator(to_lang="RU")
translation = translator.translate(data)

print(translation)
