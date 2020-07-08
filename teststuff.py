# socket library will give us TCP sockets access
# A port is an applicaiton-specific/process-specific software communications endpoint
# It allows multiple networked applications to coexist on the same server
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) ) # ('host', port)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')
mysock.close()

# above code is sending POST and receiving GET request (web browser)
# HTTP/1.1 200 OK
# Date: Wed, 08 Jul 2020 05:53:10 GMT
# Server: Apache/2.4.18 (Ubuntu)
# Last-Modified: Sat, 13 May 2017 11:22:22 GMT
# ETag: "a7-54f6609245537"
# Accept-Ranges: bytes
# Content-Length: 167
# Cache-Control: max-age=0, no-cache, no-store, must-revalidate
# Pragma: no-cache
# Expires: Wed, 11 Jan 1984 05:00:00 GMT
# Connection: close
# Content-Type: text/plain

# But soft what light through yonder window breaks
# It is the east and Juliet is the sun
# Arise fair sun and kill the envious moon
# Who is already sick and pale with grief

# most websites use UTF-8 encoding

import urllib.request
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())

# Web Scraping: program or script pretends to be a browser and retrieves web pages,
# looks at those web pages, extracts information, and then looks at more web pages

# Search engines scrape web pages - we call this "spidering the web" or "web crawling"
# BeautifulSoup library is used for parsing HTML and extracting data from HTML documents

import json
data = '''
  [
    { 'id' : '001',
      'x' : '2',
     'name' : 'Quincy'
    } ,
    { 'id' : '009',
      'x' : '7',
      'name' : 'Mrugesh'
    }
  ]
'''
info = json.loads(data)
print(info[1]['name']) # Mrugesh

# API - Application Program Interface

# class PartyAnimal:
#     x = 0
#     def party(self):
#         self.x = self.x + 2
#         print(self.x)

# an = PartyAnimal()
# an.party() # 2
# an.party() # 4

class PartyAnimal:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print(self.name,'constructed')
    def party(self):
        self.x = self.x + 1
        print(self.name,'party count',self.x)

q = PartyAnimal('Quincy') # Quincy Constructed
m = PartyAnimal('Miya') # Miya Constructed

q.party() # 'Quincy party count 1'
m.party() # 'Miya party count 1'
q.party() # 'Quincy party count 2'

# Inheritance is ability to create a new class by extending an existing class.

# SQL command would you use to retrieve all users that have the email address quincy@freecodecamp.org
# SELECT * FROM Users WHERE email="quincy@freecodecamp.org"