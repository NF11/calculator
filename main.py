import re

print("calculator")
print("type quit or q to exit\n")
prv = 0
run = True


def calculator():
    global prv
    global run
    equation = ""
    if prv == 0:
        equation = input("enter equation , to use float type ',' :\n")
    else:
        equation = input(str(prv))
    if equation == "quit" or equation == "q":
        print("bye x)")
        run = False
    else:
        equation = re.sub('[a-zA-Z;.:()" "]', '', equation)
        if prv == 0:
            prv = eval(equation)
        else:
            prv = eval(str(prv) + equation)


while run:
    calculator()
