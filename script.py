import random

def run_guess(guess,answer):
     if guess > 0 and guess < 11:
            if guess == answer:
                print('You are Genius.')
                return True
     else:
         print('hey, I Said number 1~10')

if __name__ == '__main__':
    answer = random.randint(1, 10)

    while True:
        try:
            guess = int(input('guess a number 1~10:- '))

            if (run_guess(guess,answer)):
                break
           

        except ValueError:
            print('Please enter the number 1~10')
            continue