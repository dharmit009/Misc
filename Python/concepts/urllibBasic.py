import urllib.request, urllib.error, urllib.parse

fhand = urllib.request.urlopen('https://www.duckduckgo.com')
for line in fhand:
    print(line.decode().strip())
