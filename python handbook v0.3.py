"""
python handbook v0.1
only cli(right now)
this was made so i can learn python
make a project
and find python functions easily
email: mendelsshop@gmail.com
now using
"""
boxTop = "#################################\n"
boxBottom = "#################################\n"

searchlist = {"while loops": "whiles()", "if statements": "ifs()", "for loops": "fors()", "print statements": "prints()", "user input": "inputs()", "math functions": "maths()"}  # create dictionary for searching


def option1():
    for key in searchlist:  # for loop that lists all names in dictionary
        exec(searchlist[key])
    main()


def option2():
    for key in searchlist:  # for loop that lists all names in dictionary
        print(key)
    search = input("what are you searching for: ")  # ask for a name in dictinary
    for key in searchlist:
        if key == search:
            exec(searchlist[key])
        elif key == "main menu":
            main()
    main()


def option3():
    search = input("what are you searching for: ")  # ask for a name in dictinary
    for key in searchlist:
        if key == search:
            exec(searchlist[key])
        elif key == "main menu":
            main()


def ifs():
    l1 = "#      if statements            #\n"
    l2 = "# an if statament is telling    #\n"
    l3 = "# the computer to do something  #\n"
    l4 = "# if a condotion is met         #\n"

    print(boxTop + l1 + l2 + l3 + l4 + boxBottom)


def whiles():
    l1 = "#      while loops              #\n"
    l2 = "#                               #\n"
    print(boxTop + l1 + l2 + boxBottom)


def fors():
    l1 = "#      for loops               #\n"
    l2 = "#                              #\n"
    print(boxTop + l1 + l2 + boxBottom)


def prints():
    l1 = "#      print statements        #\n"
    l2 = "# a print statement is how     #\n"
    l3 = "# you make the computer talk   #\n"
    print(boxTop + l1 + l2 + l3 + boxBottom)


def inputs():
    l1 = "#     user input               #\n"
    l2 = "# this is how we ask the user  #\n"
    l3 = "# for input                    #\n"
    print(boxTop + l1 + l2 + l3 + boxBottom)


def maths():
    l1 = "#     math function            #\n"
    l2 = "# + is for addition            #\n"
    l3 = "# - is for subtraction         #\n"
    print(boxTop + l1 + l2 + l3 + boxBottom)


def main():
    print("   1.Show all explanations \n   2.Show all operations \n   3.Quit ")

    choose = input("choose an option: ")
    for key in searchlist:
        if choose == "1":
            option1()
        elif choose == "2":
            option2()
        elif choose == key:
            exec(searchlist[key])
            main()
        elif choose == "4":
            quit()


main()
