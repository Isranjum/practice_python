#list with intial valuess
fruits = ['banana', 'mango', 'apple', 'pineapple']
vegetables = ['onion', 'potato', 'ginger', 'carrot']
Animal_products = ['milk', 'paneer', 'cheese', 'tofu']
web_techs = ['HTMl', 'python', 'Js', 'Css']
countries = ['Finland', 'AMerica', 'turkey', 'sri lanka']
#print list and its length
print('Fruits:', fruits)
print('Number o f fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal_products:', Animal_products)
print('Number of Animal_products:', len(Animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('countries:', countries)
print('NUmber of countries:', len(countries))
fruits =['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruit = fruits[3]
print(last_fruit)

last_index = len(fruits)-1
last_fruit = fruits[last_index]
fruits = ['banana', 'mango', 'pineapple', 'oranges']
first_fruit = fruits[-4]
second_fruit = fruits[-2]
last_fruit = fruits[-1]
print(first_fruit)
print(second_fruit)
print(last_fruit)
#unpacking list items
lst = ['zumar', 'faris', 'saadi', 'haneen']
first_name, second_name, third_name, *rest = lst
print(first_name)
print(second_name)
print(third_name)
print(rest)
#first example 
names = ['Imama', 'Zumar', 'maleeha', 'Aleezah']
first_name, second_name, *rest = names
print(first_name)
print(second_name)
print(rest)
#second example about unpacking list
first, second, third, *rest, tenth = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first)
print(second)
print(third)
print(rest)
print(tenth)
#third example
countries = ['Germany', 'Turkey', 'Finland', 'Denmark', 'Norway', 'Sweden']
gr, tu, fi, sw, *scandic, es = countries
print(gr)
print(tu)
print(fi)
print(sw)
print(scandic)
print(es)
fruits = ['banana', 'orange', 'apple', 'mango']
all_fruits = fruits[0:4]
all_fruits = fruits[0:]
orange_and_mango = fruits[1:3]
oranges_mango_lemon = fruits[1:]
oranges_and_lemon = fruits[::2]
#modifying list
fruits=  ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avacado'
print(fruits)
fruits[1] = 'Daragon fruit'
print(fruits)
last_index = len(fruits)-1
fruits[last_index] = 'lime'
print(fruits)
#in operator
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  
does_exist = 'lime' in fruits
print(does_exist) 
#adding item to list
fruits =  ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)
fruits.append('pineapple')
print(fruits)
#inserting item to list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(3, 'papaya')
print(fruits)
fruits.insert(2, 'lime')
print(fruits)
#removing items using remove()
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)
fruits.remove('lemon')
print(fruits)
#removing items using pop()
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop(3)
print(fruits)
fruits.pop(0)
print(fruits)
#removing items usind del
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)
del fruits[1:3]
print(fruits)
#clearing list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)
#cpying a list
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)
#joinning list
positive_numbers = [1, 2, 3, 4, 5]
zero =[0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]
negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
#excersise questions
empty_list =[]
print(empty_list)
list = ['zumar', 'faris', 'hannen', 'saadi', 'zartasha']
print(list)
print(len(list))
fruits = ['banana', 'oranges', 'apple', 'mango', 'lime']
first_item, middle_item, last_item, *rest= fruits
print(first_item) 
print(middle_item)
print(last_item)
list = ['Arshiya', 41, 5.2, 'married', 'india' ]
print(list)
it_companies =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
first_it_company, middle_it_company, last_it_company, *rest = it_companies
print(first_it_company)
print( middle_it_company)
print( last_it_company)
print(it_companies)
print(len(it_companies))
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
company[3] = 'wipro'
print(company)
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
company.append('samsung')
print(company)
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
company.insert(4, 'samsung')
print(company)
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
company.append('samsung')
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
company[2] = company[2].upper()
print(company)
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
result = '#'.join(company)
print(result)
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
does_exits = 'Google' in company
print(does_exits)
list = ['zumar', 'faris', 'hannen', 'saadi']
list.sort()
print(list)
list = ['zumar', 'faris', 'hannen', 'saadi']
list.reverse()
print(list)
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
company = company[:3]
print(company)
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
company = company[-3:]
print(company)
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
print(company[3])
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
company.remove('Facebook')
print(company)
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
company.remove('IBM')
print(company)
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
company.remove('Amazon')
print(company)
company =['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', ' Amazon']
company.clear()
print(company)
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
Full_stack = front_end + back_end
print(Full_stack)
Full_stack.insert(5, 'python')
Full_stack.insert(6, 'SQL')
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))
ages.append(min(ages))
ages.append(max(ages))
print(ages)
median = (ages[5] + ages[6]) /2
print(median)
length = len(countries)
if length % 2 == 0:
    print(countries[length//2-1])
    print(countries[length//2])
else:
    print(countries[length//2])





