"""
python handbook v0.0
only cli(right now")
this was made so i can learn python
make a project
and find python functions easly
email: mendelsshop@gmail.com
"""
def ifs():
    print("""#      if statement             #\n
            # an if statement is saying      """)
def whileloos():
    print("""#       whileloops             #\n# """)

def main():
    pythondict = {"while loops":"whileloos()", "if statements": "ifs()"} #create dictinary for searching
    print("   1.Show all explanations \n   2.Search \n   3.Quit ")

    choose = input("choose an option: ")
    if choose == "1":
        for key in pythondict: #for loop that lists all names in dictionary
            print(key)
            #exec(pythondict[key])
            

    elif choose == "2":
        for key in pythondict: #for loop that lists all names in dictionary
            print(key) 
        search = input("what are you searching for: ")#ask for a name in dictinary
        for key in pythondict:
            if key == search:
                exec(pythondict[key])
                main()
            elif key != search:
                main()
                
           
    elif choose == "3":
        exit()


            

            
    
main()

