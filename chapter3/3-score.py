score = input('Enter a score between 0 and 1: ')

try:
    score = float(score)
    assert score >= 0 and score <= 1
except:
    print('Bad score')
    exit()

if score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
else:
    grade = 'F'

print('Your grade:', grade)