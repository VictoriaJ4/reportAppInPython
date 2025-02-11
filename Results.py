import csv
results_file_path="C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\results.csv"
modules_file_path= "C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\Modules.csv"
students_file_path= "C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\students.csv"

#initially empty but we read filelines into arrays
modules=[]
students=[]
grades=[]
results=[]


#read modules from file
def get_modules_from_file():
   global modules_file_path
   modules_file=open(modules_file_path, "r")
   modules_lines=modules_file.readlines()

   for module in modules_lines[1:]:
      stripped_module = module.strip()  
      modules.append(stripped_module)
      
   return modules
#read students from file
def read_students_file():
 #global students_file_path
 students_file=open(students_file_path, "r")
 student_lines=students_file.readlines()[1:]
 students = [line.strip().split(",") for line in student_lines]
   
 print(students)
 students_file.close()
 return students  

#define results header
def results_header(modules):
 for module in modules:
  results_header = f"Firstname,Lastname,Age,{','.join(modules)}"
 print("header",results_header)
 return results_header



#enter student results
def enter_student_results():
   # enter results for each student and each module
   global results
   students=read_students_file()

   for student in students:
      #students.append(student)
      print(f" === Results for : {student[0]},{student[1]} ===")
      result = ",".join(student)
      for module in modules:
        marks=input(f"Please enter results for {module} >")
        result +=","+ str(marks)
        
      results.append(result)
   print(results)
   return results

def write_results_file(results,header,results_file_path):
   try:
    result_file=open(results_file_path, "w")
    writer = csv.writer(result_file)
    writer.writerow(header.split(","))

    for result in results:
        writer.writerow(result.split(","))

    result_file.close()
    print(f"Results have been written to {results_file_path}")
   except FileNotFoundError:
     print("No file found. Create a file first.")
     exit()
   except PermissionError:
     print("File error, another user is using this file. Try again later.")
     exit()


def main():
 get_modules_from_file()
 #read_students_file()
 header=results_header(modules)
 enter_student_results()
 write_results_file(results,header,results_file_path)


main()

##bin
   
   # global results_file_path
   # results_file=open(results_file_path, "w")
   # all_modules=get_modules()##this is an arrray
   
   # header_line = ",".join(all_modules) + "\n"        
   # lines= []
   # lines = add_students_to_grades_file()
   
   # results_file.write(f"FirstName,LastName,Age,{header_line}") 
   # results_file.writelines (lines)
   # results_file.close()
   # print("File created successfully ✅") 

   # def add_students_to_grades_file():
#    students=read_students_from_file()   
#    lines = []
#    for student in students:
#       lines.append( f"{student[0]},{student[1]},{student[2]} \n")

#    return lines