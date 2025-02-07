#global variables
all_modules=["","","",""] #no header, will show in menu option ##4
modules_header=["","","","",""] #modules with header- will be  saved in report ##5
file_path= "C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\Modules.csv"

def show_all_modules():
   for module in all_modules:
       print(module.strip())

def module_menu():
    print("==============All modules===========")
    show_all_modules() 
    print("====================================")
    #print(f" {i} {all_modules[i]} 2) {all_modules[1]} 3) {all_modules[2]} 4) {all_modules[3]}")
    #print("======= You're editing modules =========")


def read_modules(path):
    file_text= open(path, "r")
    data_lines=file_text.readlines() ##this is a string
    return data_lines
   

def organise_data():
    global all_modules
    global modules_header
    global file_path
    data_lines=read_modules(file_path)
    for i in range(len(all_modules)):##4
        all_modules[i]=data_lines[i+1]
        
    for i in range(len(modules_header)):
        modules_header[i]=data_lines[i]
         
         
#this function edits module
def write_modules():
    while(True):
     user_input=int(input("Press [1 - 4] to edit module or 0 to create a report and exit > "))

     if user_input==0:
        break

     if user_input>0 and user_input<4:
        user_imput_str=input("Enter new module name > ")
        all_modules[user_input-1] =user_imput_str
        module_menu()
     else:
        print("Invalid input.")
        break
    

##upate array with header
def update_header_array():
    modules_header[1]=all_modules[0].strip()
    modules_header[2]=all_modules[1].strip()
    modules_header[3]=all_modules[2].strip()
    modules_header[4]=all_modules[3].strip()
    
    
##create report close file    ##error handling if report doesnt exsist = create
    ##if exsists= overwriteit?
def create_report():
 try:
    result_file_name="C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\Report.csv"
    file_handler=open(result_file_name, "w")
    #print(modules_header)
    for module in modules_header:
     file_handler.write(module+ "\n")
    file_handler.close()
 except:
        print("Something went wrong😒. Make sure the file is not used by other users.")
        exit()

def main():
    organise_data()
    module_menu()
    write_modules()
    update_header_array()
    create_report()

main()