#global variables
all_modules=["","","",""] #no header, will show in menu option ##4
modules_header=["","","","",""] #modules with header- will be  saved in report ##5
file_path= "C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\Modules.csv"


def read_modules(path):
    file_text= open(path, "r")
    data_lines=file_text.readlines() ##this is a string
    return data_lines
   
def organise_data():
    global all_modules
    global modules_header
    data_lines=read_modules("C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\Modules.csv")
    for i in range(4):
        all_modules[i]=data_lines[i+1]
        
    for i in range(5):
        modules_header[i]=data_lines[i]
         
         
#this function edits module
def write_modules():
    while(True):
     user_input=int(input("Press 1 to 4 to edit module or 0 to exit > "))
     chosen_module=all_modules[user_input]
     print(chosen_module)
    
     if user_input>0 and user_input<4:
       all_modules[user_input] =input("Enter new module name > ")
       print(all_modules)
     else:
        exit
    else:
       exit
    
##upate array with header

##create report close file

def main():
    read_modules(file_path)

    organise_data()
   
    print("==============All modules===========")
    print(all_modules[0],all_modules[1],all_modules[2], all_modules[3])
    print("======= You're editing modules =========")

    write_modules()

main()