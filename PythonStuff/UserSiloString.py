#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import re
import sys

user_sledid = sys.argv[1]

#Checking input to make sure no letters are entered.
for i in user_sledid:
	if i.isdigit():
		#print i
		continue
	else:
		break
#Slicing the last for digits of the string and printing in reverse.
#print user_sledid[-1] + user_sledid[-2] + user_sledid[-3] + user_sledid[-4]
#print user_sledid

user_reverse = user_sledid[-4:]
new_text = user_reverse[::-1]
print new_text[0:2] + '/' + new_text[2:] + '/' + user_sledid
