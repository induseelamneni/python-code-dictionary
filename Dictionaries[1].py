Expression = input()

Dictionary = {"A":'Hello', "B": 'World', "C": 'Buddy',"D": 'Welcome'}
if Expression == "A and B":
    print(Dictionary["A"] + Dictionary["B"])
if Expression == "A and C":
    print(Dictionary["A"]+Dictionary["C"])
if Expression == "D or B":
    print(Dictionary["B"] or Dictionary["D"])
if Expression == "A or B":
    print(Dictionary["B"] or Dictionary["A"])
if Expression == "A and B and C":
    print(Dictionary["A"] + Dictionary["B"] + Dictionary["C"])
if Expression == "A and (B or C)":
    print(Dictionary["A"]+Dictionary["B"] or Dictionary["C"])
if Expression == "A and (C or D)":
    print(Dictionary["A"]+Dictionary["C"] or Dictionary["D"])
if Expression == "A and (B or C) and D":
    print(Dictionary["A"]+(Dictionary["C"] 
    or Dictionary["B"] )+ Dictionary["D"])