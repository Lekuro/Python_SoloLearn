print(None)
print(None == None)

def some_func():
  print("Hi!")
var = some_func()
print(var)

foo = print()
if foo == None:
   print(1)
else:
   print(2)

ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

primary = {
  "red": [255, 0, 0], 
  "green": [0, 255, 0], 
  "blue": [0, 0, 255], 
}
print(primary["red"])
#print(primary["yellow"])

test = { }
#print(test[0])

#bad_dict = { [1, 2, 3]: "one two three", }

squares = {1: 1, 2: 4, 3: "error", 4: 16,}
squares[8] = 64
squares[3] = 9
print(squares)

nums = {
  1: "one",
  2: "two",
  3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))
print(pairs.get(12345, -1))

#Tuples
words = ("spam", "eggs", "sausages",)
print(words[0])
#words[1] = "cheese"#error


# list
list = ["one", "two"]

# dictionary 
dict = {1:"one", 2:"two"}
 
# tuple 
tp = ("one", "two")
tpl = () # empty tuple
print(tpl)
my_tuple = "one", "two", "three"
print(my_tuple)
my_tuple = 1, 2, 3
print(my_tuple)
my_tuple = 1, "two", ["three",1],{'w':3}
print(my_tuple)

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(num[::-1])
print(num[::2])
print(num[::-2])
print(num[::3])
print(num[::-3])
print(num[::4])
print(num[::-4])
print(num[::5])
print(num[::-5])
print(num[::6])
print(num[::-6])
print(num[::9])
print(num[::-9])
print(num[::10])
print(num[::-10])
print(num[::100])
print(num[::-100])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])#[1, 4, 9, 16, 25, 36, 49, 64]
print(squares[-1:1])#[]
print(squares[:-1])#[]
print(squares[-1:-3])#[]
print(squares[-3:-1])#[49,64]

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[7:5:-1])

# a list comprehension
cubes = [i**3 for i in range(8)]
print(cubes)
even = [i*2 for i in range(10)]
print(even)
square_even=[i**2 for i in range(10) if i**2 % 2 == 0]
print(square_even)
multiples_3 = [i for i in range(20) if i % 3 == 0]
print(multiples_3)
a = [x*10 for x in range(5, 9)]
print(a)

# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)
print("{0}{1}{0}".format("catch", "cat"))
a = "{x}, {y}".format(x=5, y=12)
print(a)
msg="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(msg)

# string functin
print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

# numeric function
print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

a=min([sum([11, 22]), max(abs(-30), 2)])
print(a)

# list ffunction
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

for v in enumerate(nums):
   print(v)

# text analyse
with open('filename.txt') as f:
   text = f.read()
print(text)
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count
print('print amount all "r" in file: ' + str(count_char(text, "r")))

for char in "abcdefghijklmnopqrstuvwxyz":
  perc = 100 * count_char(text, char) / len(text)
  print('char "' + char + '" is in text ' + str(count_char(text, char)) + ' times. And percent: ')
  print("{0} - {1}%".format(char, round(perc, 2)))

nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))