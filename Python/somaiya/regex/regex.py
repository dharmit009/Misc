# importing regex. 
import re

# A very old programming language and is very cryptic. - REGEX
allLines = open('test.txt')

for eachLine in allLines:
    eachLine = eachLine.rstrip();
    if re.search('^from:', eachLine):
        print(eachLine)


