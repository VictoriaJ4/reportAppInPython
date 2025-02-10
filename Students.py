student_file_path="C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\students.csv"

def read_student_file():
 global student_file_path
 try:
    file_text= open(student_file_path, "r")
    data_lines=file_text.readlines()
    print("=========== All students ============")
    print (data_lines)
    print("==================================")
 except FileNotFoundError:
    create_student_file()
    print("Error reading file.File does not exsist or is used by another user.")
    return 0
 

def create_student_file():
   global student_file_path
   file_text= open(student_file_path, "w")
   ##add header as first row
   header_line=file_text.write("Name", "LastName", "Age"+"\n")
   ##leave space for 8 learners?
   file_text.close()
   print("File created successfully")
   
 
def add_student():
    while(True):
     user_answer_add_student=input("Do you want to add student? [y/n]")
     if user_answer_add_student== "y" or user_answer_add_student=="Y":
        student_name=input("Add student first name >")
        student_last_name=input("Add student last name >")
        student_age=input("Add student age >")
        return(student_name,student_last_name, student_age)
     else:
        exit()    


def save_student_details():
    student_info=add_student()##saves student info into variable
    print(student_info)
    


def main():
    read_student_file()
    #add_student()
    
    #save_student_details()
main()    