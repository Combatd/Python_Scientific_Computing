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
print(word.find("na"))
