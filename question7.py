sm=0
count=0
average=0


while True:
try:
num = raw_input('Please enter a number: ')
if (num == 'done'):
print('Total: ',str(sm),'Count: ',str(count),'Average: ',str(average))

break
else:

value = float(num)
sm = value + sm
count = count +1
average = sm / count

except :
print('Try again')
