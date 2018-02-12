from urllib.request import urlopen
content = urlopen('http://54.68.89.68/timeset/ip/').read()
print (content)
