def rpsgame():
 
 import random
 a=input("Enter an option:\n1.Rock\n2.Paper\n3.Scissors\n")
 choices=["Rock","Paper","Scissors"]
 computer_choice = random.choice(choices)
 if(computer_choice==a):
    print(f"You both chose {a}. It's a tie.")

    b=input("Do you want to play again?")
    if(b=="yes" or b=="Yes"):
        rpsgame()
    else:
        print("Thank you for playing!")
 elif(a=="Rock"):
  if(computer_choice=="Paper"):
        print("Computer chose Paper, You Lose.")
       
        
        b=input("Do you want to play again?")
        if(b=="yes" or b=="Yes"):
            rpsgame()
        else:
            print("Thank you for playing!")
  else:
        print("Computer chose Scissors, You Win!")
        b=input("Do you want to play again?")
        if(b=="yes" or b=="Yes"):
            rpsgame()
        else:
            print("Thank you for playing!")
            
 elif(a=="Paper"):
    if(computer_choice=="Rock"):
        print("Computer chose Rock, You Win!")
        b=input("Do you want to play again?")
        if(b=="yes" or b=="Yes"):
            rpsgame()
        else:
            print("Thank you for playing!")
    else:
        print("Computer chose Scissors, You Lose.")

        b=input("Do you want to play again?")
        if(b=="yes" or b=="Yes"):
            rpsgame()
        else:
            print("Thank you for playing!")
 elif(a=="Scissors"):
    if(computer_choice=="Rock"):
        print("Computer chose Rock, You Lose.")
 
        b=input("Do you want to play again?")
        if(b=="yes" or b=="Yes"):
            rpsgame()
        else:
            print("Thank you for playing!")
    else:
        print("Computer chose Paper, You Win!")
       
        b=input("Do you want to play again?")
        if(b=="yes" or b=="Yes"):
            rpsgame()
        else:
            print("Thank you for playing!")
rpsgame()
