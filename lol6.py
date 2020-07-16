# num = [1, 2, 3, 4, 5]


# num = list ((1, 2, 3, 4, 5, 6, 7))

# num = [5] * 6

# num = [1, 2, 3]
# num2 = [4, 5, 6]
# print (num + num2)


# num = [1, 2, 3, 4, 6]
# print (num [-1])
# print (num[1:3])

# num.append ("Makers")
# print (num)
# num.append ([1,2,3,4])
# print(num)
# num.insert(3m "Inserted object")

# num = range(10)
# print(num)

# num = list (range(5, 16, 2))


# list_ = [1, 2, 0.6, True, "Makers", "bishkek", [3, 4, 5], "ne nujen"]
# # list_.pop()
# # print(list_)
# list_.extend([1,2,3,4])
# list_.reverse()
# print (list_)

# print(num)
# print(type(num))
# print(dir(num))

#"----------------------------------------------------------------------------------------------------------------

# companies = ['Makers', 'Beeline', 'O', 'Megacom']
# item = 'Telecom'
# if item in companies:
#     companies.remove('item')
# in / not in / is / is not.

# users = ['Tom', 'Bob', 'Alice', 'Tom', 'Tom']
# users_count = users.count(Tom)
# print(users_count)

# users = ['Tom', 'Bob', 'Alice', 'Tom', 'Tom']
# users.sort()
# print(users)

# numbers = (1, 2, 3, 4, 5)
# print(min(numbers))
# print(max(numbers))


# users1 = ['Tom', 'BOb', 'Alice']
# users2 = users1
# users2.append('Sam')
# print(users1)
# print(users2)

# import copy 

# users1 = ['Tom', 'Bob', 'Alice']
# users2 = copy.deepcopy(users1)
# users2.append('Aybek')

#  pirnt(users1)
#  print(users2)
 
#  num1 = [1, 2, 3]
#  num2 = [4, 5, 6]
#  num3 = num1 + num2
#  print(num3)
 
# users = [
#     ['Tom' 29]
#     ['Alise' 33]
#     ['Bob', 25]
# ]
# print(users[1][1]) к возрасту алисы(33)

# users = ['Tom', 'Bob', 'Alice', 'Tom', 'Tom']
# for user in users:
#     print (f'Hello {user}')

# users = ['Tom', 'Bob', 'Alice', 'Tom', 'Tom']
# i = 0
# while i < len(users):
#     print(users[i])
#     i += 1



# users = [
#     ['Tom' 29]
#     ['Alise' 33]
#     ['Bob', 25]
# ]

# for user in users:
#     for inem in user:
#         print(item, end =' * ')


# strings = ['a', 'b', 'c', 'd', 'e']
# for index, starting in enumerate(strings, 1):
#     print (index, string)

#'---------------------------------------------------------------------------------------------------------------------

# numbers = ((1,2,3),("sv","fvf","xcv"))
# for num in numbers:
#     num_second,num_thhird ,hihk= num
#     print(num_second,num_thhird)
# print (type(numbers))

# qwe = {"1": "one", "2" : "two"}
# for x,y in qwe.items():
#     print(x,y)
    
#-------------------------------------------------------------------------------------------------------------------

# choise = 'y'

# while choise.lower() == 'y':
#     print('Privet')
#     choise = input('To continue enter "Y", for ending enter any')
# else:
# print('Process end')

# raining = False
# fire = False
# teacher_looking = True
# while not raining:
#     print("run")
#     if fire == True:
#         break
#     elif teacher_looking == False:
#          continue
#     elif raining == True:
#         print('Finish')
# else:
#     print('Go home')




    
    # students = ["One", "Two", "Three", "Four"]

    # for stufent in students:
    #     ("Hello" student)



# number = int(input("Enter u number"))
# factorial = 1
# for num in range(1, number+1):
#     factorial *= num
# print(f'Factorial of number {number} is {factorial}')

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i*j, end = "\t")
#     print("\n")



# number = int(input("Enter u number"))
# factorial = 1
# for num in range(1, number+1):
#     factorial *= num
# print(f'Factorial of number {number} is {factorial}')



# print ('Enter Y to exit')
# while True:
#     data = input('enter the amount for change')
#     if data.lower() == "y":
#         break
#     money = int(data)
#     cashe = round(money / 78, 2)
#     print('You will recieve', cashe, 'USA')
# print('Exchange workin')


#-----------------------------------------------------------------------------------------------------------
#sets 





# sets1 = set()
# sets2

# set3 = set(['Makers', 'coding', 'is', 'Makers'])
# print (set3)


# users = {['Bakyt', ]}

# set1 = (['qwe', 'qwe'])
# print (set1)


#-----------------------------------------------------------------------------------------------------------



# nums = [i**2 for i in range(10)]
# print(nums)

# list1 = list(range(1, 30))
# list2 = [num for num in list1 if num%2 == 0]
# print(list2)


# list1 = [-30, 34, 23,-14, -42, 23, 35, 235]
# list2 = [num for num in list1 if num%2 == 0 and num > 0] 
# print(list2)

# words = ['2020', '2012', '2031year', 'stroka']
# list1 = [word for word in words if word.isdigit()]
# print(list1)


# names = ['Baha', 'John', 'Abdykerim', 'Aynura', 'Mehmed', 'Sooronbay', 'Sharip', 'Atambay', 'Kut', 'Abdymalik']
# filtred_names = [name + 'bigger' if len(name) >=6 else name + 'Smoller' for name in names]
# print(filtred_names)


# john = {'name' : 'John', 'age' : '22'}
# Sam = {'name' : 'Sam', 'age' : '23'}
# Peter = {'name' : 'Peter', 'age' : '17'}

# users = [John, Sam, Peter]

# ages = [user.get('age') for user in users]
# print(ages)


# matrix = [
#     [0, 1, 2, 3],
#     [18, 11, 12],
#     [30, 31, 32],
# ]

# new_list = [x for row in matrix for x in row]


# from datetime import datetime

# start = datetime.now()

# list_ = []
# for i in range(10**10)


#-----------------------------------------------------------------------------------------------------------

# dict_abs = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 3}

# dict_123 = {value : key for key, value in dict_abs.items()}
# print(dict_123)

# my_dict = {key:value ** 2 for key, value in dict_abs.items()}
# print(my_dict)



# dict_abs = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : -4, 'e' : -5}
# new_dict = {key:val for key, val in my_dict.items() if val < 0 and key != 'e'}
# print(new_dict)

# list_a = [-2, -1, 0, 1, 2, 3, 4, 5, 2, 3, -2]
# my_set = {i for i in list_a}
# print(my_set)


# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10, 11]]
# list2 = [[num2**2 for num2 in num1] for num1 in list1]
# print(list2)


#----------------------------------------------------------------------------------------------------------



#                                        Exeption(Исключение)


# num1 = int(input(' '))
# num2 = int(input(' '))
# result = num1/num2
# print(' ')
# print(result)

#-------------------------------------------------------------------------------------------------------

# 

