#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 09:22:12 2021

@author: carolyndavis
"""
# =============================================================================
# 
# # Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension. 
# Output should be ['MANGO', 'KIWI', etc...]
# =============================================================================
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

#numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)


# =============================================================================
# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like 
# ['Mango', 'Kiwi', 'Strawberry', etc...]
# =============================================================================
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)


# =============================================================================
# 
# # Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
# Hint: You'll need a way to check if something is a vowel.
# =============================================================================

# =============================================================================
# vowel = ['a', 'e', 'i', 'o', 'u', 'y']
# 
# fruits_with_more_than_two_vowels = []
# 
# 
# for char in fruits :
#     if char in vowel :
# =============================================================================
# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

import pandas as pd
from collections import Counter
 
# creating a series of words
series = pd.Series(['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange'])
 


print("\nWords containing atleast 2 vowels")
 
# mapping through the series and checking if count of vowels is >=2
result = series.map(lambda c: sum([Counter(c.lower()).get(i, 0)
                                   for i in list('aeiou')]) == 2)
 
print(series[result])


# =============================================================================
# # Exercise 5 - make a list that contains each fruit with more than 5 characters
# =============================================================================

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
print(long_fruits)


# =============================================================================
# # Exercise 6 - make a list that contains each fruit with exactly 5 characters
# =============================================================================

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

exact_fruits = [fruit for fruit in fruits if len(fruit) == 5]
print(exact_fruits)

# =============================================================================
# # Exercise 7 - Make a list that contains fruits that have less than 5 characters
# =============================================================================
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

little_fruits = [fruit for fruit in fruits if len(fruit) < 5]
print(little_fruits)


# =============================================================================
# # Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
# =============================================================================
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruit_count = [len(fruit) for fruit in fruits]
print(fruit_count)

# =============================================================================
# 
# # Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the
# fruits that contain the letter "a"
# =============================================================================

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_letter_a)

# =============================================================================
# # Exercise 10 - Make a variable named even_numbers that holds only the even numbers
# =============================================================================

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

even_numbers = [number for number in numbers if number % 2 == 0]

# =============================================================================
# # Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
# =============================================================================



odd_numbers = [number for number in numbers if number % 2 == 1]

# =============================================================================
# # Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
# =============================================================================

positive_numbers = [number for number in numbers if number >= 0]


# =============================================================================
# # Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
# =============================================================================

negative_numbers = [number for number in numbers if number <= 0]

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

more_numerals = [number for number in numbers if len(str(abs(number))) >= 2]

# =============================================================================
# 
# # Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. 
# Output is [4, 9, 16, etc...]
# =============================================================================

number_squared = [number**2 for number in numbers]
print(number_squared)


# =============================================================================
# # Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
# =============================================================================

odd_negative_numbers = [number for number in numbers if number % 2 == 1 and number < 0]

# =============================================================================
# # Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
# =============================================================================

numbers_plus_five = [number + 5 for number in numbers]


# =============================================================================
# # BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. 
# *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
# =============================================================================
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
    

prime_numbers = [is_prime(number) for number in numbers ]


    
    
