grades_file_path="C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\grades.csv"
modules_file_path= "C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\Modules.csv"
modules_array=[]

def read_grades_file():
    try:
     grades_file=open(grades_file_path, "r")
     data_lines=grades_file.readlines()
     print("============== All grades =========")
     for line in data_lines:
        print(line.strip())
     grades_file.close()
    except FileNotFoundError:
       print("File does not exsist, creating new file...")
       create_grades_file()


def create_grades_file():
   global grades_file_path
   grades_file=open(grades_file_path, "w")
   all_modules=get_modules()##this is an arrray
   print(all_modules)
   header_line = ",".join(all_modules) + "\n"        
   grades_file.write(header_line)
   grades_file.close()
   print("File created successfully ✅") 


def get_modules():
   global modules_file_path
   modules_file=open(modules_file_path, "r")
   modules_lines=modules_file.readlines()
   global modules_array
   for module in modules_lines[1:]:
       line=module.strip()
       modules_array.append(line)

   return modules_array  



def read_modules_file():
    pass




def main():
    read_grades_file()
    

main()