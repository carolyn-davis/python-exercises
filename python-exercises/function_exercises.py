#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 17:03:59 2021

@author: carolyndavis
"""

# =============================================================================
# Define a function named is_two. It should accept one input and return True if the passed input
# is either the number or the string 2, False otherwise.
# =============================================================================


def is_two(guess):  #guess is standing for the input it will represent 
    if guess == 'two' or guess == 2:  #condition stating passed input should be string/int
        return True #if the guess is right (two or 2) it will return True
    else:
        return False  # all other inputs will return False

is_two("two")
# =============================================================================
# 
# Define a function named is_vowel. It should return True if the passed string is a vowel, 
# False otherwise.
# =============================================================================

def is_vowel(test):  #test serves as the input for the function
    if test in ['a', 'e', 'i', 'o', 'u''A', 'E', 'I', 'O', 'U']:   #condition stating if the input matches the list of vowels
        return True #if the above condition is met it will return True
    else:
        return False #all consonants/numbers/etc will return false
is_vowel('e')

# =============================================================================
# Define a function named is_consonant. It should return True if the passed string is a 
# consonant, False otherwise. Use your is_vowel function to accomplish this.
# =============================================================================

def is_consonant(test): #test for input
    if test not in ['a', 'e', 'i', 'o', 'u''A', 'E', 'I', 'O', 'U']:  #using is_vowel list to to def consonants
        return True #if test not in vowel list, return true for consonant 
    else:
        return False  #vowels/numbers/etc false
is_consonant('a')

# =============================================================================
# Define a function that accepts a string that is a word. The function should capitalize 
# the first letter of the word if the word starts with a consonant.       
# =============================================================================

def accepted(word):   
    if is_consonant(word) == True: #using function from prior question to call on consonants
        return word.capitalize() #returns words that are consonants and captalizes their first letter if True
    else:
        return word #else doesnt start with a consonant, return false

accepted('india')

# =============================================================================
# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1)
#  and the bill total, and return the amount to tip.
# =============================================================================
#make a function

# x = 0.20
# percentage = "{:.0%}".format(x)
# print(percentage)

def calculate_tip(tip_perc, bill_total):   #created two variables  for the function to run through
    if tip_perc < 1:  #in the event the users uses this % format for tip calc
        return tip_perc * bill_total #return the user inputted tip_perc times the bill_total
    
    else:
        tip_perc = tip_perc / 100 #if the user decides to input over 1 for whatever reason or makes the mistake of entering whole num
        return tip_perc * bill_total
calculate_tip(3, 100)       

# =============================================================================
# Define a function named apply_discount. It should accept a original price, and a 
# discount percentage, and return the price after the discount is applied.
# =============================================================================

def apply_discount(original_price,discount_perc):
    if discount_perc < 1:  #to attend to decimal format
        return original_price - (original_price * discount_perc) #calculate the discount by multip the perc and the og price.
    else:                                                           #this return discount as a dec that can be sub from og price
        discount_perc = discount_perc / 100  #if 15 for 15% is inputted, this algo accounts for that
        return original_price - (original_price * discount_perc) # just like first return

apply_discount(6,15)


# =============================================================================
# Define a function named handle_commas. It should accept a string that is a number that 
# contains commas in it as input, and return a number as output.
# =============================================================================

def handle_commas(user_input):  #function created to handle any input from call function
    # if "," in user_input:
    return user_input.replace(',', '')  #returns any user input like 1,000 inputted as a string
                                        #replace() method replaces comma with a space
handle_commas("1,000")

# =============================================================================
# Define a function named get_letter_grade. It should accept a number and return the 
# letter grade associated with that number (A-F).
# =============================================================================

def get_letter_grade(number):    #runs any argument, such as numeric value as stated in parentheses
    grade_book = [{"A" : [i for i in range(90, 101)]},  #for loop runs the argument through a range of numbers starting
                  {"B" : [i for i in range(80, 90)]},   #--> starting with the first number and stopping but not including the last #
                  {"C" : [i for i in range(70, 80)]},   #from 0 up to but not including 101
                  {"F" : [i for i in range(0, 70)]}]
    for grades in grade_book:      #this for loop runs the qualifying argument above
        for letter, values in grades.items(): #if letter aligns with a value in the list
            if number in values:
                return letter  #return the letter corresponding with numeric input
        
                  
  

get_letter_grade(55)


# =============================================================================
# Define a function named remove_vowels that accepts a string and returns a string with all 
# the vowels removed.
# =============================================================================

def remove_vowels(words):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']   #list specifying what the function should avoid
    words = list(words) #runs the argument as a list
    words = [letter for letter in words if letter not in vowels] #if the argument is not in the vowels list...
    return "".join(words) #join the consonant letters in the words not containing vowels/ 

remove_vowels('pooopoloigicalallly')

# =============================================================================
# Define a function named normalize_name. It should accept a string and return a 
# valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed
# =============================================================================


# x = "my_word" 
# x = x.split("_")[1] 

def normalize_name(words):
    words = words.lower()           #strings inputted will be made lower case
    words = words.strip()           #strings inputted will be stripped of white space
    words = words.replace(' ', '_') #strings inputted with a space will be replaceed with underscore
    return words

normalize_name('bagle Stuff ')


# =============================================================================
# Write a function named cumulative_sum that accepts a list of numbers and returns a 
# list that is the cumulative sum of the numbers in the list.
# =============================================================================
import pandas as pd                #imports math library 

def cumulative_sum(num_list):       #expect a collection of nums
    
    num_list = pd.Series(num_list)  #numbers inoutted should present as a series
    num_list = num_list.cumsum()    #numbers inputted will be added together cdumulatively
    
    return num_list

    
cumulative_sum([1,1,1]) 

# =============================================================================
#                                 BONUS
# =============================================================================

# =============================================================================
# Create a function named twelveto24. It should accept a string in the format 10:45am or 
# 4:30pm and return a string that is the representation of the time in a 24-hour format.
#  Bonus write a function that does the opposite.
# =============================================================================

def twelveto24(str1):   #argument will be a string
      
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "AM" and str1[:2] == "12":   #checking to see if last elements are AM and time 12
        return "00" + str1[2:-2]  #return 00 in place of index 1200am to 0000 PM
          
    # remove the AM    
    elif str1[-2:] == "AM": #if the string contains AM return everything except AM at position -2
        return str1[:-2] #remove the AM if present
      
    # Checking if last two elements of time
    # is PM and first two elements are 12   
    elif str1[-2:] == "PM" and str1[:2] == "12": #checking to see if PM is apart of last two elements in argument and 12 at position 2
        return str1[:-2] #returns elements that meet these conditions
          
    else:
          
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:5]  #if conditions present return a string that 
                                                     #has had 12 hours added to hour inputted with removal of PM
# Driver Code        
print(twelveto24("11:00AM"))


# =============================================================================
# Create a function named col_index. It should accept a spreadsheet column name, 
# and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27
# =============================================================================

def col_index(index_column):
    column_list = {"A": 1, "B": 2, "AA": 27}
    index_column = column_list[index_column]
    # for index in column_name:
    #     for number, in values in numbers.items():
    #         if column_name in values:
    #             return column_name
    
    return index_column


col_index('AA')





