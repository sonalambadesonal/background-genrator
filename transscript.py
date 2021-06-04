from translate import Translator
translator= Translator(to_lang="pt")
try:
	with open('C:/Users/LENOVO/Desktop/Translator/tarans.txt',mode = 'r') as my_file:
		text= my_file.read()
		translation = translator.translate(text)
		print(translation)
		with open('C:/Users/LENOVO/Desktop/Translator/tarans-ja.txt',mode='w' ) as my_file2:
			my_file2.write(translation)
except FileNotFoundError as err:
	print('check your path silly!')