def computegrade(score):

        score = float(score)

        if score>10.0 :
            print('Score too high')

        elif score <0 :
            print('Score too low')
            
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


inputscore = input('Please input a score between 0 and 10: ')

computegrade(inputscore)
