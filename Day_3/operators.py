print('adddition:', 1+2)
print('Subraction:', 2-3)
print('Multiplication:', 3*2)
print('Division:', 4/2)
print('Modulus:', 4%2)
print('Exponentation:', 4**2)
print('Division without the remainder:', 7//2)
print('Division without the remainder:', 7//3)

print('Floating point numbers, PI', 3.14)
print('Floating point number, gravity', 9.81)

print('Complex number:', 1+1j)
print('Complex number:', 1+2j)
print('Multiplying complex numbers:', (1+1j)* (1-1j))

radius = 10
area_of_circle = 3.14*radius**2
print('area_of_circle:', area_of_circle)

length = 10
width = 20
area_of_rectangle = length*width
print('area_of_rectangle:', area_of_rectangle)


mass = 75
gravity = 9.81
weight = mass*gravity
print(weight, 'N')

mass = 75
volume = 0.075
density = mass/volume
print(density, 'kg/m^3')

print(3>2)
print(5<10)
print(3>=2)
print(2<3)
print(2<=3)
print(3==2)
print(3!=2)
print(len('mango')==len('avacado'))
print(len('mango')!=len('banana'))
print(len('mango')<len('avacado'))
print(len('avacado')>len('mango'))

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)


age = 20
print(age)

height = "5'6"
print(height)

complex = 1+4j
print(complex)

base = 20
height = 10
area_of_triangle = 0.5*height*base
print('area_of_triangle:', area_of_triangle)

side_a = 5
side_b = 4
side_c = 3
perimeter_of_triangle = side_a+ side_b+ side_c
print('perimeter_of_triangle:', perimeter_of_triangle)
length = 10
width = 20
area_of_rectangle = length*width
print('area_of_rectangle:', area_of_rectangle)
perimeter_of_rectangle = 2*(length+width)
print('perimeter_of_rectangle:', perimeter_of_rectangle) 
radius = 10
area_of_circle = 3.14*10*10
print('area_of_circle:', area_of_circle)
circumference_of_circle = 2*3.14*10
print('circumference_of_circle:', circumference_of_circle)
x = 5
y = 2*x - 2
slope = 2
x_intercept = 2/2
y_intercept = -2
print("slope:", slope)

x1= 2
y1= 2

x2=6
y2=10
slope = (y2-y1)/(x2-x1)
distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
print("slope:", slope)
print("Euclidian distance:", distance)

x= -3
y = x**2 + 6*x + 9
print("x=", x)
print("y=", y)

x = 'python'
y = 'dragon'
print(len('python'))
print(len('dragon'))
print(len('python') == len('dragon'))

print('on' in 'python' and 'on' in 'dragon')

sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)
print('on' not in 'python' and 'on'not in 'dargon')

length = len('python')
print(length)

length = float(len("python"))
print(length)

length = str(float(len("python")))
print(length)

number = 6
print(number % 2==0)
print(7//3 == int(2.7))
print(type('10') == type(10))
print(type('9.8') == type(10))


hours = float(input("enter hours:"))
rate = float(input("enter rate per hour:"))
pay = hours*rate
print("your weekly earning is", pay)

years = int(input("Enter number of years you have lived: "))

seconds = years * 365 * 24 * 60 * 60

print("You have lived for", seconds, "seconds.")