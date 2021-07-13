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

def handle_commas(user_input):
    # if "," in user_input:
    return user_input.replace(',', '')
    
handle_commas("1,000")

# =============================================================================
# Define a function named get_letter_grade. It should accept a number and return the 
# letter grade associated with that number (A-F).
# =============================================================================

def get_letter_grade(number):
    grade_book = [{"A" : [i for i in range(90, 101)]}, 
                  {"B" : [i for i in range(80, 90)]},
                  {"C" : [i for i in range(70, 80)]},
                  {"F" : [i for i in range(0, 70)]}]
    for grades in grade_book:
        for letter, values in grades.items():
            if number in values:
                return letter
        
                  
  

get_letter_grade(55)


# =============================================================================
# Define a function named remove_vowels that accepts a string and returns a string with all 
# the vowels removed.
# =============================================================================

def remove_vowels(words):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    words = list(words)
    words = [letter for letter in words if letter not in vowels]
    return "".join(words)

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
    words = words.lower()
    words = words.strip()
    words = words.replace(' ', '_') 
    return words

normalize_name('bagle Stuff ')


# =============================================================================
# Write a function named cumulative_sum that accepts a list of numbers and returns a 
# list that is the cumulative sum of the numbers in the list.
# =============================================================================
import pandas as pd

def cumulative_sum(num_list):
    
    num_list = pd.Series(num_list)
    num_list = num_list.cumsum()
    
    return num_list

    
cumulative_sum([1,1,1]) 
    