# creating string and checking its length
letter = 'p'
print('letter')
print(len(letter))
greeting = 'Hello, world!'
print(greeting)
print(len(greeting))
sentence = "I hope i learn python from 30 days of python challenge"
print(sentence)
#multiline string
multiline_string = '''I am a student and excited to learn
coding and new things and love to explore more languages.
That is why iI strated 30 days of python.'''
#string concatenation
first_name = 'zumar'
last_name = 'ghazi'
space = ''
full_name = first_name + space + last_name
print(full_name)
print(len(first_name))
print(len(last_name))
print(len(first_name) < len(last_name))
print(len(full_name))
#escape sequence with example
print('I hope everyone is enjoying the python challenge.\nAre you ?')
print('days\tTopics\tExcercises')
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day4\t1\t35')
print('This is backslash symbol (\\)')
print('In every programming language it starts with \"Hello, world!\"')
#string formatting 
#strings only
first_name = 'Haneen'
last_name = 'yusuf'
language = 'python'
formatted_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formatted_string)
 #old strings and numbers
radius = 10
pi = 3.14
area = pi*radius**2
formatted_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)
python_libraries = ['Django', 'Flask', 'Numpy', 'Matplotlib', 'Pandas']
formatted_string = 'The following are python libraries:%s' %(python_libraries)
print(formatted_string)
#new style string formatting
first_name = 'Faris'
last_name = 'Ghazi'
language = 'python'
formatted_string = 'I am {} {}. I teach{}'.format(first_name, last_name, language)
print(formatted_string)
a = 4
b = 3
print('{}+{} ={}'.format(a, b, a+b))
print('{}-{} ={}'.format(a, b, a-b))
print('{}*{} ={}'.format(a, b, a*b))
print('{}/{} ={}'.format(a, b, a/b))
print('{}%{} ={}'.format(a, b, a%b))
print('{}//{} ={}'.format(a, b, a//b))
print('{}**{} ={}'.format(a, b, a**b))
#strings and numbers
radius = 10
pi = 3.14
area = pi*radius**2
formatted_string = 'The area of circle with a radius {} is {:.2f}.'.format(radius, area)
print(formatted_string) 
#string interpolation
a = 4
b = 3
print(f'{a} = {b} = {a+b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
#unpacking characters
language = 'python'
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
language = 'python'
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) -1
last_letter = language[last_index]
print(last_letter)
#slicing python strings
language = 'python'
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)
#string methods
challenge = 'thirty days of python'
print(challenge.capitalize())
challenge = 'thirty days of python'
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.count('th'))
challege = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))
#excercise questions
word1 = 'Thirty'
word2 = 'days'
word3 = 'of'
word4 = 'python'
result = word1 + ' ' + word2 + ' ' + word3 +' ' + word4
print(result)
word1 = 'Coding'
word2 = 'For'
word3 = 'All'
total = word1 + ' ' + word2 + ' ' + word3
print(total)
company  = 'Coding For All'
print(company)
variable = 'company' 
print(variable)
company = 'Coding For All'
print(company)
print(len(company))
challenge = 'thirty days of python'
print(challenge.upper())
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.lower())
challenge = 'thirty days of python'
print(challenge.capitalize())
print(challenge.title())
print(challenge.swapcase())
company = 'Coding For All'
print(company[0:6])
challenge = 'coding for all'
print(challenge.index('coding'))
company = 'coding for all'
print(challenge.replace('all', 'python'))
challenge = 'Python for Everyone'
print(challenge.replace('Everyone', 'All'))
challenge = 'coding for all'
print(challenge.split())
challenge = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(challenge.split(', '))
text = 'Coding For All'
print(text[0])
text = 'Coding For All'
print(text[13])
character = 'Coding For All'
print(character[10])
text = 'python for everyone'
print("".join(word[0] for word in text.split()))
text = 'coding for all'
print("".join(word[0] for word in text.split()))
text = "coding for all"
text = "Coding For All"
print(text.index("C"))
text = 'Coding For All'
print(text.index("F"))
text ="Coding For All People"
print(text.rfind(" l "))
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because'))
sentence ='You cannot end a sentence with because because because is a conjunction'
print(sentence[35:58])
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence[35:58])
text ='Coding For All'
print(text.index('Coding'))
text = '   Coding For All      ' 
print(text.strip())
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))
print('I am enjoying this challenge. \n I just wonder what is next.')
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

