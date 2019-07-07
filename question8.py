filename = open(input("Enter file name: "))

for i in filename:
    i = i.rstrip().upper()

    print(i)
