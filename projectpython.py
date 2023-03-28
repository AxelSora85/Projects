#Nathan Ford
#4/12/2021
#I have neither given nor received unauthorized aid in completing this work, nor have I presented someone else's work as my own
#sources used: github.com


import random

animewordss =[
    'rasengan',
    'itachi',
    'zangetsu',
    'naruto',
    'ichigo',
    'titan',
    'getsugatensho',
    'jaeger',
    'ackerman',
    'banki',
]

def start():
    anime= random.choice(animewordss)                                  #takes a random word from ther list and returns it in uppercase
    return anime.upper()
bigbrain=start()


def roundstart(anime):
    completedword= "_" * len(anime)
    randomwords= False                                               #the listed word will equal false until the right attempt is given
    letters=[]
    words=[]
    attempts=6
    print(" lets play hang man!, you have 6 attempts! \n")
    print("number of attempts ",attempts)
    print("\n")
    while not randomwords and attempts > 0:
        print(completedword)
        attempt= input("please guess a letter: ").upper()                #ask the user to enter a letter to start hangman then will display the lenght of word and filled letters on next turn.
        
        
        


        if len(attempt) == 1 and attempt.isalpha():                              # the length of the attempt will be = to 1 and will return the True if all charcters typed in are letters otherwise later on it will return false
            if attempt in letters:
                print("you already guessed this letter ", attempt)


            elif attempt not in anime:
                    print(attempt, "Letter is incorrect")                 #if the attempt is wrong it will subtract 1 from attempts
                    attempts= attempts-1
                    letters.append(attempt)


            else:
                print("Nice!", attempt, "is in the word")
                letters.append(attempt)
                listedwords=list(completedword)
                pickout=[i for i, letter in enumerate(anime) if letter == attempt]      #using enumrate here will return the iterable into the form of a enumrate object   
                for index in pickout:
                    listedwords[index] = attempt
                    completedword = "".join(listedwords)
                if  "_" not in completedword:
                    randomwords= True                                                    
        elif len(attempt) == len(anime) and attempt.isalpha():
            if attempt in words:
                print(" you already guessed that letter", attempt)                                #if the word guessed is already guessed before then this statment will print
            elif attempt != anime:
                print(attempt,"is not a valid letter")                                            #if any numbers or symbols are typed in then this message will pritn as a result and you will lose a turn 
                attempts= attempts - 1
                anime.append(attempt)

                
            else:
                randomwords= True                                                                  #if no errors with the word then its True 
                ompletedword=anime
        else:
            print("not a valid guess ")
            print(completedword)
            print("\n")
    if randomwords:                                                                              #if the word is completed and is not false then the user correctly guessed the word 
        print("congrats! you got the right word you win!, the word was " + str(anime) )
    elif attempts==0:                                                                            #if attempts reaches 0 then this message will be displayed
            print("sorry you ran outta tries the word was "+ str(anime) + " try again!")

roundstart(bigbrain)





               
            


        
