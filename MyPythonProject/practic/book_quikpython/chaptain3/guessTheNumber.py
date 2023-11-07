import random
guessNumber=random.randint(1,20)
print('thinking number between 1 to 20')
for guesstime in range(1,7):
    print('thake a guess')
    guess=int(input())

    if guessNumber<guess:
        print('high')
    elif guessNumber>guess:
        print('lower')
    else:
        print('correct')
    