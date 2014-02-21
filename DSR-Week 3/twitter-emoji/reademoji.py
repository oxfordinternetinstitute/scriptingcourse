# -*- coding: utf-8 -*-#

# emojiList = []
# filein = open("EmojiSources.txt")

# for i in filein:
# 	char = string.split(";")[0]
# 	if len(char) == 4: 
# 		emojiList.append(u"\U0000%s" % char)
# 	elif len(char) == 5: 
# 		emojiList.append(u"\U000%s" % char)
# 	else:
# 		continue
import codecs

x = "1F601"
print u"\U0001F601"


emojiList = [u"\U0001F601",unicode("\U000%s" % x)]
teststr = u"Wow, this is epic! \U0001F601"

print teststr
print emojiList[0] in teststr
print emojiList[1] in teststr
print emojiList[1]