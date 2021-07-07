@echo off
:passport
cls
title Enter Password
echo Enter PASSWORD before game.
set/p "pass=Password: "
if %pass%==PhucTan goto begin
goto passport

:begin
cls
color 0
title Guessing game by Phuc Tan
set /a guessnum=0
set /a answer=%RANDOM%
set variable1=ans
echo -----------------------------------------------------------
echo Welcome to Guessing game
echo. 
echo Try guessing my number!
echo -----------------------------------------------------------
echo Tip: Read the Instructions before gameplay
echo -----------------------------------------------------------

:CONFIRM
echo.
echo Are you ready to play? (Y,N,R,L) (R to see the instruction, L to lock the game)
set/p "cho=Type your choice here >>> "
if %cho%==Y goto start
if %cho%==y goto start
if %cho%==n goto exit1
if %cho%==N goto exit1
if %cho%==R goto RULES
if %cho%==r goto RULES 
if %cho%==L goto passport
if %cho%==l goto passport
echo Invalid Answer
goto CONFIRM

:start
echo.
echo Let's start!!!
echo Good luck :)
goto top
:lo2
cls
set /a guessnum=0
set /a answer=%RANDOM%
set variable1=ans
goto start2
:start2
echo.
echo Let's start!!!
echo Good luck :)
goto top
:top
echo. 
set /p guess=
echo. 
if %guess% GTR %answer% ECHO Lower! 
if %guess% LSS %answer% ECHO Higher! 
if %guess%==%answer% GOTO EQUAL
if %guess%==exit GOTO exit2
set /a guessnum=%guessnum% +1
if %guess%==%variable1% ECHO You've been stuck?, the answer is %answer%
goto top
:equal
cls
echo -----------------------------------------------------------
echo Congratulation, you guess right!!! 
echo. 
echo You guessed %guessnum% time(s) and have the answer: %answer%. 
echo -----------------------------------------------------------
echo. 
goto ab
:ab
echo Do you want to re-play? (Y,N)
set/p "cho=Type your choice here >>> "
if %cho%==Y goto lo2
if %cho%==y goto lo2
if %cho%==n goto dong
if %cho%==N goto dong
echo Invalid Answer
goto ab
:RULES
echo.
echo --------------------------------------------------------------------------------
echo Instruction:
echo - Start, choose Y or y to play, N or n to exit
echo - Type in a number (Suggestion: 100000)
echo - If it shows as "lower", enter a lower number  
echo - If it shows as "higher", enter a higher number
echo - When you enter a number (eg: 50000), the previous numbers (60000,...) you
echo see it keeps saying "lower" but on this number you see it's now as "higher", 
echo then switch from the row of numbers you just used to the next row of number 
echo and other rows of numbers and vice versa (with greater than and less than).
echo - If you guess right, it will show the number of guesses and the result.
echo - If you can't guess or don't know, type "ans" to see the answer
echo - While you play, If you want to exit the game, just type "exit" to exit game
echo - Depending on how you play, you will discover more ways to win.
echo --------------------------------------------------------------------------------
goto CONFIRM
:exit1
echo.
echo Do you want to close this window? (Y,N)
set/p "cho=Type your choice here >>> "
if %cho%==Y goto dong
if %cho%==y goto dong
if %cho%==n goto CONFIRM
if %cho%==N goto CONFIRM
echo Invalid Answer
goto exit1
:exit2
echo.
echo Do you want to close this window? (Y,N)
set/p "cho=Type your choice here >>> "
if %cho%==Y goto dong
if %cho%==y goto dong
if %cho%==n goto top
if %cho%==N goto top
echo Invalid Answer
goto exit2
:dong
echo.
echo Now you can close this window!
echo.	
pause