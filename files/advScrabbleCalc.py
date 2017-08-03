#values sets a point value to each letter of the alphabet
values = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, 
          "j": 8,"k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
          "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10,
          "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, 
          "J": 8,"K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1,
          "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}

def score():                                                        #score is a function that will run given one parameter (the word you want to find the score of)
    word = str(raw_input("What is your scrabble word? "))           #this asks for the user to input their word and sets it as a string to the variable word
    total = 0                                                       #total initializes total to 0, this is important because it will reset the value everytime you call the function.
    for letter in word:                                             #for loop will find take each letter in your parameter (word) and get that value
        total += values[letter]                                     #this is inside the loop and will take the value of each letter and add it to the total
    print total                                                     #this returns the total so that you can print it
    another = str(raw_input("Do you have another word? Y or N: "))  #will allow you to continue running the program or stop the program
    while another=="Y" or another=="y":                             #if user enters y then they will be allowed to calculate the total for another word
        score()
    else:                                                           #if a user enters n then it will tell them "thanks for playing" and stop the program
        end()
                                                    
def end():
    print "Thank you for playing!" 

score()                                                     #calling the function allows for the program to run on start