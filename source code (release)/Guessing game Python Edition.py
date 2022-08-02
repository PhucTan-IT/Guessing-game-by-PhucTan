import os
import time
import sys
import random

replayGame = "start"

def key_loadGame():
    while True:
        passport = input("Enter passcode: ") #Insert passcode
        if passport=="PhucTan": #Check if passcode is correct
            break
        else:
            print('incorrect, try again')

    os.system('cls')
    os.system('title Please wait...')
    animation = ["Starting game... (|) (|)","Starting game... (/) (/)","Starting game... (-) (-)","Starting game... (\\) (\\)"]

    for i in range(100):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

def menuGame():
    os.system('cls')
    os.system('title Guessing game Python Edition')
    print('-----------------------------------------------------------')
    print('Welcome to Guessing game')
    print(' ')
    print('Try guessing my number!')
    print('-----------------------------------------------------------')
    print('Tip: Read the Instructions before gameplay')
    print('-----------------------------------------------------------')
    print(' ')
    #menu game
    while True:
        start = input('Are you ready to play? (Y/N)(R for instructions) ') #Choice
        if start=='R' or start=='r':
            os.system('cls')
            print(' ') #Instructions
            print('---------------------------------------------------------------------------------------------------')
            print('Help menu:')
            print("- Start, choose Y(y) to play, N(n) to exit")
            print('- Type in a number (Suggestion: 10000)')
            print('- If it shows "lower", enter a lower number')
            print('- If it shows "higher", enter a higher number')
            print('- If you guess right, it will show the number of guesses and the result.')
            print("- If you can't guess or don't know, you can view the answer at guess 50 (not recommended)")
            print('- Depending on how you play, you will discover more ways to win.')
            print('---------------------------------------------------------------------------------------------------')
            print(' ')
        elif start=='Y' or start=='y': #Input: Yes
            break
        elif start=='N' or start=='n': #Input: No
            print(' ')
            exit1 = input('Do you want to quit? (Y/N) ')
            print(' ')
            if exit1=='Y' or exit1=="y":
                print('Program ended')
                print(' ')
                for ext in range(0,10): #End program code
                    if ext==0:
                        exit()
        else: #Check if the input is the valid option
            print("invalid option, try again")

def startGame():
    global replayGame

    os.system('cls')
    print("Let's start \nGood luck :)")
    print(' ')

    list = []
    ans = random.randrange(100, 100000) #Give random number from 100 to 100000
    nInput = 0
    while True: #Guessing field
        print(' ')
        inpt = input("==> ") #Insert number        
        while not(inpt.isdigit()): #Check if the input is a number
            inpt = input("Try again: ") #Replay Insert number            
        inpt = int(inpt)
        list.append(inpt)
        if inpt > ans: #Chk: Number needs to be lower
            print(' ')
            print('Lower!')
        elif inpt < ans: #Chk: Number needs to be higher
            print(' ')
            print('Higher!')
        elif inpt==ans: #Correct answer
            break
        nInput += 1
        if nInput>50:
            print(' ')
            sQuest = input('Have you been stuck? (Y/N): ') #Show answer if player can't guess it          
            if (sQuest.lower()=="y"):
                print(' ')
                print('The answer is: ' +  str(ans))
                print('Type it in!')

    #Answer is correct
    #Give amount of guesses and correct answer
    os.system('cls')
    print('-----------------------------------------------------------')
    print('Congratulations, you guess right!!!')
    print(' ')
    print('You have guessed',nInput+1,'time(s) and have the correct answer:',ans)
    print('-----------------------------------------------------------')
    print(' ')
    opt = input("Do you want to view all of your inputs/numbers/guesses? (Y/N) ")    
    if opt=='Y' or opt=='y':
        #Display all inserted numbers
        os.system('cls')
        print("The numbers/guesses that you have inserted are:", end=' ')
        for inpt in range(len(list)):
            if inpt == len(list)-1:
                print(str(list[inpt]) + ".")
            else:
                print(list[inpt], end=', ')
    replayGame="y"

def main():
    global replayGame

    if replayGame=="start":
        key_loadGame()
    menuGame()
    startGame()    

#Replay Game
while (replayGame!="n" or replayGame=="start"):
    if replayGame=="y":
        replayGame = input('Do you want to replay? (Y/N) ') #Replay prompt
    if (replayGame=='Y' or replayGame=='y' or replayGame=='start'):
        main() #Return to start menu
    elif replayGame=='N' or replayGame=='n':
        print(' ')
        print('Thank you for playing Guessing game')
        print('Program ended')
