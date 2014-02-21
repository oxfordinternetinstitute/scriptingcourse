# -*- coding: utf-8 -*-#
import re 

filein = open("Emoji_web_table.html").read()


emojireg1 = re.compile("<td class=\"code\">.*</td>\s*<td class=\"code\">.*</td>\s*<td class=\"name\">.*</td>")

result = emojireg1.findall(filein)
emojidict = {}

for i in result: 
	lines = i.split("</td>")[:-1]
	emojis = [x.split(">")[1].strip() for x in lines]
	emojidict[emojis[1]] = emojis[2]

strout = "["
for c,i in enumerate(emojidict.keys()):
	strout += "\"%s\"," % i
	if c % 8 == 0:
		strout += "\n" 
		
print strout