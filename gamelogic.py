import random #It is used for suggest any random number
'''
A for Stone
B for Paper
C for Scissor
'''
#Welcome line for User
print("Hello User !\n      I am excited for playing Stone,Paper,Scissor Game with you.")
#How many round user like to play
round = int(input("How many round you want to play with me(please try to select between 1 to 20):"))
print("-"*50)
#Declare initial Score
computer_score = 0 
your_score = 0
draw = 0

Dict = {'A':"Stone", 'B':"Paper", 'C':"Scissor"} #Declare a dictonary which mention corresponding Input w.r.t User Input
no_suffix = {1: "st",2: "nd",3: "rd",4: "th",5: "th",6: "th",7: "th",8: "th",9: "th",10: "th",11: "th",12: "th",13: "th",14: "th",15: "th",16: "th",17: "th",18: "th",19: "th",20: "th"
}

i = 1
while(i<=round):
    computer_choice = random.choice(['A','B','C']) #Random Choice by Computer
    print("All the choices:-\nA : Stone\tB : Paper\tC : Scissor")
    print("-"*50)
    your_choice = input("Enter your Choice(A/B/C) :").upper() #User's Choice
    if your_choice not in Dict:
        print("Invalid choice, please select A, B, or C.")
        continue
    #This line is for telling the user which He choice and which input is chosen by Computer
    print(f"{i} {no_suffix[i]} Round:")
    print(f"You chose {Dict[your_choice]}\nComputer chose {Dict[computer_choice]}")

    #Conditions for winnings or Losings
    if(computer_choice == your_choice):
        print(f"{i} {no_suffix[i]} Round is drawn")
        print(f"Your Score : {your_score}\tComputer Score : {computer_score}\tDraw : {draw+1}")
        draw+=1 #increment the value
    else:
        if(computer_choice=='A' and your_choice=='B'):
            print(f"You win {i}{no_suffix[i]} round!")
            print(f"Your Score : {(your_score+1)}\tComputer Score : {computer_score}\tDraw : {draw}")
            your_score+=1 #increment the value
        elif(computer_choice=='A' and your_choice=='C'):
            print(f"Computer win {i}{no_suffix[i]} round!")
            print(f"Your Score : {your_score}\tComputer Score : {(computer_score+1)}\tDraw : {draw}")
            computer_score+=1 #increment the value
        elif(computer_choice=='C' and your_choice=='A'):
            print(f"You win {i}{no_suffix[i]} round!")
            print(f"Your Score : {(your_score+1)}\tComputer Score : {computer_score}\tDraw : {draw}")
            your_score+=1 #increment the value
        elif(computer_choice=='C' and your_choice=='B'):
            print(f"Computer win {i}{no_suffix[i]} round!")
            print(f"Your Score : {your_score}\tComputer Score : {(computer_score+1)}\tDraw : {draw}")
            computer_score+=1 #increment the value
        elif(computer_choice=='B' and your_choice=='C'):
            print(f"You win {i}{no_suffix[i]} round!")
            print(f"Your Score : {(your_score+1)}\tComputer Score : {computer_score}\tDraw : {draw}")
            your_score+=1 #increment the value
        elif(computer_choice=='B' and your_choice=='A'):
            print(f"Computer win {i}{no_suffix[i]} round!")
            print(f"Your Score : {your_score}\tComputer Score : {(computer_score+1)}\tDraw : {draw}")
            computer_score+=1 #increment the value
        else:
            print("Something Went wrong")
    i+=1
    print("-"*50)
print("")
#Match Result
print("!!! Match Finished !!!")
print("-"*30)
print(f"Total Round : {round}\nYour Score : {your_score}\nComputer Score : {computer_score}\nRound Drawn : {draw}")
if(your_score>computer_score):
    print("Hurray!!! You Won.")
elif(your_score<computer_score):
    print("Oops!!! You Lost.")
else:
    print("Match Drawn")
