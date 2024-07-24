while True:
    import random
    comp = random.randint(0,2)
    user = int(input("0 for rock,1 for paper ,2 for Scissor:\n"))
    def check(comp, user):
        if comp==user:
            return 0
        if comp==0 and user==2:
            return -1
        if comp==1 and user==0:
            return -1
        if comp==2 and user==1:
            return -1
        return 1
    score=check(comp,user)
    print("you " , user)
    print("computer ", comp)
    if score==0:
        print("the game is drow")
    elif score==1:
        print("you won the game")
    elif score==-1:
        print("you lost the game")
    else:
        print("invaild syntax")
    restart=input("do you want to play the game ?(yes/no):")
    if restart=="no":
        break

