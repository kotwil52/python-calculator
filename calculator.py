#First number check and convert to from str to int
"""operators = ['+', '-', '*', '%']

def calculation(first_number,second_number, input_user_operator):

   if input_user_operator == "+":
    result = first_number+second_number
    string = "the result is: " + str(result)
    print(string)
   elif input_user_operator == "-":
    result = first_number-second_number
    string = "the result is: " + str(result)
    print(string )
   elif input_user_operator == "*":
    result = first_number*second_number
    string = "the result is: " + str(result)
    print(string)
   elif input_user_operator == "%":
    result = first_number%second_number
    string = "the result is: " + str(result)
    print(string)
   elif input_user_operator:
    print("this is not operator. Please provide operator")




#First number check and convert to from str to int
first_number = input("Give me first number: ")
while  not first_number.isdigit():
 print("this is not digit") 
 first_number = input("Give me first number: ")
first_number = int(first_number)

#operator check

#Second number check
second_number = input("Give me second number: ")
while  not second_number.isdigit():
 print("this is not digit:") 
 second_number = input("Give me second number: ")
second_number = int(second_number)



input_user_operator = input("What is your operator: ")
if input_user_operator in operators:
 calculation(first_number,second_number, input_user_operator)
 print("Yes it was mathematical operator")

else:
 print("this is not operator my friend. Please type operator")
 input_user_operator = input("What is your operator: ")
 calculation(first_number,second_number, input_user_operator)

"""

       # Chat GPT fixed code
operators = ['+', '-', '*', '%']

def calculation(first_number, second_number, input_user_operator):
    if input_user_operator == "+":
        result = first_number + second_number
        string = "The result is: " + str(result)
        print(string)
    elif input_user_operator == "-":
        result = first_number - second_number
        string = "The result is: " + str(result)
        print(string)
    elif input_user_operator == "*":
        result = first_number * second_number
        string = "The result is: " + str(result)
        print(string)
    elif input_user_operator == "%":
        result = first_number % second_number
        string = "The result is: " + str(result)
        print(string)
    else:
        print("This is not a valid operator. Please provide a valid operator")

# First number check and convert from str to int
first_number = input("Give me the first number: ")
while not first_number.isdigit():
    print("This is not a valid digit.")
    first_number = input("Give me the first number: ")
first_number = int(first_number)

# Operator check
input_user_operator = input("What is your operator: ")
while input_user_operator not in operators:
    print("This is not a valid operator.")
    input_user_operator = input("What is your operator: ")

# Second number check
second_number = input("Give me the second number: ")
while not second_number.isdigit():
    print("This is not a valid digit.")
    second_number = input("Give me the second number: ")
second_number = int(second_number)

calculation(first_number, second_number, input_user_operator)
print("Yes, it was a valid mathematical operator.")
input("Press Enter to exit...")


