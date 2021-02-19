# print("Hello World")

#PRINT FUNCTION
# print("   /1")
# print("  / 1")
# print(" /  1")
# print("/___1")

#VARIABLES

# character_name = "John"
# character_age = "35"
# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + " years old. ")

# character_name = "Dave" <-- NEW VARIABLE
# print("He really liked the name " + character_name + ", ")
# print("but didn't like being " + character_age + ".")

#EXAMPLE
# name = "Aaron"
# age = "20"
# print(name + " was bored of being " + age + ". ")
# print("He also didn't like the name " + name + ". ")
# name = "Divock"
# age = "21"
# print ("So he changed his name to " + name)
# print("when he turned " + age + ".")

#STRINGS
# print("Giraffe Academy")  <---- WORDS ON SAME LINE
# print("Giraffe\nAcademy") <---- WORDS ON SEPARATE LINES
# print("Giraffe\"Academy")   <---- QUOTATION MARKS INSIDE PARAMETER

#phrase = "Giraffe Academy"
#print(phrase + " is cool.")
#print(phrase.upper().isupper())
#print(phrase.index("Acad"))


#IMPORTANT FUNCTIONS

#FORMAT FUNCTION
#{}.format(value)
# Apply single index with value
#print("\nLearn {0} programming".format("Python"))
# Apply formatting without index value
#print("Both {} and {} are scripting languages".format("Bash", "Python"))
# Apply multiple index with with index value
#print("\nStudent ID: {0}\nStudent Name: {1}\n".format("c3544165", "Stanaway Aaron"))
# Apply multiple index without any order
#print("{2} is a student of {0} at {3}. He is currently in year {4}, semester {1}".format("the school of Architecture", "2", "Aaron Stanaway", "Leeds Beckett University", "3"))

#FIND FUNCTION
#str = "Learn Python programming"
#print(str.find("on")

#thistuple =  ("apple", "banana", "cherry", "apple", "banana")
#print(thistuple)

#thisdict =	{
#  "brand": "Ford",
 # "model": "Mustang",
 # "year": 1964
#}
#print(thisdict)

#thisset = {"apple", "banana", "cherry", "apple"}
#print(thisset)







#NUMBERS
#'print(abs(-x))' = absolute value of -x
#'print(pow(x, y))' = x raised to the power of y
#'print(x%y))' = remainder when x is divided by y
#'print(max(x, y))' = largest number out of x and y
#'print(min(x, y))' = smallest number out of x and y
#'print(round(x.y))' = rounds to nearest number

#IMPORT PYTHON MATH
#from math import *  <----- Type this out to access extra maths functions
#print(floor(3.8)) = rounds down
#print(ceil(3.8)) = rounds up
#print(sqrt(36)) = 6 = finds the square root of the value


#GETTING INPUT FROM SOMEONE
#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print("Hello " + name + "! You are " + age)

#CALCULATOR
#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#------ 'int' used only for full integers
#------ 'float' used for decimals!!!
#result = float(num1) + float(num2)
#print(result)

#MADLIBS
#colour = input("Enter colour: ")
#plural_noun = input("Enter plural noun: ")
#name = input("Enter name: ")

#print("Roses are " + colour)
#print(plural_noun + " are blue")
#print(name + " is shit at coding")

#lucky_numbers = [4, 8, 15, 16, 23, 42]
#friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
#lucky_numbers.sort()
#print(lucky_numbers)


#FUNCTIONS
#def say_hi():
#    print("Hello Aaron!")
#say_hi()

#1 PARAMETER
#def say_hi(name):
#    print("Hello " + name + "!")
#say_hi("Steve")
#say_hi("Mike")

#2 PARAMETERS
#def say_hi(name, age):
#    print("Hello " + name + ", you are " + age)
#say_hi("Steve", "26")
#say_hi("Mike", "35")


#IF STATEMENTS
#is_male = False(/True)

#if is_male:
#    print("You are a male")
#else:
#    print("Your are not a male")


# is_male = False
# is_tall = False
#
# if is_male and is_tall:
#     print("You are male and tall")
# elif is_male and not(is_tall):
#     print("You are male but not tall")
# elif is_tall and not(is_male):
#     print("You are tall but not male")
# else:
#     print("You are neither male or tall")


# emp_file = open("employees.txt", "a")
#
# emp_file.write("\nKelly = Customer Service")
#
# emp_file.close()

# from Question import Question
#
# Question_prompts = [
#     "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n"
#     "What colour are oranges?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n"
#     "What colour are bananas?\n(a) Red/Green\n(b) Yellow\n(c) Orange\n\n"
# ]
#
# questions = [
#     Question(Question_prompts[0], "a"),
#     Question(Question_prompts[1], "c"),
#     Question(Question_prompts[2], "b")
# ]
#
# def run_test(questions):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#
#     print("You got " + str(score) + "/" + str(len(questions)) + " correct.")


from question import Question
from question import Quiz

list_of_questions = [
    Question("Where do we live?", ["Leeds", "Manchester", "Hull", "Liverpool"], "Leeds"),
    Question("Where is aaron from?", ["Leeds", "Chester", "Hull", "Liverpool"], "Chester")
]

quiz = Quiz()
quiz.add_questions(list_of_questions)
quiz.start_quiz()



#
# q3 = Question("Where is caleb from?", ["Leeds", "Manchester", "Hull", "Liverpool"], "Hull")
# q4 = Question("How old am I?", [1, 2, 3, 4, 5], 5)
