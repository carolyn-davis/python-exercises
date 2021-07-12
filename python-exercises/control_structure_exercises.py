#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 15:29:50 2021

@author: carolyndavis
"""

# =============================================================================
# 1.) Conditional Basics
# 
# prompt the user for a day of the week, print out whether the day is Monday or not
# 
# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
# 
# create variables and make up values for
# 
# the number of hours worked in one week
# the hourly rate
# how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours
# =============================================================================


today = 'monday'
question = 'What day of the week is it?'

guess = str(input(question))
    
if guess != today:
    print("I don't know what day it is.")
else:
    print("Today is Monday")
# =============================================================================
#  --
# =============================================================================
    
 
question = 'Tell me a day of the week:'    
bus_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
week_end = ['saturday', 'sunday']

guess = str(input(question))

if guess in bus_week:
    print("That day is a weekday.")
if guess in week_end:
    print("That day is a weekend day.")  
# =============================================================================
# 
# =============================================================================
weekly_hours = 30
hourly_rate = 10 
over_time = 0


if weekly_hours > 40:
    over_time = hourly_rate * 1.5 * (weekly_hours - 40)
    weekly_paycheck = (40 * hourly_rate) + over_time
    
else:
    weekly_paycheck = weekly_hours * hourly_rate
    
# =============================================================================
# 2.) Loop Basics
# 
# While
# 
# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.    
# =============================================================================
i = 5
while i <= 15:
    print(i)
    i += 1

# =============================================================================
# 
# =============================================================================
#Create a while loop that will count by 2's starting with 0 and ending at 100. 
#Follow each number with a new line.
counter = 0
while counter <= 100:
    print(counter)
    counter = counter + 2
    
# =============================================================================
# Alter your loop to count backwards by 5's from 100 to -10.
# =============================================================================
counter = 100
while counter >= -10:
    print(counter)
    counter = counter - 5
    
# =============================================================================
# Create a while loop that starts at 2, and displays the number squared on each line 
# while the number is less than 1,000,000. Output should equal:
# =============================================================================
counter = 2
while counter < 1000000:
    print(counter)
    counter *= counter  # counter = counter * counter
    
# =============================================================================
# Write a loop that uses print to create the output shown below.
# =============================================================================
counter = 100
while counter >= 5:
    print(counter)
    counter = counter - 5
    
# =============================================================================
# For Loops
# 
# Write some code that prompts the user for a number, then shows a multiplication table up 
# through 10 for that number.
# =============================================================================

statement = "Input a number:"
user_answer = int(input(statement))
multip_table = [1,2,3,4,5,6,7,8,9,10]
for number in multip_table:
    ans = user_answer * number
    print(f'{user_answer} x {number} = {ans}')   #variables need curlies in f string!
    
# =============================================================================
# Create a for loop that uses print to create the output shown below. 
# =============================================================================
rep_numbers = [1,2,3,4,5,6,7,8,9]
for number in rep_numbers:
    print(str(number) * number)
    
# =============================================================================
# break and continue
# 
# Prompt the user for an odd number between 1 and 50. Use a loop and a break statement 
# \to continue prompting the user if they enter invalid input. (Hint: use the isdigit method on 
# strings to determine this). Use a loop and the continue statement to 
# output all the odd numbers between 1 and 50, except for the number the user entered.
# =============================================================================

question = "Enter an odd number between 1 and 50:"
# user_answer = input(question)

flag = False

numbers = [num for num in range(1, 51)]
# while user_answer.isdigit() == False:
while flag == False:
    user_answer = input(question)
    print(f'Number to skip is: {user_answer}')
    numbers = [num for num in numbers if num != int(user_answer)]
    if user_answer.isdigit() and int(user_answer) % 2 == 1:
        [print(f"Here is an odd number: {num}") for num in numbers if num % 2 == 1]
        break
    
# =============================================================================
# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that 
#  the input function returns a string, so you'll need to convert this to a numeric type.)    
# =============================================================================

question = "Enter a positive number:"


while counter > 0:
    user_input = int(input(question))
    print(counter)
    counter += 1
    
    
# =============================================================================
# Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number 
# the user entered down to 1.
# =============================================================================

prompt = "Enter a positive integer:"
user_answer = int(input(prompt))
numbers = [num for num in range(1, user_answer + 1)]
numbers.reverse()
print(numbers)

# =============================================================================
# 3.) Fizzbuzz Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
# =============================================================================
    
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

# =============================================================================
# Display a table of powers.
# 
# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.
# =============================================================================


prompt = "Enter an integer:"
user_answer = int(input(prompt))
print(f'number | squared | cubed')
for number in range(1, user_answer + 1):
    square_ans = number * number
    cubed_ans = number * square_ans
    print(f'{number}      | {square_ans}       | {cubed_ans}')




              
# =============================================================================
# Convert given number grades into letter grades.
# 
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
# 
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0
# =============================================================================

letter_grades = [{"A" : [i for i in range(88, 101)]},
                 {"B" : [i for i in range(80, 88)]},
                 {"C" : [i for i in range(67, 80)]},
                 {"D" : [i for i in range(60, 67)]},
                 {"F" : [i for i in range(0, 60)]}]
#print(letter_grades)



flag = 'Yes'
while flag != 'no':
    prompt = "input numerical grade from 0 to 100:"
    
    grade = int(input(prompt))
    
    for grades in letter_grades:
        for letter, values in grades.items():
            if grade in values:
                print(letter)
                flag = str(input('Do you want to continue? (Yes/No)')).lower()

                           
# =============================================================================
# Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.
# 
# Prompt the user to enter a genre, then loop through your books list and 
# print out the titles of all the books in that genre.
# =============================================================================

book_list = [
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "romance"},
    {"title": "Hatchet", "author": "Gary Paulsen", "genre": "adventure fiction"},
    {"title": "Atlas Shrugged", "author": "Ayn Rand", "genre": "philosophical fiction"}]


# for book in book_list:
#     if book["title"] == 'Hatchet':
#         print(book)

prompt = "Enter a genre in on of these categories: romance, adventure fiction, philosophical fiction:"        
user_answer = str(input(prompt))
for book in book_list:
    if book["genre"] == user_answer:
        print(book)    


     
     
     
     