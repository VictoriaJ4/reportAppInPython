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

#reads results csv file into lines skipping header
def read_results_file(results_path):
    results_file_data= open(results_path, "r")
    data_lines = results_file_data.readlines()[1:]
    #print("From first function",data_lines)
    return data_lines ##these are all students and their data no header


#Extract student data function
def extract_student_data():
    data_lines=read_results_file(results_path)
    students=[]
    # Step 2: Loop through each student record
    for student in data_lines:
        splitted_data = student.strip().split(",")
        students.append(splitted_data)

    #print("from second function",students)
    return students ##this is array of arrays [ [], []]


# Create a function calculate_grades(student_marks) that converts numerical marks into grades.
#this is a checker
def get_marks():
    all_students=extract_student_data()
    #print("third function",all_students)
    grades_array=[]

    for i in range(len(all_students)):##runs as many times as we have students
        #print(f"Processing student {i}: {all_students[i]}")
        individual_student_data=all_students[i] #one student list []
        #print(f"Length of student data: {len(individual_student_data)}")
           
        for j in range(3, len(individual_student_data)):##skip name,lastname and age
            #print(individual_student_data[j])
            grades=individual_student_data[j]
            print("Grades", grades)
            grades_array.append(int(grades))##save all grades in an array grades
                    
    
    print(grades_array)
    return grades_array ##returns array


#Create a function calculate_certification(grades_list) to determine the final certification.
def calculate_final_cert():
    all_grades=get_marks() ##array of grades
    grade_labels=[] ##initially empty

    for i in all_grades:
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
 pass

##user menu for creating certs
def user_menu_for_final_cert():
    input(" Do you want to generate final cert? [y/n]")

def main():
    #extract_student_data()
    #calculate_grades()
    calculate_final_cert()

main()