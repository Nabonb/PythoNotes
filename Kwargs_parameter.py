# **kwargs = parameter that will pack all argument into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

#FOR NORMAL
# def hello(first,last):
#     print("Hello "+first+" "+last)
#
# hello(first="Pratham",last="Nabo")            #aikhane jdi ami akhon aro akhta middle name add kori tahole aita error dekhabe

##FOR KWARGS

def hello(**name):
    # print("Hello "+name["first"]+" "+name["middle"]+" "+name["last"])
    #OR
    print("Hello",end=" ")
    for key,value in name.items():
        print(value,end=" ")

hello(title="MR.",first="Pratham",middle="Barua",last="Nabo")     #aitate ami chaile aro add krte parbo kopno error ashbe na










