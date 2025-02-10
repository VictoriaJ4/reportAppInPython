student_file_path="C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\students.csv"

def read_student_file():
 global student_file_path
 try:
    file_text= open(student_file_path, "r")##reads file
    data_lines=file_text.readlines()# gets file into lines
    print("=========== All students ============")
    for line in data_lines:
       print(line.strip())
    print("==================================")
    file_text.close()##close the file
    checker_if_8()##this opens file again to check
 except FileNotFoundError:
    print("File does not exsist, creating new file...")
    create_student_file()
 

def create_student_file():
   global student_file_path
   file_text= open(student_file_path, "w")
   #write() only accepts a single string argument
   header_line=file_text.write("Name,LastName,Age\n") 
   file_text.close()
   print("File created successfully ✅")
   
 
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


def insert_student_details(name,lastname,age):
    student_info=[name,lastname,age]
    file_text= open(student_file_path, "a")
    file_text.write(",".join(student_info) + "\n")
    file_text.close()
    print("Student details added successfully.✅")
    print("===============================")
    
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

##we need only 8 students so we need a checker of how many students there are and if <8 add if more than 8 stop
def main():
    read_student_file()


main()    