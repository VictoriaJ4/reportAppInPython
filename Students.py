import main
import os
from dotenv import load_dotenv

load_dotenv()
student_file_path = os.getenv("STUDENT_FILE_PATH")


print(f"Student file path: {student_file_path}")

## reads all students from csv file
def read_student_file():
 global student_file_path
 try:
    file_text= open(student_file_path, "r")##reads file
    data_lines=file_text.readlines() # gets file into lines
    ##calls function to show all students into terminal and passes data_lines
    show_all_students(data_lines)
    file_text.close()##close the file
    checker_if_8()##this opens file again to check
 except FileNotFoundError:
    print("File does not exsist, creating new file...")
    create_student_file()
 
##prints all students into terminal
def show_all_students(data_lines):
    data_lines= data_lines
    print("=========== All students ============")
    for line in data_lines[1:]:
       print(line.strip())
    print("==================================")
    

def create_student_file():
   global student_file_path
   file_text= open(student_file_path, "w")
   #write() only accepts a single string argument
   header_line=file_text.write("Name,LastName,Age\n") 
   file_text.close()
   print("File created successfully ✅")
   
 ## Prompts user and saves response into variables which are passed to insert_student_details function
def get_student_details():
    while True:
     user_answer_add_student=input("Do you want to add student? [y/n]")
     if user_answer_add_student== "y" or user_answer_add_student=="Y":
        student_name=input("Add student first name >")
        student_last_name=input("Add student last name >")
        student_age=input("Add student age >")
        insert_student_details(student_name,student_last_name, student_age)
     else:
        exit()    
        

## receives details typed by user and adds a new row with it in the students file
def insert_student_details(name,lastname,age):
    student_info=[name,lastname,age]
    try:
     file_text= open(student_file_path, "a")
     file_text.write(",".join(student_info) + "\n")
     file_text.close()
     print("Student details added successfully.✅")
     print("===============================")
    except:
       print("Coudln't save changes to the file. Try again.")
       get_student_details()

##reads student file and checks how many students are enrolled
def checker_how_many_students():
   file_text= open(student_file_path, "r")##open file to read only
   file_lines=file_text.readlines()##add file into lines
   count_of_students=0

   for student in file_lines[1:]:
      count_of_students+=1
      
   print("Total of enrolled students is: ",count_of_students)
   print("================================")
   file_text.close()
   return count_of_students

##checking if there is 8 students (maximum of students enrolled is 8)
def checker_if_8():
   student_count=checker_how_many_students()
   student_name, student_last_name, student_age = get_student_details()
   if student_count<8:
    insert_student_details(student_name, student_last_name, student_age)
   elif student_count==0:
      insert_student_details(student_name, student_last_name, student_age)
   else:
    print("Maximum number of students enrolled. ❌")
    exit()


def main():
    read_student_file()
    

if __name__ == "__main__":
    main()  