# *args = parameter that will pack all argument into tuple
#         useful so that a function can accept a varying amount of arguments.

##Shudu matro specific number ar jonno
# def add(num1,num2):
#     sum= num1+num2
#     return sum
#
# print(add(4,6)) #aikhane jdi ami akhon 3 ta number pathai tahole aita akhon kaj e krbe na

##In Args
def Add(*add): #aikhaen ami chahile * ar por jekono nam dite parbo
    sum = 0
    for i in add:
        sum = sum + i
    return sum


print(Add(1,2,3,4)) #aikhane ami chaile iccha moto value pathaite parbo

















