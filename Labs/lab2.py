#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)


        # Enter your own print statements below:
        Greeting = "Hello World, We are currently inside PyCharm IDE"


        # print only first and last of the sentence:
        print(Greeting[0] + Greeting[-1])


        # use slice notation:
        print(Greeting[:4])
        print(Greeting[2:])
        print(Greeting[:])


        # escaping a character:
        print("\tThat\'s Fantastic")


        # find all a's in the input word and count how many there are:
        Position_Of_A = Greeting.find("a")
        print(Position_Of_A)

        Num_Of_A = Greeting.count("a")
        print(Num_Of_A)


        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:


        # append a new element to the list and print:


        # remove from the list in 3 ways:


        # check if the word cake is in your input list:


        # reverse the items in the list and print:


        # reverse the list with the slicing trick:


        # print the list 3 times by using multiplication:



tas = Types_and_Strings()
tas.play_with_strings()
#tas.play_with_lists()
