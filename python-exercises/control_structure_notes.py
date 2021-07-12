#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:37:10 2021

@author: carolyndavis
"""

#Control Structure Notes with Ryan 

#Example: Condionals, loops (allow us to execute code under certain conditions)

#Conditionals: if, this, then, that

#If statements: Most Basic way to execute code conditionally--->
i_like_coffee = True #its either truth or not

if i_like_coffee:    #if followed by a variable or something that will evaluate to true or false then colon
    print('I like coffee!')
    print('Coffee is the best!')

#condition evaluates a boolean value 

#if/else

it_is_raining = False
if it_is_raining:
    print('Better bring an um')
else: #else is indented back under the if because this condition will be evaluated if the first one fails
    print('Looks like a nice day') #prints this statemtn because the first evaluation failed 
    
    
#if with elif/elsif


coffee_pref = 'medium'   #so far these conditions are only running once

if coffee_pref == 'dark':
    print('I love a good dark')
elif coffee_pref == 'medium':
    print('Middle of the road huh?')
elif coffee_pref == 'light':
    print('light roast has the most caff')
else:
    print('how bout tea')
    
# =============================================================================
#     What if we want to run the condition in repetition L O O P S
# =============================================================================



#for loop runs the loop a set number of times  ****** usually using this type of loop in data science
#while loops are used for running a block of code until the condition is met 



#For LOOP is commonly used for iterables, objects that can be enumerated: LISTS OR STRINGS
#example, iterating across a list
for number in range(1, 4): #number is defined as variable with for/// checks to see if variable is iterable in the collection/range
    print(number) #loops up to but not including the number 4 so 1,2,3


for letter in 'abcde': #loops runs through the letters but does not include the letter e
    print(letter) #when we are out of strings (components of the list) the loop stops
    
    
#What if we have a list of strings?

languages = ['bash', 'python', 'R', 'clojure']

for programming_language in languages:  #for loop allows for the creation of new variables in a loop. programming_language is the creation
    print(f'{programming_language} is a nice programming language') #doesn't need a range to run throught the loop start to finish


staff = ['Ryan', 'Faith', 'John']

in_office = ['Faith', 'John']

for person in staff:
    if person in in_office:
        print(f"{person} is ready for your question")
    else:
        print(f'{person} is out of the office and looking forward to helping later')


#Sometimes with a FOR LOOP, we need BOTH item on the list and the index of that item
#Manual example:
    
operating_systems = ["Linux", "Windows", "Mac OS", "Solaris"]

i = 0 #set index to zero, manually
print(f"The item at index {i} is {operating_systems[i]}")

#how would you get the index and each item from the list:
    #for index, new_variable in enumerate(list_variable):
#i, the new variable unpacks the tuple
        
for i, os in enumerate(operating_systems):   #enumerate gives us tuples with index and the item 
    print(f"The item at index {i} is {os}")
    
    
    
# =============================================================================
#     WHILE LOOPS
# =============================================================================
#anything to the right of the while loop evaluates

i = 5
while i <= 10:
    print(i)
    i += 1