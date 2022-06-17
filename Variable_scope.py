# variable scope = The region that a variable is recognized
#                   A variable is only avilable from inside the region it is created.
#                   A global and locally scoped versions of a variavble can be created.

name = "Pratham"     #Global Variable (avaiable inside and outside functions)

def display_name():
    # name = "Nabo"      #local scope cz aita under declare kora hoise inside of a function
    print(name)

display_name()
print(name)

## ORDER IS
# L = LOCAL
# E = ENCLOSING
# G = GLOBAL
# B = BUILT - IN























