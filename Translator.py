from googletrans import Translator
translator = Translator()
print("input your sentence:")
s =input()
out = translator.translate(s, dest="hi")
print(out)
