
print("Hello World")
print(2 + 3)
print(2 - 8)
print(2*3+3*(8-5))
print(10/2)
print( 0.42 )
print( 6 * 7.0 )
print( 4 + 1.65 )
print((2**3)**2)
print(2**3**2)
print(9**(1/2))
print(2**(-1))
print(20//6)
print(20%6)
print(8.3//4.1)
print(1.25%0.5)

print("Pyton is fun")
print('Always look on the bright side of life')
print('Bob\'s mother: my son isn\'t an angel.')
print('Bob"s mother: my son isn"t an angel.')
print("Bob's mother: my son isn't an angel.")
print('One \nTwo \nThree') 
print("""This
is a
multiline
text""") 

print('''This is 
multiline 
text
too''')
print('Some' + ' text')
print('2' + '2')
print('Some text * 3 ' * 3)
print(2 * '2 * text usually stay first ')

this_is_a_normal_name_of_variable = 'I am a value of this variable'
print(this_is_a_normal_name_of_variable)
print('Python is a case sensitive programming language. Thus, Lastname and lastname are two different variable names in Python.')
x = 7
print(x)
print(x + 3)
print(x)
x = 123.456
print(x)
x = "This is a string"
print(x + "!")
print('However, it is not good practice. To avoid mistakes, try to avoid overwriting the same variable with different data types.')
x = input('Enter something please: ')
print('You enter ' + x)
x = int(input('please enter your age: '))
print('Are you ' + str(x) + ' years old?')
x = 8
y = 3
x += y
print(x)
x -= y
print(x)
x *= y
print(x)
x /= y
print(x)
x %= y
print(x)
x **= y
print(x)
x //= y
print(x)
x = 'i am string '
print(x)
x *= 3
print(x)
y = 'ok'
print(y)
x += y
print(x)

x = True
print(x)
print(2 == 3)
print("hello" == "hello")
print( 1 != 1 )
print("eleven" != "seven")
print(2 != 10)
print( 7 > 5 )
print( 10 < 10.0 )
print(7 <= 8)
print(9 >= 9.0)
print("Annie" > "Andy")

if 10 > 5 :
    print('10 is greate than 5')
num = 12
if num > 5:
   print("Bigger than 5")
   if num <=47:
      print("Between 5 and 47")
x = 4
if x == 5:
   print("Yes")
else:
   print("No")
num = 3
if num == 1:
  print("One")
else: 
  if num == 2:
    print("Two")
  else: 
    if num == 3: 
      print("Three")
    else: 
      print("Something else")

print( 1 == 1 and 2 == 2 )
print( 1 == 1 and 2 == 3 )
print( 1 != 1 and 2 == 2 )
print( 2 < 1 and 3 >  6 )

print( 1 == 1 or 2 == 2 )
print( 1 == 1 or 2 == 3 )
print( 1 != 1 or 2 == 2 )
print( 2 < 1 or 3 >  6 )

print(not 1 == 1)
print(not 1 > 7)

print( False == False or True )
print( False == (False or True) )
print( (False == False) or True )

grade = 88
if (grade >= 70 and grade <=100):
    print("Passed!") 

x = 4
y = 2
if not 1 + 1 == y or x == 4 and 7 == 8:
  print("Yes")
elif x > y:
  print("No")

words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2]) 

empty_list = []
print(empty_list)
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])
m = [
    [1, 2, 3],
    [4, 5, 6]
    ]    
print(m[1][2])  

string = "Hello world!"
print(string[6])

nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)

nums = [1, 2, 3]
nums.append(4)
print(nums)

nums = [1, 3, 5, 2, 4]
print(len(nums))

words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)

letters = ['p', 'q', 'r', 's', 'p', 'u']
print(letters)
print(letters.index('r'))
print(letters.index('p'))
print(letters.count('p'))
print(len(letters))
print(max(letters))
print(min(letters))
letters.remove('p')
print(letters)
letters.reverse()
print(letters)

i = 1
while i <=5:
   print(i)
   i = i + 1

print("Finished!")

x = 1
while x < 10:
  if x%2 == 0:
    print(str(x) + " is even")
  else:
    print(str(x) + " is odd")

  x += 1 

  i = 0
while True:
  print(i)
  i = i + 1
  if i >= 5:
    print("Breaking")
    break

print("Finished")

i = 1
while i<=5:
    print(i)
    i+=1
    if i==3:
      print("Skipping 3")
      continue

words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")

string = "testing for loops"
count = 0

for x in string:
  if(x == 't'):
    count += 1

print(count) 

numbers = list(range(10))
print(numbers)

numbers = list(range(3, 8))
print(numbers)

print(range(20) == range(0, 20))

numbers = list(range(5, 20, 2))
print(numbers)

numbers = list(range(20, 5, -2))
print(numbers)

for i in range(5):
  print("hello!")

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])