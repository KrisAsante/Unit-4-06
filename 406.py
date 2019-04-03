# Created by: Chris Asante
# Created on: 3-April-2019
# Created for: ICS3U
# Daily Assignment – Unit 4-06
# The code checks to see if the two strings the user inputs are the same

def check_if_true(first_string, second_string):
    
    first_string = string_1.upper()
    second_string = string_2.upper()
    
    if first_string == second_string:
        return True
    else:
        return False

string_1 = input("Enter string: ")
string_2 = input("Enter next string: ")

answer = check_if_true(string_1, string_2)

print (answer)