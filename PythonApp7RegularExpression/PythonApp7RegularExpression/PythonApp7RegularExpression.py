import re
# re.match function can be used to determine whether it matches at the beginning of a string
pattern = r"spam"
if re.match(pattern, "spamspamspam"):
   print("Match")
else:
   print("No match")

if re.match(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")

# re.search finds a match of a pattern anywhere in the string
if re.search(pattern, "eggspamsausagespam"):
   print(str(re.search(pattern, "eggspamsausagespam")))
else:
   print("No match")

match = re.search(pattern, "eggspamsausage")
if match:
   print(match.group())
   print(match.start())
   print(match.end())
   print(match.span())

# re.findall returns a list of all substrings that match a pattern    
print(re.findall(pattern, "eggspamsausagespam"))

# re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list
print(list(re.finditer(pattern, "eggspamsausagespam")))

# re.sub(pattern, repl, string, count=0)
# sub replaces all (or count) occurrences of the pattern in string with repl
# This method returns the modified string
string = "My name is David. Hi David."
print(string)
pattern = r"David"
newstr = re.sub(pattern, "Amy", string, 1)
print(newstr)
newstr = re.sub(pattern, "Amy", string) # all
print(newstr)

# -----------Metacharacters----------------------------

# . (dot) matches any character, other than a new line but only one
pattern = r"gr.y"

if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "blue"):
   print("Match 3")

# ^ and $ match the start and end of a string, respectively
pattern = r"^gr.y$" # means that the string should start with gr, 
# then follow with any character, except a newline, and end with y
 
if re.match(pattern, "grey"):
   print("Match 1")

if re.match(pattern, "gray"):
   print("Match 2")

if re.match(pattern, "stingray"):
   print("Match 3")

# Character Classes------------return only one element
# A character class is created by putting the characters it matches inside square brackets
pattern = r"[aeiou]" # match only one of a specific set of characters

if re.search(pattern, "grey"):
   print(str(re.search(pattern, "grey")))

if re.search(pattern, "qwertyuiop"):
   print(str(re.search(pattern, "qwertyuiop")))

if re.search(pattern, "rhythm myths"):
   print(str(re.search(pattern, "rhythm myths")))

pat = r'[etm][gey]' # Any letter out of "abc", then any out of "def" must be next to

if re.search(pat, "grey"):
   print(str(re.search(pat, "grey")))

if re.search(pat, "qwertyuiop"):
   print(str(re.search(pat, "qwertyuiop")))

if re.search(pat, "rhythm myths"):
    print(str(re.search(pat, "rhythm myths")))

print('''
Character classes can also match ranges of characters:
The class [a-z] matches any lowercase alphabetic character.
The class [G-P] matches any uppercase character from G to P.
The class [0-9] matches any digit.
Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case.
''')
pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
   print(str(re.search(pattern, "LS8")))

if re.search(pattern, "E3"):
   print("Match 2")

if re.search(pattern, "1ab"):
   print("Match 3")

# ^ at the start of a character class to invert it.
# This causes it to match any character other than the ones included.
pattern = r"[^A-Z]" # not uppercase letter return only one symbol

if re.search(pattern, "this is all quiet"):
   print(str(re.search(pattern, "this is all quiet")))

if re.search(pattern, "AbCdEfG123"):
   print(str(re.search(pattern, "AbCdEfG123")))

if re.search(pattern, "THISISALLSHOUTING"):
   print("Match 3")

# -----------Metacharacters-----------------
# * means "zero or more repetitions of the previous thing"
# The "previous thing" can be a single character, a class, or a group of characters in parentheses
pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
   print(str(re.match(pattern, "egg")))

if re.match(pattern, "eggspamspamegg"):
   print(str(re.match(pattern, "eggspamspamegg")))

if re.match(pattern, "spam"):
   print("Match 3")

# + is very similar to *, except it means "one or more repetitions"
pattern = r"g+"

if re.match(pattern, "g"):
   print("Match 1")

if re.match(pattern, "gggggggggggggg"):
   print("Match 2")

if re.match(pattern, "abc"):
   print("Match 3")

# ? means "zero or one repetitions"
pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
   print("Match 1")

if re.match(pattern, "icecream"):
   print("Match 2")

if re.match(pattern, "sausages"):
   print("Match 3")

if re.match(pattern, "ice--ice"):
   print("Match 4")

# | means "or", so red|blue matches either "red" or "blue"
pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
   print ("Match 1")

match = re.match(pattern, "grey")
if match:
   print ("Match 2")    

match = re.match(pattern, "griy")
if match:
    print ("Match 3")

# Curly braces can be used to represent the number of repetitions between two numbers.
# The regex {x,y} means "between x and y repetitions of something".
# Hence {0,1} is the same thing as ?
# If the first number is missing, it is taken to be zero. 
# If the second number is missing, it is taken to be infinity.
pattern = r"9{1,3}$"

if re.match(pattern, "9"):
   print("Match 1")

if re.match(pattern, "999"):
   print("Match 2")

if re.match(pattern, "9999"):
   print("Match 3")

patern = r"([^aeiou][aeiou][^aeiou])+" # One or more repetitions of a non-vowel, a vowel and a non-vowel

# group
pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(2))
   print(match.groups())

pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())

# ------------Special Sequences-----------
# special sequences are written as a backslash followed by another character
# One useful special sequence is a backslash and a number between 1 and 99

pattern = r"(.+) \1"
# Note, that "(.+) \1" is not the same as "(.+) (.+)", 
# because \1 refers to the first group's subexpression, 
# which is the matched expression itself, and not the regex pattern.
match = re.match(pattern, "word word word ")
if match:
   print (str(match))

match = re.match(pattern, "?! ?!")
if match:
   print (str(match))    

match = re.match(pattern, "abc cde")
if match:
   print ("Match 3")

#  \d, \s, \w These match digits, whitespace, and word characters respectively but only one
# In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_]
# \D, \S, and \W - mean the opposite to the lower-case versions
# For instance, \D matches anything that isn't a digit

pattern = r"(\D+\d)" # (\D+\d) matches one or more non-digits followed by a digit.

match = re.match(pattern, "Hi 999!")

if match:
   print(str(match))

match = re.match(pattern, "1, 23, 456!")
if match:
   print("Match 2")

match = re.match(pattern, " ! $?")
if match:
    print("Match 3")

# \A and \Z match the beginning and end of a string, respectively.
# \b matches the empty string between \w and \W characters, 
# or \w characters and the beginning or end of the string. 
# Informally, it represents the boundary between words
pattern = r"\b(cat)\b" # basically matches the word "cat" surrounded by word boundaries
match = re.search(pattern, "The cat sat!")
if match:
   print ("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
   print ("Match 2")

match = re.search(pattern, "We scattered.")
if match:
   print ("Match 3")

# email addres
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
   print(match.group())