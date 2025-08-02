import os

file2 = "File2.txt"
file = []

try:
    with open('file.txt','r') as file:
        for line in file:
          base = file.readlines()
        
        
        
    with open (file2,'w') as file:
        pass
            
        
except FileNotFoundError:
    print("Thats not a file")
except FileExistsError:
    print("File already exists")
    