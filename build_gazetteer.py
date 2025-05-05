import requests   #makes API requsts
import time    #adds delays between requests

geonames_username = "alihasnain"  # my Geonames API username

def get_coordinates(place, username=geonames_username, fuzzy=0, timeout=1):
    """This function gets a single set of coordinates from the geonames API."""
    time.sleep(timeout)  #Delay to avoid overload
    url = "http://api.geonames.org/searchJSON?"  #API URL
    params = {"q": place, "username": username, "fuzzy": fuzzy, "maxRows": 1, "isNameRequired": True}
    response = requests.get(url, params=params)  #Request data from API
    results = response.json()  #Convert response to JSON

    try:
        result = results["geonames"][0]  #try to get the first result
        return {"latitude": result["lat"], "longitude": result["lng"]}   #return coordinates
    except (IndexError, KeyError):  #if no result or key is missing
        return {"latitude": "NA", "longitude": "NA"}  #Return "NA" if no coordinates found

place = [] #Empty list to store place names

#Open the tsv file and read its content
with open("C:/Users/aienullah.beg/Downloads/FASDH25-portfolio2/ner_counts.tsv", 'r', encoding="utf-8") as file:
    lines = file.readlines()  #Read all the lines into a list

header = lines[0].strip().split('\t') # Get header columns
place_index = header.index('Place')  #Find index of "Place" column

#loop through the remaining lines
for line in lines[1:]:  #Loop through data lines
    columns = line.strip().split('\t')  #Split line by tabs
    if len(columns) > place_index:   #Check if place column exists
        place.append(columns[place_index])  #Add place to list

# Go through each place name and get coordinates
coordinates_data = []  #list to store coordinates data
for place_name in place:  #Loop through place names
    coordinates = get_coordinates(place_name) #Get coordinates
    coordinates_data.append({'Place': place_name, 'Latitude': coordinates['latitude'], 'Longitude': coordinates['longitude']})   #Add the result to the list
  
    print(f"{place_name}: {coordinates['latitude']}, {coordinates['longitude']}")  #Print coordinates

filename = "NER_gazetteer.tsv"   #output file name

#write the coordinates to new TSV file
with open(filename, 'w', encoding="utf-8") as file:
    file.write('Place\tLatitude\tLongitude\n') #write header
    for row in coordinates_data:  #write data rows
        file.write(f"{row['Place']}\t{row['Latitude']}\t{row['Longitude']}\n")  #write each row

print("Coordinates written to NER_gazetteer.tsv")  #confirm saving
