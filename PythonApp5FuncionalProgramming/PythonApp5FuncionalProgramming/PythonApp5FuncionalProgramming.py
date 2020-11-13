def apply_twice(func, arg):
   return func(func(arg))
def add_five(x):
   return x + 5
print(apply_twice(add_five, 10))

# Pure function:
def pure_function(x, y):
  temp = x + 2*y
  return round(temp / (2*x + y),3)
print(pure_function(3,8))
def func(x):
  y = x**2
  z = x + y
  return z

# Impure function:
some_list = []
def impure(arg):
  some_list.append(arg)
impure(3)
print(some_list)

# lambda is anonymous
def my_func(f, arg):
  return f(arg)
print(my_func(lambda x: 2*x*x, 5))

#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

#Lambda functions can be assigned to variables, and used like normal functions
double = lambda x: x * 2
print(double(7))

triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))

# function map takes a function and an iterable as arguments, 
# #and returns a new iterable with the function applied to each argument.
def add_five(x):
  return x + 5
nums = [11, 22, 33, 44, 55]
num_tup =(11,22,33,44,55)
result_list = list(map(add_five, nums))
result_tuple = tuple(map(add_five, nums))
res_list = list(map(add_five, num_tup))
res_tuple = tuple(map(add_five, num_tup))
print(nums)
print(result_list)
print(result_tuple)
print(num_tup)
print(res_list)
print(res_tuple)
# with lambda function
result = list(map(lambda x: x+5, nums))
print(result)

#function filter filters an iterable by removing items that don't match a predicate (a function that returns a Boolean)
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

nums = [1, 2, 5, 8, 3, 0, 7]
res = list(filter(lambda x: x<5, nums))
print(res)

# Generators are a type of iterable, like lists or tuples 
# can be created using functions and the yield statement.
def countdown():
  i=5
  while i > 0:
    yield i
    i -= 1    
for i in countdown():
  print(i)
# yield one item at a time, generators don't have the memory restrictions of lists it is infinite!
# generators allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.
 
def numbers(x):
  for i in range(x):
    if i % 2 == 0:
      yield i
print(list(numbers(11)))

def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    yield word
print(list(make_word()))

# Decorators provide a way to modify functions using other functions.
# Decorators are functions that modify other functions
def decor(func):
  def wrap():
    print("============")
    func()
    print("============")
  return wrap

def print_text():
  print("Hello world!")

decorated = decor(print_text)
decorated()
print_text = decor(print_text)
print_text()
decorated()

@decor
def print_again():
  print("Hello world!")
print_again()

# Recursion is self-reference - functions calling themselves
# The base case acts as the exit condition of the recursion.
# The base doesn't involve any further calls to that function
def factorial(x):
  if x == 1:
    return 1
  else: 
    return x * factorial(x-1)    
print(factorial(5))
def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))

# indirect recursion
def is_even(x):
  if x == 0:
    return True
  else:
    return is_odd(x-1)
def is_odd(x):
  return not is_even(x)
print(is_odd(3))
print(is_even(3))

# set data stracture
# They are unordered, which means that they can't be indexed.
# They cannot contain duplicate elements.
empty_set = set() # {} empty dictionary
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])
print(word_set)
print(3 in num_set)
print("spam" not in word_set)
nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
print(len(nums))
nums.add(-7)
nums.remove(3)
print(nums)

first = {1, 2, 3, 4, 5, 6}
print(first)
second = {4, 5, 6, 7, 8, 9}
print(second)
print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

#
from itertools import count

for i in count(3):
  print(i)
  if i >=11:
    break

from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))

from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters))) 