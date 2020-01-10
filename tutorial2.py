from time import sleep
def tutorial():
    print("Welcome to your tutorial!")
    sleep(3)
    print("This tutorial will teach you the very basics of python")
    sleep(5)
    x = raw_input("To start off, we will be playing a very short game. Please press enter to begin. ")
    def game():
        print("Hello! And welcome to Guessinator")
        sleep(2)
        maybe = raw_input("To continue, press enter ")
        print("Alright, let's start!")
        sleep(2)
        print("Please choose something from the following list: \n A whale \n A baseball \n An airplane \n A rocket ship \n A boat \n A bicycle \n A dog")
        sleep(9)
        print("please answer the following questions with 'yes' or 'no'")
        sleep(3)
        w = raw_input("Is this thing alive? ").lower()
        if w == "yes":
            w = raw_input("Does this thing live in the water? ").lower()
            if w == "yes":
                print("It's a whale!")
            else:
                print("It's a dog!")
        else:
            w = raw_input("Is this thing water-based? ").lower()
            if w == "yes":
                print("It's a boat!")
            else:
                w = raw_input("Does this thing fly? ").lower()
                if w == "yes":
                    w = raw_input("Does this thing have wings? ").lower()
                    if w == "yes":
                        print("It's an airplane!")
                    else:
                        print("It's a rocket ship!")
                else:
                    w = raw_input("Is this thing thrown? ").lower()
                    if w == "yes":
                        print("It's a baseball!")
                    else:
                        print("It's a bicycle!")
        sleep(2)
        print("Thank you for playing Guessinator!")
    game()
    sleep(3)
    print("This game was very reliant on something called an if/else statement")
    sleep(5)
    print("It was also very reliant on 'raw_input()' variables")
    sleep(5)
    print("The 'raw_input()' allows for you, the player, to write and answer")
    sleep(5)
    print("The 'raw_input' was made into a variable, so it could then run the if/else statements.")
    sleep(5)
    print("A variable can be anything. It could be a single letter, or even the longest word in the dictionary")
    sleep(5)
    print("The if/else statements are used to determine what question to ask next after you've answered.")
    sleep(5)
    print("If you answered yes to an answer, it would then ask a question using the information from the question")
    sleep(6)
    print("If you answered no, the 'else' part would run, and ask a question knowing it wasn't the thing from the question")
    sleep(7)
    print("These statements you're reading right now are shown using the print() function and strings")
    sleep(6)
    print("The string uses quotes to know what text to print")
    sleep(5)
    print("The quotes are inside the parentheses in the 'print()' statement. It will then print the statement.")
    sleep(6)
    print("The final thing you should know about is functions.")
    sleep(5)
    print("Functions use the term 'def' to define a function.")
    sleep(4)
    print("It will look something like this:\ndef tutorial(): \n    words\n    code\n    text")
    sleep(5)
    print("You can simply type 'tutorial()'(as an example) into python, and then the function/code will run.")
    sleep(7)
    print("This has been your tutorial. Thank you for playing and learning.")
    sleep(6)
