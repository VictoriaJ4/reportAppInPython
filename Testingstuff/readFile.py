#Read the file in function

def read_file():
    file_path= "C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\results.txt"
    file_text= open(file_path, "r")
    data_lines= file_text.readlines()
    file_text.close()

    for i in range(len(data_lines)):
     print(data_lines[i].strip())

def main():
    read_file()

main()