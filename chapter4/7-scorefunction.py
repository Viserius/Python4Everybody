score = input('Enter a score between 0 and 1: ')

try:
    score = float(score)
    assert score >= 0 and score <= 1
except:
    print('Bad score')
    exit()

def determineGrade(score):
    if score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'

grade = determineGrade(score)
print('Your grade:', grade)