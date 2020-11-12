num1 = 7
num2 = 0
#print(num1/num2)

try:
   num1 = 7
   num2 = 0
   print (num1 / num2)
   print("Done calculation")
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")

try:
   variable = 10
   print(variable + "hello")
   print(variable / 2)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")

try:
   word = "spam"
   print(word / 0)
except:
   print("I cath all exceptions. An error occurred")

try:
   print("Hello")
   print(1 / 0)
except ZeroDivisionError:
   print("Divided by zero")
finally:
   print("This code will run no matter what")

try:
   print(1)
   print(10 / 0)
except ZeroDivisionError:
   print('#print(unknown_var) # here there is var not declared at all and occure new exception')
finally:
   print("This is executed last")

print(1)
#raise ValueError
print(2)

name = "123"
#raise NameError("Invalid name!")

try:
   num = 5 / 0
except:
   print("An error occurred")
   #raise

print(1)
assert 2 + 2 == 4
print(2)
#assert 1 + 1 == 3
print(3)

print(0)
assert "h" != "w"
print (1)
#assert False
print(2)
assert True
print(3)

temp = -10
#assert (temp >= 0), "Colder than absolute zero!"

 
def my_func(x): 
    assert  x > 0, "Error!"
    print(x)
#my_func(-1)

myfile = open("filename.txt")#if file is in current directory
myfile.close()
# rewrite mode
myfile = open("filename.txt", "w") # if file don't exist it will create
myfile.close()
# read mode
myfile = open("filename.txt", "r")
myfile.close()
myfile = open("filename.txt") # by default read
myfile.close()
# read and write mode
myfile = open("filename.txt", "r+")
# append mode
myfile = open("filename.txt", "a")
myfile.close()
# binary write mode
myfile = open("filename.txt", "wb")
myfile.close()

file = open("filename.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("filename.txt", "r")
print(file.read())
file.close()

file = open("filename.txt", "r")
print("Reading initial contents")
print(file.read())
print("Finished")
file.close()

file = open("filename.txt", "w")
file.write("Some new text")
file.close()

file = open("filename.txt", "r")
print("Reading new contents")
print(file.read())
print("Finished")
file.close()

file = open('filename.txt', 'w')
file.close()
file = open('filename.txt', 'r')
print('don\'t open file in "w" mode and close() them because you will get:')
print(file.read())
print("Finished")
file.close()

msg = "Hello world!"
file = open("filename.txt", "w")
amount_written = file.write(msg)
print(msg + ' amount_written: ' + str(amount_written) + ' == len(msg): ' + str(len(msg)))
file.close()

msg = str(list(range(3,8)))
file = open("filename.txt", "w")
amount_written = file.write(msg)
print(msg + ' amount_written: ' + str(amount_written) + ' == len(msg): ' + str(len(msg)))
file.close()

file = open('filename.txt', 'a')
print('amount added text: ' + str(file.write('I am a continue of line in your file')))
print('amount added text: ' + str(file.write('''
I am a new line in your file''')))
print('amount added text: ' + str(file.write('''
I am a new line in your file yet
I am still new line in your file
I am and line in your file
''')))
file.close()

file = open("filename.txt", "r")
cont = file.read()
print(cont)
file.close()

file = open("filename.txt", "r")
print(file.read(16))
print(file.read(4))
print(file.read(4))
print(file.read()) # print evrething that leave yet
file.close()

file = open("filename.txt", "r")
print(file.read()) # print evrething in file
print(file.read(-1)) # print evrething in file
file.close()

file = open("filename.txt", "r")
for i in range(21):
  print(file.read(4))
file.close()

file = open("filename.txt", "r")
print("First reading:")
print(file.read())
print("Re-reading:")
print(file.read())
print("Finished")
file.close()

file = open("filename.txt", "r")
print('len of your file: '+ str(len(file.read())) + "\n")
file.close()

file = open("filename.txt", "r")
print(file.readlines())
file.close()

file = open("filename.txt", "r")
for line in file:
    print(line)
file.close() 

try:
   f = open("filename.txt")
   print(f.read())
finally:
   f.close()

with open("filename.txt") as f:
   print(f.read())


try: 
    with open("test.txt") as f:
        print(f.read()) 
except:
    print("Error")