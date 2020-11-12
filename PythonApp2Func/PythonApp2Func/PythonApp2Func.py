x = 365
y = 7
# this is a comment

print(x % y) # find the remainder
# print (x // y)
# another comment

def print_with_exclamation(word):
   print(word + "!")
    
print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")

def print_sum_twice(x, y):
   print(x + y)
   print(x + y)

print_sum_twice(5, 8)

def function(variable):
   variable += 1
   print(variable)

function(7)

def max(x, y):
    if x >=y:
        return x
    else:
        return y
        
print(max(4, 7))
z = max(8, 5)
print(z)

def add_numbers(x, y):
  total = x + y
  return total
  print("This won't be printed")
print(add_numbers(4, 5))

def shout(word):
  """
  Print a word with an
  exclamation mark following it.
  """
  print(word + "!")    
shout("spam")

def multiply(x, y):
   return x * y
a = 4
b = 7
operation = multiply
print(operation(a, b))
print(multiply(a, b))

def add(x, y):
  return x + y
def do_twice(func, x, y):
  return func(func(x, y), func(x, y))
a = 5
b = 10
print(do_twice(add, a, b))

 
def square(x):
  return x * x
def test(func, x):
  print(func(x))
test(square, 42)

import random
for i in range(5):
   value = random.randint(1, 6)
   print(value)

#import math
#print (math.sqrt(num))
#from math import *       #no confused variable

from math import pi, sqrt
num = 10
print (sqrt(num))
print(pi)

#import some_module     # error

import math as m
print(math.sqrt(25))