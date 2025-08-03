

file2 = "File2.txt" #creating a variable for the output file
data = []

try:
    with open('file.txt','r',encoding='utf-8-sig') as file:
        header = file.readline().strip().split(",") #to take the header from the top of the file
        rows = [dict(zip(header, line.strip().split(","))) for line in file]# this is to take the header and than make rows for each data to make it easily accesbile in a dictionary set
    #print(rows)
        
    with open (file2,'w' , encoding='utf-8-sig') as file: #to create the file where the answers are 
       
        file.write("Question a: \n ")
        for row in rows:
            country = row['CountryName'] # calls to dictionary rows to find the header CountryName
            if country.endswith("a"):  #searchs through the dictionary for countrys that end with a 
                file.write(f"{country},")
                
        citypop = set() #empty list to hold the population nuumbers
        for row in rows:
            if 'CityPopulation' in row and 'CityName' in row : #Calls the header directly in dictionary
                cityN = row['CityName']
                pop = int(row['CityPopulation'])#Converts the string in the dictionary into integers
                citypop.add((cityN,pop))
        # sorts the list citypop and then reverse the order to ensure the largest numbers are on top and then pulls the top 5
        city5 = sorted(citypop,key=lambda x: x[1] , reverse=True)[:5]
        file.write("\n\nQuestion b: \n " + str(city5))
        
        landMass = set() #empty list to hold the population nuumbers
        for row in rows:
            if 'LandMass' in row and 'CityName' in row : #Calls the header directly in dictionary
                cityN = row['CityName']
                Land = int(row['LandMass'])#Converts the string in the dictionary into integers
                landMass.add((cityN,Land))
        land5 = sorted(landMass,key=lambda y: y[1], reverse=True)[:5]
        file.write("\n\nQuestion c: \n" + str(land5) ) 
         
            
        
except FileNotFoundError:
    print("Thats not a file")
except FileExistsError:
    print("File already exists")
    