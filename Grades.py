grades_file_path="C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\grades.csv"
modules_file_path= "C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\Modules.csv"
students_file_path= "C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\students.csv"

modules_array=[]
students_array=[]

def read_grades_file():
    try:
     grades_file=open(grades_file_path, "r")
     data_lines=grades_file.readlines()
     print("============== All grades =========")
     for line in data_lines:
        print(line.strip())
     grades_file.close()
    except FileNotFoundError:
       print("File does not exsist, creating new file...")
       create_grades_file()


def create_grades_file():
   global grades_file_path
   grades_file=open(grades_file_path, "w")
   all_modules=get_modules()##this is an arrray
   print(all_modules)
   header_line = ",".join(all_modules) + "\n"        
   grades_file.write(header_line)
   grades_file.close()
   print("File created successfully ✅") 


def get_modules():
   global modules_file_path
   modules_file=open(modules_file_path, "r")
   modules_lines=modules_file.readlines()
   global modules_array
   for module in modules_lines[1:]:
       line=module.strip()
       modules_array.append(line)

   return modules_array  

def user_prompt():
   user_answer=input("Do you want to grade a student? [y/n]").lower()
   return user_answer
   
def user_grading_menu():
   answer_from_user=user_prompt()   

   if answer_from_user=="y":
      user_number=input("Choose the student you want to grade [1-8] > ")
      #print(user_number)
      return user_number
   elif answer_from_user=="n":
      exit()
   else:
      print("Invalid input")


def read_students_from_file():
   global students_file_path
   students_file=open(students_file_path, "r")
   student_lines=students_file.readlines()
   
   global students_array
   for module in student_lines[1:]:
       line=module.strip()
       students_array.append(line)

   return students_array  
   



def grade_student():
   student_ID=int(user_grading_menu())
   

def main():
    read_grades_file()
    read_students_from_file()
    

main()