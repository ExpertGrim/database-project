

file2 = "File2.txt" #creating a variable for the output file

try:
    with open('file.txt','r',encoding='utf-8-sig') as file:
        header = file.readline().strip().split(",") #to take the header from the top of the file
        rows = [dict(zip(header, line.strip().split(","))) for line in file]# this is to take the header and than make rows for each data to make it easily accesbile in a dictionary set
    #print(rows)
        
    with open (file2,'w' , encoding='utf-8-sig') as file: #to create the file where the answers are 
        file.write("Question a: \n ")
        def question_A(rows):
            countryset = set() #empty set to hold the country names
            for row in rows:
                country = row['CountryName'] # calls to dictionary rows to find the header CountryName
                if country.endswith('a'):  # searches through the dictionary for countries that end with a
                    countryset.add(country) #adds the country to the set if it ends with a
            file.write(f"Total countries ending with 'a': {len(countryset)}") #writes the total number of countries ending with a to the file
            return len(countryset) #returns the total number of countries ending with a
        question_A(rows) #function call
        
                
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
            if 'LandMass' in row and 'CountryName' in row : #Calls the header directly in dictionary
                try:
                    countryN = row['CountryName']
                    Land = int(row['LandMass'])#Converts the string in the dictionary into integers
                    landMass.add((countryN,Land))
                except ValueError:
                    continue    
        land5 = sorted(landMass,key=lambda y: y[1], reverse=True)[:5]
        file.write("\n\nQuestion c: \n" + str(land5) ) 
        
        # d) Countries with independence year between 1960-1980

        #Thando: This code counts the number of countries that have independence year between 1960 and 1980, then shows the total of thos countries in File2
        def question_d(rows):
            uniqueSet = set()
            count_indep = 0
            for row in rows:
                if 'IndepYear' in row and 'CountryName' in row:
                    try:
                        Year = int(row['IndepYear'])
                        if 1960 <= Year <= 1980:
                            if row['CountryName'] not in uniqueSet: #To avoid counting the same country multiple times
                                uniqueSet.add(row['CountryName']) # Add country name to the set
                                count_indep += 1
                    except ValueError:
                        #Skip invalid entries like 'NULL' or non-numeric values
                        continue
            file.write("\n\nQuestion d: \n" + str(count_indep) )
            return count_indep
        question_d(rows)
        
         # e) Countries with independence year between 1830-1850
        countries_indep = set()
        for row in rows:
            if 'IndepYear' in row and 'CountryName' in row:
                try:
                    Years = int(row['IndepYear'])
                    if 1830 <= Years <= 1850:
                        # Add county name to the list
                        countries_indep.add(row['CountryName'])
                except ValueError:
                    #Skip invalid entries like 'NULL' or non-numeric values
                    continue
        file.write("\n\nQuestion e: \n" + str(countries_indep))
        
         # f) Top 5 African countries by life expectancy
        African = set()
        for row in rows:
                Cont = row['Continent']
                if Cont == "Africa":
                    life = float(row['LifeExpectancy'])
                    Country = row['CountryName']
                    African.add((Country,life))
        Afri5 = sorted(African,key=lambda z: z[1], reverse=True)[:5]
        file.write("\n\nQuestion f: \n " + str(Afri5))  
             
        #Question g:
        def question_g(rows):
            lang_count = {}
            for row in rows:
                if 'Language' in row:
                    try:
                        langs = [lang.strip() for lang in row['Language'].split(',')]
                        for lang in langs:
                            if lang: #Ensure the language string is not empty
                                lang_count[lang] = lang_count.get(lang, 0) + 1
                    except AttributeError:
                        #Handle cases where 'Language' is unexpected (e.g., a non-string type)
                        continue
            #Sort languages by count in descending order and select the top 5
            sorted_langs = sorted(lang_count.items(), key=lambda x: x[1], reverse=True)
            top5_langs = [lang for lang, count in sorted_langs[:5]]
            file.write("\n\nQuestion g: \n" + str(top5_langs))
            return top5_langs
        question_g(rows) #function call
            
        
        #Question h:
        Base = set()
        for row in rows:
            country = row['CountryName'] # calls to dictionary rows to find the header CountryName
            if country.endswith("a"):  #searchs through the dictionary for countrys that end with a 
                Base.add(country)
        file.write("\n\nQuestion h: \n" + str(Base))
                
         
         
            
        
except FileNotFoundError:
    print("Thats not a file")
except FileExistsError:
    print("File already exists")
    