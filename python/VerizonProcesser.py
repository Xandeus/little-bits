import re
txtmessage = open('/home/xandeus/Documents/textmessages.txt')
b = "<body>"
text = txtmessage.read()
messages = re.findall("<body>.*?</body>", text)
cm1 = re.sub("</body>", '', ' '.join(messages))
cm2 = re.sub("<body>", '', (cm1))
cm3 = re.sub("&amp;apos;", "'", (cm2))

print(cm3)
processedFile = open('pText.txt', 'w')
processedFile.write(''.join(cm3))
processedFile.close()
