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
    print("File does not exsist, creating new file...")
    create_student_file()
    return 0
 

def create_student_file():
   global student_file_path
   file_text= open(student_file_path, "w")
   #write() only accepts a single string argument
   header_line=file_text.write("Name,LastName,Age\n") 
   ##leave space for 8 learners?
   file_text.close()
   print("File created successfully")
   
 
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
    # add_user_imput=file_text.write(f"{student_info}\n") 
    print("Student details added successfully.")
    print("===============================")
    
##we need only 8 students so we need a checker of how many students there are and if <8 add if more than 8 stop
def main():
    read_student_file()
    get_student_details()
    insert_student_details()
    
    #save_student_details()
main()    