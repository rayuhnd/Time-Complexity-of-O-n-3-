import os


def print_files(dir_path):  
    files = os.scandir(dir_path)   #Scans directory
    for file in files:
        if file.is_file() and not is_hidden(file): #Checks whether its a regular file
            print(file.name) #Prints file name
            

        elif file.is_dir() and not is_hidden(file):
            print_files(file.path) #Calls function again recursive
            print(file.name)
      

def is_hidden(entry): #function checking for hidden files
    dot = entry.name.startswith(".")
    underscore = entry.name.startswith("_")
    return dot or underscore
        
def main():
    
    dir_path = os.getcwd()  #Retrieves the directory 
    print_files(dir_path)    #Calls print_files function

main()  
