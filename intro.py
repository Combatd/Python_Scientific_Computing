# temp = "5 degrees"
# cel = 0
# try:
#     fahr = float(temp)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print(cel)

# def fred():
#     print("Zap")

# def jane():
#     print("ABC")

# jane()
# fred()
# jane()

n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1

for i in [2,1,5]:
    print(i)

print(0 == 0.0) # true
print(0 is 0.0) # false
print(0 is not 0.0) # true

for n in "banana":
    print(n) # prints each character

word = "bananana"
print(word.find("na")) # 2

fruit = "banana"
print(fruit[1]) # a

words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
new_str = parts[1] #lar@freecodecamp.org

# dict = {"Fri": 20, "Thu": 6, "Sat": 1}
# dict["Thu"] = 13
# dict["Sat"] = 2
# dict["Sun"] = 9
# print(dict) # {'Fri': 20, 'Thu': 13, 'Sat': 2, 'Sun': 9}

# counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0)) # 0 is default value when not found

counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])

d = dict()
d['quincy'] = 1
d['beau'] = 5
d['kris'] = 9
for (k,i) in d.items(): # key, value
    print(k, i)

# lst = []
# for key, val in counts.items():
#     newtup = (val, key)
#     lst.append(newtup)
# lst = sorted(lst, reverse=True)
# print(lst)

print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )

import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s) # ' non-whitespace followed by @, followed by non-whitespace '
print(lst)