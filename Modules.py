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

     if user_input==0:
        break

     if user_input>0 and user_input<4:
        all_modules[user_input-1] =input("Enter new module name > ")
        print(all_modules)
     else:
        break
    
##upate array with header
def update_header_array():
    modules_header[1]=all_modules[0]
    modules_header[2]=all_modules[1]
    modules_header[3]=all_modules[2]
    modules_header[4]=all_modules[3]
    
    
##create report close file    ##error handling if report doesnt exsist = create
    ##if exsists= overwriteit?
def create_report():
 try:
    result_file_name="C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\Report.csv"
    file_handler=open(result_file_name, "w")
    print(modules_header)
    for module in modules_header:
     file_handler.write(module+ "\n")
    file_handler.close()
 except:
        print("Error opening the file")
        exit()

def main():
    read_modules(file_path)

    organise_data()
   ##menu visible in terminal
    print("==============All modules===========")
    print(f" 1) {all_modules[0]} 2) {all_modules[1]} 3) {all_modules[2]} 4) {all_modules[3]}")
    print("======= You're editing modules =========")
    write_modules()
    update_header_array()
    create_report()

main()