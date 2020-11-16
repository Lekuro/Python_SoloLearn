import this
print(this)

# --------Function Arguments--------------

print('--------------Function Arguments----------------------')
def function(named_arg, *args):
   print(named_arg)
   print(args)

function(1, 2, 3, 4, 5)

def function(x, y, food="spam"): # default value
   print(food)

function(1, 2)
function(3, 4, "egg")

# **kwargs allows you to handle named arguments that you have not defined in advance
def my_func(x, y=7, *args, **kwargs):
   print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

# --------Tuple Unpacking------------
numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)

a, b = b, a = (3, 8)
print(a)
print(b)

x, y = [1, 2]
x, y = y, x

a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

a, b, c, d, *e, f, g = range(20)
print(len(e))

# -----Ternary Operator-----
a = 7
b = 1 if a >= 5 else 42
print(b)

status  = 1
msg = "Logout" if status == 1 else "Login"

if bool(None):
    print('why?')
else:
    print(bool(None))

#       ----------More on else Statements------------
print(' ----------More on else Statements------------ ')
for i in range(10):
   if i == 999:
      break
else:
   print("Unbroken 1")

for i in range(10):
   if i == 5:
      break
else: 
   print("Unbroken 2")

try:
   print(1)
except ZeroDivisionError:
   print(2)
else:
   print(3)

try:
   print(1/0)
except ZeroDivisionError:
   print(4)
else:
   print(5)

# -----------------__main__-------------------
print('''
  -----------------__main__-------------------
''')
import module1sololearn
module1sololearn.function()

if __name__=="__main__":
   print("This is a script")

for i in range(10):
  try: 
    if 10 / i == 2.0:
      break
  except ZeroDivisionError:
    print(1)
  else:
    print(2)