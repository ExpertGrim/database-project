

file2 = "File2.txt" #creating a variable for the output file
data = []

try:
    with open('file.txt','r',encoding='utf-8') as file:
        header = file.readline().strip().split(",") #to take the header from the top of the file
        rows = [dict(zip(header, line.strip().split(","))) for line in file]# this is to take the header and than make rows for each data to make it easily accesbile in a dictionary set
    #print(rows)
        
    with open (file2,'w') as file: #to create the file where the answers are 
        file.write("Question a: \n ")
        for row in rows:
            country = row['CountryName']
            if country.endswith("a"):
                file.write(f"{country},")
        citypop = [] 
        for row in rows:
            if 'CityPopulation' in row:
                pop = int(row['CityPopulation'])
                citypop.append(pop)
        print(citypop)
        city5 = sorted(citypop, reverse=True)[:5]
        file.write("\n\nQuestion b: \n " + str(city5))

                  
                
         
            
        
except FileNotFoundError:
    print("Thats not a file")
except FileExistsError:
    print("File already exists")
    