# Script to get user marks
import os
import CSV_files
learner_file = "C:\\Users\\TomTaylor(TallaghtTC\\Desktop\\learners.csv"
module_file = "C:\\Users\\TomTaylor(TallaghtTC\\Desktop\\modules.csv"
results_file = "C:\\Users\\TomTaylor(TallaghtTC\\Desktop\\results.csv"
learners = []
modules = []
results = []
# Read the Modules file id it exists
if os.path.exists(module_file):
    module_file_lines = CSV_files.read_file_lines(module_file)
    modules = CSV_files.parse_file_lines(module_file_lines)
    #print(f"Modules = {modules}")

if os.path.exists(learner_file):
    learner_file_lines = CSV_files.read_file_lines(learner_file)
    learners = CSV_files.parse_file_lines(learner_file_lines)

# for each learner - ask the results for each module90

results_header = f"Firstname,Lastname,age,{modules[0]},{modules[1]},{modules[2]},{modules[3]}"

for learner in learners:
    os.system("cls")
    learner_fields = learner.split(",")
    print(f"== Results for : {learner_fields[0]}")
    result = str(learner)
    for module in modules:
        marks = int(input (f"Enter results for {module} >"))
        result += "," + str(marks)
    results.append (result)
    
result_file_lines = CSV_files.create_file_lines(results, results_header)
CSV_files.write_file_lines(results_file,result_file_lines)
