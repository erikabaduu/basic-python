numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(numbers)
first_index=int(input('Pick a number '))
second_index=int(input('Pick another number'))
index1=numbers.index(first_index)
index2=numbers.index(second_index)
print('Index of first number:', index1)
print('Index of second number:',index2)
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
