user_name=input("Type your name\n").upper()
print("Welcome "+user_name+" to the Amazon Jungle Adventure\n")
answer=input("You come near a bridge. You have two options: To (cross) or to (jump) from bridge.\n").lower()
if answer == "cross":
    print("You successfully crossed the bridge\n")
    answer1=input("After walking certain metres.You came near a river.Now you can (swim),cross by the help of rope through trees(rope),make a boat using the wood(boat)\n").lower()
    if answer1 == "swim":
      print("You are caught by Crocodiles of River and you died.Game Over\n")
    elif answer1== "rope":
      print("The rope broke as a result of which you fell into the river and died.\n")
    else:
        print("You successfully crossed the river with the help of Boat\n")
        answer2=input("After crossing the River,you came across a animal.You have two options to try to kill him(kill),escape from there(escape),try to give animal something(give)\n").lower()
        if answer2=="kill":
                         print("While trying to kill the animal,the animal killed you.Game Over\n")
        elif answer2=="escape":
                         print("While escaping from the animal.The animal ran behind you and killed you.Game Over\n")
        else: 
              print("You gave fruits to the animal and it was mesmerized by it and let you go.\n")
              answer3=input("You came across a stranger near the cave after travelling few miles.You have two options- To (ignore) him to (talk) with him.\n").lower()
              if answer3 =="ignore":
                                 print("You ignored the stranger and he did not talk with you.Game Over\n")
              else: 
                 answer4=input("You talk with him and he offered you a parcel.You have two options-To (take) or to (refuse).\n").lower()
                 if answer4=="refuse": 
                   print("You refused the parcel and did not get the coins.Game Over\n")
                 else: 
                      print("You took the parcel and got the gold coins.\n")
                      print(user_name+" won the game.\n")


else: 
    print("You died after jumping from Bridge.GAME OVER.")
 
