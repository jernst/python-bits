import random

print( "I'm thinking of a secret number between 1 and 100. Can you guess it?" )
secret = random.randint( 1, 100 )

while True:
    guess = raw_input( "Your guess: " )

    try:
        guessedNumber = int( guess )

        if guessedNumber == secret:
            break

        if guessedNumber < secret:
            print( "Sorry. Your guess is too low!" )
        else:
            print( "Sorry. Your guess is too high!" )

    except ValueError:
        print( "You must enter a whole number" )

print( "Congratulations, you found the secret! It was %d." % secret )
