#This program calulates y=mx+c

from colorama import Fore


def valInputs():
    print(Fore.RED + "DO NOT INCLUE '()' OR ',' ONLY THE NUMBERS \nThe numbers should be formated like: 4 8\nThey must include a space between the numbers!")
    x, y = input(Fore.BLUE + "First set of coordinates: ").split()
    if "," in x:
        print(Fore.RED + "ERROR: Must not inclue: ,")
    else:
        x2, y2 = input(Fore.BLUE + "Second set of coordinates: ").split()
        # Subtracting the y values from each other
        top = (int(y)-int(y2))
        # Subtracting the x values from each other
        bot =(int(x)-int(x2))
        # Dividing the top and bottom values to get the gradient.
        m = int(top/bot)
        # Multiplying the gradient by the x value.
        mx = int(m * x)
        # Subtracting the y value from the mx value to get the c value.
        c = int(y) - mx
        print(Fore.CYAN+"=======================")
        print(Fore.BLUE + "C= " + str(c))
        print(Fore.GREEN + "equation: " + str(y)+"="+str(m)+"+"+str(c) + Fore.RESET)
        print(Fore.CYAN + "======================="+Fore.RESET)


#runs code
valInputs()
