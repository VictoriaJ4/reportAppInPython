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

def read_results_file(results_path):
    results_file_data= open(results_path, "r")
    data_lines = results_file_data.readlines()[1:]
    #print(data_lines)
    return data_lines ##these are all students and their data no header


#Extract student data function
def extract_student_data():
    data_lines=read_results_file(results_path)
    students=[]
    # Step 2: Loop through each student record
    for student in data_lines:
        splitted_data = student.strip().split(",")
        students.append(splitted_data)

    print(students)
    return students ##this is array of arrays [ [], []]


# Create a function calculate_grades(student_marks) that converts numerical marks into grades.
def calculate_grades():
    pass


#Create a function calculate_certification(grades_list) to determine the final certification.
def calculate_final_cert():
    pass


##create new file with all grades and calculations
def create_final_cert():
 pass

##user menu for creating certs


def main():
    read_results_file(results_path)
    extract_student_data()


main()