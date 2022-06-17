# keyword argument = arguments preceded by an identifier when we pass them to function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Pythons knows the names of the arguments that our function recieves

## POSITIONAL ARGUMENTS
# def hello(firstname,middlename,lastname):
#     print("Hello "+firstname+" "+middlename+" "+lastname)
#
# hello("Pratham","Barua","Nabo")


##KEYWORD ARGUMENT

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(middle="Barua",first="Pratham",last="Nabo")