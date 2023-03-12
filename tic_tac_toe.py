import random
whatcorner = random.randint(1,5)

A = ["( )","( )","( )"]
B = ["( )","( )","( )"]
C = ["( )","( )","( )"]

def playermove(r,cl):
    if r == "A":
        if A[int(cl)-1] == "( )":
            A[int(cl)-1] = "(X)"
            return "exit"
        else:
            print("that spot is already taken")
    elif r == "B":
        if B[int(cl)-1] == "( )":
            B[int(cl)-1] = "(X)"
            return "exit"
        else:
            print("that spot is already taken")
    elif r == "C":
        if C[int(cl)-1] == "( )":
            C[int(cl)-1] = "(X)"
            return "exit"
        else:
            print("that spot is already taken")
    else:
        print("That isnt an option for this game")

def block():
    if A == ['(X)', '(X)', '( )'] or A == ['(X)', '( )', '(X)'] or A == ['( )', '(X)', '(X)']:
        if A == ['(X)', '(X)', '( )']:
            A[2] = "(O)"
        elif A == ['(X)', '( )', '(X)']:
            A[1] = "(O)"
        elif A == ['( )', '(X)', '(X)']:
            A[0] = "(O)"
    elif B == ['(X)', '(X)', '( )'] or B == ['(X)', '( )', '(X)'] or B == ['( )', '(X)', '(X)']:
        if B == ['(X)', '(X)', '( )']:
            B[2] = "(O)"
        elif B == ['(X)', '( )', '(X)']:
            B[1] = "(O)"
        elif B == ['( )', '(X)', '(X)']:
            B[0] = "(O)"
    elif C == ['(X)', '(X)', '( )'] or C == ['(X)', '( )', '(X)'] or C == ['( )', '(X)', '(X)']:
        if C == ['(X)', '(X)', '( )']:
            C[2] = "(O)"
        elif C == ['(X)', '( )', '(X)']:
            C[1] = "(O)"
        elif C == ['( )', '(X)', '(X)']:
            C[0] = "(O)"
    elif A[0] == "(X)" and B[0] == "(X)" and C[0] == "( )":
        C[0] = "(O)"
    elif A[0] == "(X)" and B[0] == "( )" and C[0] == "(X)":
        B[0] = "(O)"
    elif A[0] == "( )" and B[0] == "(X)" and C[0] == "(X)":
        A[0] = "(O)"
    elif A[1] == "(X)" and B[1] == "(X)" and C[1] == "( )":
        C[1] = "(O)"
    elif A[1] == "(X)" and B[1] == "( )" and C[1] == "(X)":
        B[1] = "(O)"
    elif A[1] == "( )" and B[1] == "(X)" and C[1] == "(X)":
        A[1] = "(O)"
    elif A[2] == "(X)" and B[2] == "(X)" and C[2] == "( )":
        C[2] = "(O)"
    elif A[2] == "(X)" and B[2] == "( )" and C[2] == "(X)":
        B[2] = "(O)"
    elif A[2] == "( )" and B[2] == "(X)" and C[2] == "(X)":
        A[2] = "(O)"
    elif A[0] == "(X)" and B[1] == "(X)" and C[2] == "( )":
        C[2] = "(O)"
    elif A[0] == "( )" and B[1] == "(X)" and C[2] == "(X)":
        A[0] = "(O)"
    else:
        trytowin()

def trytowin():
        if A == ['(O)', '(O)', '( )'] or A == ['(O)', '( )', '(O)'] or A == ['( )', '(O)', '(O)']:
            if A == ['(O)', '(O)', '( )']:
                A[2] = "(O)"
            elif A == ['(O)', '( )', '(O)']:
                A[1] = "(O)"
            elif A == ['( )', '(O)', '(O)']:
                A[0] = "(O)"
        elif B == ['(O)', '(O)', '( )'] or B == ['(O)', '( )', '(O)'] or B == ['( )', '(O)', '(O)']:
            if B == ['(O)', '(O)', '( )']:
                B[2] = "(O)"
            elif B == ['(O)', '( )', '(O)']:
                B[1] = "(O)"
            elif B == ['( )', '(O)', '(O)']:
                B[0] = "(O)"
        elif C == ['(O)', '(O)', '( )'] or C == ['(O)', '( )', '(O)'] or C == ['( )', '(O)', '(O)']:
            if C == ['(O)', '(O)', '( )']:
                C[2] = "(O)"
            elif C == ['(O)', '( )', '(O)']:
                C[1] = "(O)"
            elif C == ['( )', '(O)', '(O)']:
                C[0] = "(O)"
        elif A[0] == "(O)" and B[0] == "(O)" and C[0] == "( )":
            C[0] = "(O)"
        elif A[0] == "(O)" and B[0] == "( )" and C[0] == "(O)":
            B[0] = "(O)"
        elif A[0] == "( )" and B[0] == "(O)" and C[0] == "(O)":
            A[0] = "(O)"
        elif A[1] == "(O)" and B[1] == "(O)" and C[1] == "( )":
            C[1] = "(O)"
        elif A[1] == "(O)" and B[1] == "( )" and C[1] == "(O)":
            B[1] = "(O)"
        elif A[1] == "( )" and B[1] == "(O)" and C[1] == "(O)":
            A[1] = "(O)"
        elif A[2] == "(O)" and B[2] == "(O)" and C[2] == "( )":
            C[2] = "(O)"
        elif A[2] == "(O)" and B[2] == "( )" and C[2] == "(O)":
            B[2] = "(O)"
        elif A[2] == "( )" and B[2] == "(O)" and C[2] == "(O)":
            A[2] = "(O)"
        elif A[0] == "(O)" and B[1] == "(O)" and C[2] == "( )":
            C[2] = "(O)"
        elif A[0] == "( )" and B[1] == "(O)" and C[2] == "(O)":
            A[0] = "(O)"

def board():
    print("    1      2      3")
    print("A" + str(A))
    print("B" + str(B))
    print("C" + str(C))

def playerwin():
    if A == ['(X)', '(X)', '(X)'] or B == ['(X)', '(X)', '(X)'] or C == ['(X)', '(X)', '(X)']:
        return(True)
    elif A[0] == "(X)" and B[0] == "(X)" and C[0] == "(X)":
        return(True)
    elif A[1] == "(X)" and B[1] == "(X)" and C[1] == "(X)":
        return(True)
    elif A[2] == "(X)" and B[2] == "(X)" and C[2] == "(X)":
        return(True)
    elif A[0] == "(X)" and B[1] == "(X)" and C[2] == "(X)":
        return(True)
    elif A[0] == "(X)" and B[1] == "(X)" and C[2] == "(X)":
        return(True)
    else:
        return(False)

def computerwin():
    if A == ['(O)', '(O)', '(O)'] or B == ['(O)', '(O)', '(O)'] or C == ['(O)', '(O)', '(O)']:
        return(True)
    elif A[0] == "(O)" and B[0] == "(O)" and C[0] == "(O)":
        return(True)
    elif A[1] == "(O)" and B[1] == "(O)" and C[1] == "(O)":
        return(True)
    elif A[2] == "(O)" and B[2] == "(O)" and C[2] == "(O)":
        return(True)
    elif A[0] == "(O)" and B[1] == "(O)" and C[2] == "(O)":
        return(True)
    elif A[0] == "(O)" and B[1] == "(O)" and C[2] == "(O)":
        return(True)

#player goes first
flag = ""
while flag != "exit":
    board()
    print("Let's play tic tac toe! You go first, type the row and column you want your tic mark in\nfor example A2, B3, C1, ect")
    location = list(input().upper())
    row = location[0]
    column = location[1]
    flag = playermove(row, column)
board()

#computer's turn
print("my turn!")
if row == "B" and column == "2":
    if whatcorner == 1:
        A[0] = "(O)"
    elif whatcorner == 2:
        A[2] = "(O)"
    elif whatcorner == 3:
        C[0] = "(O)"
    elif whatcorner == 4:
        C[2] = "(O)"
else:
    B[1] = "(O)"
board()

#player's turn
flag2 = ""
while flag2 != "exit":
    board()
    print("where do you wanna go next? Type the row and column you want your tic mark in\nfor example A2, B3, C1, ect")
    location2 = list(input().upper())
    row2 = location2[0]
    column2 = location2[1]
    flag2 = playermove(row2, column2)
board()

#computer turn
print("my turn again!")
block()
board()

#player turn
flag3 = ""
while flag3 != "exit":
    board()
    print("where do you wanna go next? Type the row and column you want your tic mark in\nfor example A2, B3, C1, ect")
    location3 = list(input().upper())
    row3 = location3[0]
    column3 = location3[1]
    flag3 = playermove(row3, column3)
board()

#check for a win then computer turn
if playerwin() == True:
    print("you win!!")
elif computerwin() == True:
    print("I win!!")
else:
    print("my turn again!")
    block()
    board()

#check for a win then player turn
if playerwin() == True:
    print("you win!!")
elif computerwin() == True:
    print("I win!!")
else:
    flag4 = ""
    while flag4 != "exit":
        board()
        print("where do you wanna go next? Type the row and column you want your tic mark in\nfor example A2, B3, C1, ect")
        location4 = list(input().upper())
        row4 = location4[0]
        column4 = location4[1]
        flag4 = playermove(row4, column4)
    board()

#check for a win then computer turn
if playerwin() == True:
    print("you win!!")
elif computerwin() == True:
    print("I win!!")
else:
    print("my turn again!")
    block()
    board()

#check for a win then player turn
if playerwin() == True:
    print("you win!!")
elif computerwin() == True:
    print("I win!!")
else:
    flag5 = ""
    while flag5 != "exit":
        board()
        print("where do you wanna go next? Type the row and column you want your tic mark in\nfor example A2, B3, C1, ect")
        location5 = list(input().upper())
        row5 = location5[0]
        column5 = location5[1]
        flag5 = playermove(row5, column5)
    board()

#state if its a win or a draw
if playerwin() == True:
    print("you win!!")
elif computerwin() == True:
    print("I win!!")
else:
    print("its a draw!")

#comment: I love this game! For the row selection, you did accept both lower case and upper case letter.
#that is great! One thing maybe when I try to enter another letter, it still can direct me to choose the
#column. I wonder if you can make it "not an option" when enter a letter other than A B or C, and ask
#for another entry for letter. Another thing is, when I try to run this program twice, sometimes the 
#computer cannot generate its' choice. May be you can take a look at this. Overall is very good! 