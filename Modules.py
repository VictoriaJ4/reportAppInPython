#global variables
all_modules=["","","",""] #no header, will show in menu option ##4
modules_header=["","","","",""] #modules with header- will be saved in report ##5
file_path= "C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\Modules.csv"


#shows menu for modules, calls show all modules 
def show_all_modules():
    print("==============All modules===========")
    for module in all_modules:
       print(module.strip())
    print("====================================")
   
# reads modules from the file (happening first), error handling added
def read_modules(path):
 try:
     file_text= open(path, "r")
     data_lines=file_text.readlines() ##this is a string
     return data_lines
 except FileNotFoundError:
    print("File not found. Exiting...")
    exit()
 except FileExistsError:
    print("Check if file exsist. Exiting...")
    exit()
    
   
## calls function read modules and saves data into variable, loops and pushes modules to array that is global
def organise_data():
    global all_modules
    global modules_header
    global file_path
    data_lines=read_modules(file_path) ##array of strings
    for i in range(len(all_modules)):##4
        all_modules[i]=data_lines[i+1].strip()
        
        
    for i in range(len(modules_header)):
        modules_header[i]=data_lines[i].strip()## strip here so it saves without \n in report later
         
         
#this function edits modules
def write_modules():
    while(True):
     user_input=int(input("Press [1 - 4] to edit module, 9 to save and create module report or 0 to exit > "))

     if user_input>0 and user_input<4:
        user_imput_str=input("Enter new module name > ")
        all_modules[user_input-1] =user_imput_str
        update_header_array()
        show_all_modules()
     elif user_input==0:
        break
     elif user_input==9 or user_input==9:
        create_report() ##user chose to save and create report
        break
     else: ##error handling user can only choose numbers 1-4, 9 or 0 no letters
        print("⚠️ Invalid input.⚠️")
        break
    

##upate array with header, we need this to save into file with HEADER not only modules
def update_header_array():
    modules_header[1]=all_modules[0].strip()
    modules_header[2]=all_modules[1].strip()
    modules_header[3]=all_modules[2].strip()
    modules_header[4]=all_modules[3].strip()
    
##creates file writes changes added by user
def create_report():
 global file_path
 try:
    result_file_name=file_path
    file_handler=open(result_file_name, "w")
    
    for module in modules_header:
     file_handler.write(module+"\n")
    file_handler.close()
    print("Report successfully created.") 
 except:
        print("Something went wrong😒. Make sure the file is not used by other users.")
        exit()

def main():
    organise_data()
    show_all_modules()
    write_modules()
    
    

main()