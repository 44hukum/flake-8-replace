import subprocess
import linecache
import re
import os

for path, subdirs, files in os.walk('./app/'):
    for name in files:
        if re.search('(pyc\Z)', name) is None:
            filename= os.path.join(path, name)
            output=subprocess.run(["flake8",filename], capture_output=True)
            # read file
            with open(filename, 'r+') as file:
                data = file.readlines()
            for error in list(filter(None, str(output.stdout, 'UTF-8').split("\n"))):
                file, message = tuple(error.split(": ")) # for future deduction
                line_number =int(re.findall(r'[0-9]{1,3}', file)[0])
                refined_data=re.sub('"',"'",linecache.getline(filename, line_number)) # replaced double quotes with single quotes
                data[line_number-1] = refined_data
                print("Removed: ", refined_data, line_number-1)
            
            # write file
            with open(filename, 'w+') as file:
                file.truncate()
                file.writelines(data)