import re
######################################### title

print("Calculator")
print("Type 'quit' to exit\n")

######################################### set beginning

previous = 0
run = True

######################################### define variable

def performMath():
    global run
    global previous
    equation = ""
    if previous == 0:
            equation = input("Enter equation:")
    else:
        equation = input(str(previous))

######################################### define quit variables

    if equation == 'quit':
        print("thanks fo checking in, im still a piece of garbage")
        run = False
    if equation == 'quit' 'equation':
        print("thanks fo checking in, im still a piece of garbage")
        run = False

######################################### exceptions

    else:
        equation = re.sub('[a-zA-Z,.()" "]', '', equation)

######################################### calculate

    if previous == 0:
        previous = eval(equation)
    else:
        previous = eval(str(previous) + equation)

######################################### close variable script

while run:
    performMath()