import random

#prompt user - get the answer 

def prompt_user():
  user_input=input("🎲 Do you want to roll the dice?  y/n ▶️  ").lower()
  return user_input

def roll_dice():
    dice_numbers=[1,2,3,4,5,6]
    #this needs to be inside the loop to prompt user each time until user says N
    user_input=prompt_user()
    while user_input=="y":
        random_number=random.choice(dice_numbers)
        print(f"Dice rolled your number is > {random_number}")
        dice_test(random_number)
        return random_number
    else:
        print("Thank you for playing, goodbye")
        exit(0)

    
    
def dice_test(random_number):
 number=random_number
 numbers=[0,0,0,0,0,0]

 for x in range(10000):
     if number==1:
      numbers[0]+=1
     elif number==2:
        numbers[1]+=1
     elif number==3:
      numbers[2]+=1
     elif number==4:
       numbers[3]+=1
     elif number==5:
       numbers[4]=1
     elif number==6:
       numbers[5]+=1
     else:
       print("Not a valid number")
 print("\n--- Dice Fairness Test Results ---")
 print(f"Number 1: {numbers[0]} times")
 print(f"Number 2: {numbers[1]} times")
 print(f"Number 3: {numbers[2]} times")
 print(f"Number 4: {numbers[3]} times")
 print(f"Number 5: {numbers[4]} times")
 print(f"Number 6: {numbers[5]} times")



#call functions 
roll_dice()
