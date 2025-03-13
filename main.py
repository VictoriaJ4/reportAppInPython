import Modules
import Students
import Results
import Grades

def top_level_menu():
 print("================ Select option =============")
 print(" 1) Modules")
 print(" 2) Students")
 print(" 3) Marks")
 print(" 4) Grades")
 print(" or press 0 to exit")
 print("============================================")

def user_input():
    try:
        user_choice = int(input("Select > "))
        return user_choice
    except ValueError:
        print("Invalid input. Please enter a number.")
        return -1


def conditional_dispaly():
 user_choice=user_input()

 if user_choice==1:
    Modules.main()
    
 elif user_choice==2:
  Students.main()
 elif user_choice==3:
  Results.main()
 elif user_choice==4:
  Grades.main()
 elif user_choice==0:
  exit()
 else:
  print("invalid input") 
 

def main():
 top_level_menu() 
 conditional_dispaly()
 
 
if __name__ == "__main__":
    main()