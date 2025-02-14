results_file_path="C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\results.csv"
modules_file_path= "C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\Modules.csv"
students_file_path= "C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\students.csv"

#initially empty but we read filelines into these arrays
modules=[]
students=[]
grades=[]
results=[]

#read modules from modules csv file and pushes info into array modules
def get_modules_from_file():
   global modules_file_path
   modules_file=open(modules_file_path, "r")
   modules_lines=modules_file.readlines()##reads into array of strings

   for module in modules_lines[1:]:##loop through all modules and skip the header
      stripped_module = module.strip()  ## remove whitespaces
      modules.append(stripped_module)
      
   modules_file.close()
   return modules ##returns only modules 4


#read students from file
def read_students_file():
 global students ##without it it won't push students into array of students and array will stay empty
 students_file=open(students_file_path, "r")
 student_lines=students_file.readlines()[1:]
 stripped_students = [line.strip().split(",") for line in student_lines]
 students.extend(stripped_students) ##cant use append  here it will create 3d array 
 print(students)
 students_file.close()
 return students  


#define results header, gets modules that will be part of our header and adds few fields before it separated by commas
def results_header(modules):
 for module in modules:
  results_header = f"Firstname,Lastname,Age,{','.join(modules)}"
 return results_header


#enter student results
def enter_student_results():
   # enter results for each student and each module
   global results
   students=read_students_file()##reads students and adds them to students variable that is a list [[nina,dobrev,24]] 

   for student in students:
      #students.append(student)
      print(f" === Results for : {student[0]} {student[1]} ===")# shows current student name and last name
      result = ",".join(student) #Converts student details into a comma-separated string (e.g., "nina,dobrev,64")

      for module in modules:
        marks=input(f"Please enter results for {module} >")
        result +=","+ str(marks)
        
      results.append(result)
   return results

#gets results from enter_students_results() and writing all into a file
def write_results_file(results,results_file_path):
   header=results_header(modules) ## Firstname,Lastname,Age,module1,module2,module3,module4
   try:
    result_file=open(results_file_path, "w")
    result_file.write(header + "\n")

    for result in results:
        result_file.write(result + "\n")

    result_file.close()
    print(f"Results have been written to {results_file_path}")
    exit()
   except FileNotFoundError:
     print("No file found. Create a file first.")
     exit()
   except PermissionError:
     print("File error, another user is using this file. Try again later.")
     exit()


def main():
 get_modules_from_file() ##works fine
 #header=results_header(modules)  DON'T need to call it here but rather inside write function as we need header only for csv file
 enter_student_results()
 write_results_file(results,results_file_path)


if __name__ == "__main__":
    main()
