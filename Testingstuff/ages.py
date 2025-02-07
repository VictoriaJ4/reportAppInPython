


def check_age():
  age= int(input("What is your age? :")) 
  if age <=0:  
   print("You don't exsist")
  elif age >=1 and age<12:
   print("You are a teenager")
  elif age >=13 and age<25:
   print("You are a young adult")
  elif age>=26 and age<65:  
   print ("You are adult")
  else: 
   print("You are retiree")


check_age()