##this calculates grades based on results to be able to do it we need results
# •	Calculate the grade achieved in each module based on the following
# o	< 50% - Unsuccessfully
# o	50% – 64% Pass
# o	65%-79% Merit
# o	>= 80% Distinction

# •	Calculate the overall certification achieved as follows
# o	Pass or better in all four modules = Full Certification Achieved
# o	All unsuccessful grades – No Certification Achieved
# o	One, two or three unsuccessful – Partial Certification Achieved

results_path="C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\results.csv"

student_data=[]
grades_array=[]
final_cert_header=""

#reads results csv file into lines skipping header
def read_results_file(results_path):
    global student_data
    results_file_data= open(results_path, "r")
    data_lines = results_file_data.readlines()[1:]
    #student_data=data_lines
    student_data=data_lines
    return student_data ##these are all students and their data no header

def create_header_for_cert():
    global final_cert_header
    results_file_data= open(results_path, "r")
    final_cert_header=results_file_data.readline().strip("\n")
    return final_cert_header

#Extract student data function
def extract_student_data():
    global student_data
    students=[]
    # Step 2: Loop through each student record
    for student in student_data:
        splitted_data = student.strip().split(",")
        students.append(splitted_data)

    #print("from second function",students)
    return students ##this is array of arrays [ [], []]


# Create a function calculate_grades(student_marks) that converts numerical marks into grades.
#this is a checker
def get_marks():
    all_students=extract_student_data()
    #print("third function",all_students)
    global grades_array

    for i in range(len(all_students)):##runs as many times as we have students
        #print(f"Processing student {i}: {all_students[i]}")
        individual_student_data=all_students[i] #one student list []
        #print(f"Length of student data: {len(individual_student_data)}")
           
        for j in range(3, len(individual_student_data)):##skip name,lastname and age
            #print(individual_student_data[j])
            grades=individual_student_data[j]
            print("Grades", grades)
            grades_array.append(int(grades))##save all grades in an array grades
                    
    
    #print(grades_array)
    return grades_array ##returns array


#Create a function calculate_certification(grades_list) to determine the final certification.
def calculate_final_cert():
    global grades_array
    grade_labels=[] ##initially empty

    for i in grades_array:
        if i== 50:
            grade_labels.append("Unsucesfull")
            print("Unsucesfull")
        elif i>50 and i<=64:
            print("pass ")
            grade_labels.append("Pass")
        elif i>=65 and i<=79:
            print("merit")
            grade_labels.append("Merit")
        else:
            print("distinction")
            grade_labels.append("Distinction")
    print(grade_labels)
    return grade_labels ##returns aray


##create new file with all grades and calculations
def create_final_cert():
 header=final_cert_header
 print("hello from create final cert")


##user menu for creating certs
def user_menu_for_final_cert():
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
    create_header_for_cert()
    #print(student_data)
    get_marks()
    #print(grades_array)
    calculate_final_cert()
    user_menu_for_final_cert()

main()