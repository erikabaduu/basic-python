#a= int(input('Enter any number '))
#b= int(input('Enter another number '))
#print('Sum:', a+b) 
'''
a= int(input('Enter any number '))
b= int(input('Enter a second number '))
c= input('addition or multiplication ')
addition=a+b 
multiplication=a*b 
if c== 'addition':
    print('Sum:', addition)
elif c== 'multiplication':
    print('Product:', multiplication)
'''
'''
#List 
fruits=['apple','mango','pineapple']
print(fruits) 
print(fruits[1])
fruits_appending=fruits.append('coconut')
print(fruits)
fruits_inserting=fruits.insert(2,'grapes')
print(fruits)
fruits_remove=fruits.remove('mango')
print(fruits)
fruits_pop=fruits.pop(0)
print(fruits)

index1=numbers[first_index]
index1=numbers[first_index]
'''

numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(numbers)
first_index=int(input('Pick an index '))
second_index=int(input('Pick another index '))
index1=numbers[first_index]
index2=numbers[second_index]
print('first number:', index1)
print('second number:',index2)
user= input('What operation would you like to use? Addition, Subtraction, Multiplication or division ')
addition=index1 + index2 
subtraction=index1-index2
multiplication=index1*index2
division=index1/index2 
if user== 'addition':
    print('Sum',addition)
elif user== 'subtraction':
    print('Difference',subtraction)
elif user== 'multiplication':
    print('Product', multiplication)
elif user== 'division':
    print('Division', division)
