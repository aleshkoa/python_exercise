fname = raw_input("Enter file name: ")

if fname == "money makes the world go round":
print'mo money mo problems'
exit()
else:

try:
filename = open(fname)

for i in filename:
i = i.rstrip().upper()
print i
except:
print 'Invalid file name.'
exit()
