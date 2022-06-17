# nested loops = the inner loop will finish all of its iteration before finishing one iterration of the outer loop

rows = int(input("Enter how many rows do you want ?:"))
columns = int(input("Enter how many columns do you want ?: "))
symbol = input("Enter the symbol to use :")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")#end ta prevent kore next line a jaowa theke prevent kora ta
    print()
