

import requests
import time

geonames_username = "alihasnain"

def get_coordinates(place, username=geonames_username, fuzzy=0, timeout=1):
    """This function gets a single set of coordinates from the geonames API."""
    time.sleep(timeout)  # Wait to avoid overloading the server
    url = "http://api.geonames.org/searchJSON?"
    params = {"q": place, "username": username, "fuzzy": fuzzy, "maxRows": 1, "isNameRequired": True}
    response = requests.get(url, params=params)
    results = response.json()

    try:
        result = results["geonames"][0]
        return {"latitude": result["lat"], "longitude": result["lng"]}
    except (IndexError, KeyError):
        return {"latitude": "NA", "longitude": "NA"}  # Return "NA" if no coordinates found

# get the place names from the tsv file
place = []

# reads the tsv file
with open("C:/Users/aienullah.beg/Downloads/FASDH25-portfolio2/ner_counts.tsv", 'r', encoding="utf-8") as file:
    lines = file.readlines()

header = lines[0].strip().split('\t')
place_index = header.index('Place')

# loop through the rest of lines
for line in lines[1:]:
    columns = line.strip().split('\t')
    if len(columns) > place_index:
        place.append(columns[place_index])

# get the coordinates
coordinates_data = []
for place_name in place:
    coordinates = get_coordinates(place_name)
    coordinates_data.append({'Place': place_name, 'Latitude': coordinates['latitude'], 'Longitude': coordinates['longitude']})

    # Print the coordinates of each place
    print(f"{place_name}: {coordinates['latitude']}, {coordinates['longitude']}")

# write coordinates to tsv file
filename = "NER_gazetteer.tsv"
with open(filename, 'w', encoding="utf-8") as file:
    file.write('Place\tLatitude\tLongitude\n')
    # Iterate through the list of dictionaries and write to the file
    for row in coordinates_data:
        file.write(f"{row['Place']}\t{row['Latitude']}\t{row['Longitude']}\n")

print("Coordinates written to NER_gazetteer.tsv")

from google.colab import files
uploaded = files.upload()
