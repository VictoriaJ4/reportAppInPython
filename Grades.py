import os
from dotenv import load_dotenv

load_dotenv()
final_cert_path = os.getenv("FINAL_CERT_PATH")
results_path= os.getenv("RESULTS_FILE_PATH")

print(f"Student file path: {final_cert_path}")


# results_path="C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\results.csv"
# final_cert_path="C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\FinalGrades.csv"

student_data=[]
grades_array=[]

all_students_2d=[]

#reads results csv file into lines skipping header
def read_results_file(results_path):
    global student_data
    results_file_data= open(results_path, "r")
    data_lines = results_file_data.readlines()[1:]
    student_data=data_lines
    results_file_data.close()
    return student_data ##these are all students and their data no header

##only call when creating cert report csv
def create_header_for_cert():
    results_file_data= open(results_path, "r")
    final_cert_header=results_file_data.readline().strip("\n")+ ","+ "FinalGrade"+"\n"
    results_file_data.close()
    return final_cert_header

#Extract student data function
def extract_student_data():
    global student_data,all_students_2d
    students=[]
    # Step 2: Loop through each student record
    for student in student_data:
        splitted_data = student.strip().split(",")
        students.append(splitted_data)

    all_students_2d=students
    return students ##this is array of arrays [ [], []]


# Create a function calculate_grades(student_marks) that converts numerical marks into grades.
#this is a checker
def get_marks():
    global grades_array
    all_students = extract_student_data()
    

    for i in range(len(all_students)):##runs as many times as we have students
        #print(f"Processing student {i}: {all_students[i]}")
        individual_student_data=all_students[i] #one student list []
        #print(f"Length of student data: {len(individual_student_data)}")
        student_grades=[]

        for j in range(3, len(individual_student_data)):##skip name,lastname and age
            grade=individual_student_data[j]
            student_grades.append(int(grade))
            
           
        grades_array.append(student_grades)
    return grades_array ##returns array


#Create a function calculate_certification(grades_list) to determine the final certification.
def calculate_final_cert():
    grades_array=get_marks()
    grade_labels=[] 
    cert_final=[]
    
    for student in grades_array:
        current_student=student
        student_certification=[]

        for grade in current_student:
         if grade<=50:
            student_certification.append("Unsuccessful")
         elif grade>50 and grade<=64:
            
            student_certification.append("Pass")
         elif grade>=65 and grade<=79:
            
            student_certification.append("Merit")
         else:
            
            student_certification.append("Distinction")

        if all(label == "Unsuccessful" for label in student_certification):
            overall_cert = "No Certification Achieved"  # All grades are unsuccessful
        elif "Unsuccessful" in student_certification:
            overall_cert = "Partial Certification Achieved"  # One or more unsuccessful grades
        else:
            overall_cert = "Full Certification Achieved"  # No unsuccessful grades
        
        # Store the results for this student
        grade_labels.append((student_certification))
        cert_final.append(overall_cert)
    return grade_labels,cert_final  # Return the list of grade labels and certifications


##create new file with all grades and calculations
def create_final_cert():
 students_2d=extract_student_data()
 final_cert_header=create_header_for_cert()
 grade_labels, cert_final = calculate_final_cert()
 students_results=[]


 for idx,student in enumerate(students_2d):
    name=student[:3]
    student_grades = grade_labels[idx]  
    final_cert = cert_final[idx]
    
    student_row = name + student_grades + [final_cert]
    # Append to the results list
    student_row_str = ",".join(map(str, student_row)) + "\n"
    students_results.append(student_row_str)

 try:
    with open(final_cert_path, "w") as file:
        file.write(final_cert_header)  # Write the header
        file.writelines(students_results)  # Write student data 
        print(f"Final certification file created ✅: {final_cert_path}")
 except:
     print("Error generating final cert report ❌. Chech if other user isn't using it.")


 
##user menu for creating certs
def user_menu_for_final_cert():
    print("========== Grades menu ============")
    user_answer=input(" Do you want to generate final cert? [y/n]").upper()
    if user_answer== "Y":
        create_final_cert()
        exit()
    elif user_answer== "N":
        exit()
    else:
        print("Invalid answer")

def main():
    read_results_file(results_path) ##we need to read allresults file first 
    calculate_final_cert()
    user_menu_for_final_cert()

if __name__ == "__main__":
    main()