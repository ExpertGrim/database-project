

file2 = "File2.txt" #creating a variable for the output file
file = []

try:
    with open('file.txt','r',encoding='utf-8') as file:
        for line in file:
          base = file.readlines()
        
        
        
    with open (file2,'w') as file:
        pass
            
        
except FileNotFoundError:
    print("Thats not a file")
except FileExistsError:
    print("File already exists")
    