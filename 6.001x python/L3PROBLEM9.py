# Program that guesses your number
low = 0
high = 100
guess = (100 + 0)/2
found = False
userClue =''
properInput = False
print('Please think of a number between 0 and 100!')
while found == False:
        print('Is your secret number ' + str(guess) +'?')
        userClue = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guess correctly. "))
        if userClue == 'h':
            high = guess
        elif userClue == 'l':
            low = guess
        elif userClue == 'c':
            print('Game over. Your secret number was: ' + str(guess))
            found == True
            break
        else:
            print('Sorry, I did not understand your input.')
        guess = (high + low)/2
            
        
            
            
      
         
        
    
    
    