#write to a file 

result_file_name= "C:\\Users\\VictoriaJuszkiewicz(\\Desktop\\results.txt"

file_handler= open(result_file_name, "w")
for i in range(1,10):
    file_handler.write(f"This is a test {i}")
    
file_handler.close()    