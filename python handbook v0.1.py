"""
python handbook v0.1
only cli(right now)
this was made so i can learn python
make a project
and find python functions easly
email: mendelsshop@gmail.com
"""
boxTop = "#################################\n"
boxBottom = "\n#################################\n"

pythondict = {"while loops":"whileloos()", "if statements": "ifs()"} #create dictinary for searching
def option1():
    for key in pythondict: #for loop that lists all names in dictionary
        exec(pythondict[key])
    main()
def option2():
    for key in pythondict: #for loop that lists all names in dictionary
        print(key) 
    search = input("what are you searching for: ")#ask for a name in dictinary
    for key in pythondict:
        if key == search:
            exec(pythondict[key])
        main()

        
def ifs():   
    print(boxTop+"""#      if statement             #\n# an if statement is saying     #""",boxBottom)
def whileloos():
    print(boxTop+"""#      whileloops               #\n#                               #""",boxBottom)

def main():
    
    print("   1.Show all explanations \n   2.Search \n   3.Quit ")

    choose = input("choose an option: ")
    if choose == "1":
        option1()            
    elif choose == "2":
        option2()           
    elif choose == "3":
        exit()


            

            
    
main()

