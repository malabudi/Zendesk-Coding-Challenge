# Zendesk-Coding-Challenge
Name: Mohamad Alabudi

Installation Instructions:
1. Python 2.7 or 3.6+ is required to run the python file.
2. This program uses the requests module installed which is supported in python 2.7 & 3.6+.
3. If the requests module has not been installed, assuming your current version of python supports it then running "$ python -m pip install requests" in the terminal of your choosing will install the module. If your python is on a different interpreter such as anaconda3, just replace pip with anaconda3 or your respective interpreter path to install the module

Usage instuctions:
1. When you run the tickets viewer program, you will be greeted with a welcome message along with the main menu with two options to type into the terminal, "menu" and "exit"
2. "1" will open up another sub menu with three options to choose from, the user must choose form 1 to 3.
3. "2" will close the program
4. Once the sub menu has been chosen by typing "1", you will be provided with 3 options to choose from.
5. Selecting "1" in the sub menu will display all tickets fetched from the API to the user, if there is more than 25 you will be able to page through them
6. Selecting "2" in the sub menu will display a specific ticket by asking the user to enter a valid ticket id
7. Selecting "3" will close the program for you
