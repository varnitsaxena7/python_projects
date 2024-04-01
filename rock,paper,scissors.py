#PROJECT 2(ROCK,PAPER,SCISSORS) BY VARNIT SAXENA
import random

computer_score=0
user_score=0

choices=["ROCK","PAPER","SCISSORS"]
strs=input("Enter your name\n").upper()
while True:
       user_choice=input("Enter your choice Rock,Paper,Scissors to Continue else enter No to exit\n").upper()
       if user_choice=="NO":
          break
       else:
          pc=random.randint(0,2)
          pc_choice=choices[pc]
          print("Computer choice is "+pc_choice+".\n")
          if pc_choice=="ROCK" and user_choice=="PAPER":
                                        print("YOU WON\n")
                                        user_score=user_score+1
         
          elif pc_choice=="PAPER" and user_choice=="SCISSORS":
                                        print("YOU WON\n")
                                        user_score=user_score+1
         
          elif pc_choice=="SCISSORS" and user_choice=="ROCK":
                                        print("YOU WON\n")
                                        user_score=user_score+1
          elif pc_choice=="ROCK" and user_choice=="SCISSORS":
                                        print("YOU LOST\n")
                                        computer_score+=1
          elif pc_choice=="SCISSORS" and user_choice=="PAPER":
                                        print("YOU LOST\n")
                                        computer_score+=1
          elif pc_choice=="PAPER" and user_choice=="ROCK":
                                        print("YOU LOST\n")
                                        computer_score+=1
          else:
                print("Tied\n")



print("Computer wins in "+str(computer_score)+" chances.\n")
print(strs+" wins in "+str(user_score)+ " chances.\n")
if computer_score>user_score:
             print("Computer wins the match\n")
elif computer_score<user_score:
             print(strs+" wins the match\n")
else:
             print("Match is Tied.\n")


                        
