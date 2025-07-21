#Ex1 Lambda GeekForGeeks - check if a value is in the list
# l=[2,3,5,8]
# n=-9

# Approach 1
# x = lambda n,l: True if n in l else False
# # if x(n,l):
# #     print('It\'s there')
# # else:
#     print('It\'s not there')

#Approach 2
# x = lambda l,n: l.count(n)
# if x(l,n) !=0:
#     print('It\'s there')
# else:
#     print('It\'s not there')

#Ex2 Lambda GeekForGeeks - Using lambda vs def

# def calculate_cube_root(x):
#     try:
#         return x**(1/3)
#     except:
#         return "Invalid Input"
    
# print(calculate_cube_root('am'))  

# n=125
# # x = lambda n: n**(1/3) 
# x = lambda n: n**(1/3) if isinstance (n,(int, float)) else 'Error - wrong data type'
# print(x(n))

#Ex3 Lambda GeekForGeeks - List iteration with lambda

# All numbers in the list squared
# l1 = [4, 2, 13, 21, 5] 
# l2 = [] 
# for n in l1:
#     x = lambda n: n**2
#     l2.append(x(n))
# print(l2)    

# All numbers in the list squared 
# l1 = [4, 2, 13, 21, 5] 
# l2 = list(map(lambda n: n**2,l1))
# print(l2)

# Odd numbers squared only
# l1 = [4, 2, 13, 21, 5] 
# # l_odd = list(filter(lambda n: n % 2 ==0,l1))
# # l_odd_squared =list(map(lambda n: n**2,l_odd))
# l_odd_squared = list(map(lambda n: n**2, list(filter(lambda n: n%2 == 0, l1))))
# print(l_odd_squared)
  
#Ex4 Lambda GeekForGeeks - Conditional statements with lambda function
# Even or odd number
# identifier = lambda n: f'Number {n} is even' if n%2 == 0 else f'Number {n} is odd'
# print(identifier(24))

# Bigger, smaller or equal
# result = lambda n,m: f'{n} is bigger than {m}' if n>m else (f'{n} is equal to {m}' if n==m else f'{m} is bigger than {n}') 
# print(result(-9,9))

#Ex5 Lambda GeekForGeeks - Smaller of two numbers with lambda function
# result = lambda m,n: min(m,n)
# result = lambda m,n: m if m < n else n
# print(result(20,5))

#Ex6 Lambda GeekForGeeks - Lambda with if but without else
#Only positive numbers squared
# result = lambda x: x**2 if(x > 0) else None
# print(result(-9))




#Lambda to display only the words starting with 'M'
# words = ['cat','elephant', 'mouse', 'koala','kangaroo','zebra']
# result = list(filter(lambda w: w.upper().startswith('M'), words))
# print(result)



# Lambda to show only ppl over 30
# ages = [
#     {'name': 'Evan', 'age': 25},
#     {'name': 'John', 'age': 30},
#     {'name': 'Jane', 'age': 27},
#     {'name': 'Jack', 'age': 32},
# ]

# over_30 = list(filter(lambda x:x['age']>=30, ages))
# print(over_30)



# Lambda to show only the says with the sales over 150; to calculate 20% sales tax
# sales = [
#     ('2022-06-01', 150),
#     ('2022-06-02', 100),
#     ('2022-06-03', 125),
#     ('2022-06-04', 75),
#     ('2022-06-05', 155),
#     ('2022-06-06', 180)
# ]

# # sales_over_150 = list(filter(lambda x: x[1]>150,sales))
# # print(sales_over_150)


# tax_sales = list(map(lambda x: x[1]*0.2,sales))
# print(tax_sales)



# Lambda to create a dictionary showing the length of each string in the tuple
# fruits = ('apple', 'banana', 'cherry','kiwi')
# fruit_word_length = tuple(map(lambda w:len(w),fruits))
# fruit_zip = list(map(lambda a,b: {a:b},fruits,fruit_word_length))
# print(fruit_zip)