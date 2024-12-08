import random
choices=("r","p","s") 
computer=random.choice(choices)
user_choice=input("Enter Your Choice (r/p/s)?: ")
if user_choice not in choices:
    print("Invalid Error!!")
else:
  if(computer==user_choice):
      print("Its a Draw")     
  print(f"Computer Chose {computer} and You Chose {user_choice}")
  if computer=="r" and user_choice=="p":
       print("You Win!!")
  elif computer=="p" and user_choice=="r":
      print("You Lose!!")
  elif computer=="s" and user_choice=="r":
      print("You Win!!")
  elif computer=="r" and user_choice=="s":
      print("You Lose!!")
  elif computer=="p" and user_choice=="s":
      print("You Win!!")      
  elif computer=="s" and user_choice=="p":
      print("You Lose!!")
