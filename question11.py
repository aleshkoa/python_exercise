filename = input('Enter file name: ')

try:
    fname = open(filename, "r").read().split()
except:
    print('Invalid filename')
    exit()

cleanstring = [''.join(e for e in string if e.isalnum()) for string in fname]

clstring = ''.join(cleanstring)

catstring = clstring.lower()

freq={}

for letter in catstring:
    if letter in freq:
        freq[letter] +=1
    else:
        freq[letter] = 1

items = [(v,k) for k, v in freq.items()]
items.sort()
items.reverse()
print(items)
