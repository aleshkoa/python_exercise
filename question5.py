try:
    score = float(input('Please enter a score between 0.0 and 10.0: '))
except:
    print('Programme hit an error. Please try again. Make you you enter a numerical value')
    exit()

if score > 10.0:
    print('Score too high, please enter score between 0.0. and 10.0')

elif score>=9.0 :
    print('Grade A')

elif score>=8.0 :
    print('Grade B')

elif score>=7.0 :
    print('Grade C')

elif score>=6.0:
    print('Grade D')

else:
    print('Grade F')
