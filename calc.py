import re

print("My own Fantastic Calculator")
print("Tap 'Quit' to exit \n")

previous = 0
run = True


def do_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter the equation:")
    else:
        equation = input(str(previous))
    if equation == 'Quit':
        print("bye bye bye")
        run = False
    else:
        equation = re.sub('[a-zA-Z,./?" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    do_math()



