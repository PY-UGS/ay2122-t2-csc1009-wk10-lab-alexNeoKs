modulecode = input("Please enter a module code(example: CSC1009) : ") 


def python_has_no_switch_forsomereason(modulecode):
    switcher = {
        "CSC1009": "Object-Oriented Programming",
        "CSC1006": "Math 2",
        "CSC1007": "Operating systems",
        "CSC1008": "Data structures and algorithms"
    }
    
    for i in switcher:
        if i == modulecode:
            return switcher[i]



print(python_has_no_switch_forsomereason(modulecode))

for i in range(102,65,-1):
    if i % 2 != 0:
        print(i)