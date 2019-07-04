def computegrade(score):

score=float(score)

if score>10.0 :
print 'Score too high'

elif score>=9.0 :
print 'Grade A'

elif score>=8.0 :
print 'Grade B'

elif score>=7.0 :
print 'Grade C'

elif score>=6.0 :
print 'Grade D'

else:
print 'F'

try:
score=raw_input('Please enter a score between 0.0 and 10.0')
computegrade(score)

except:
print('Programme has hit an error')
exit()
