file = input("Enter file name: ")
regex = input("Please enter for string to search: ")

file = open(file)
count = 0

for line in file:
    if regex in line:
        count = count + 1
        print(line)

print("Total number of lines that match string ",regex, " is ",str(count))
