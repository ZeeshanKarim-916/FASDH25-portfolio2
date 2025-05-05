# importing regular expressions to find text patterns
import re

# importing os to enable interaction with the file system 
import os

# for handling tabular data and exporting tsv
import pandas as pd



# function that writes a list of data rows into a tsv file using pandas 
def write_tsv(rows, column_list, path):
   
    #convert the list of rows into pandas DataFrame
    df = pd.DataFrame(rows, columns=column_list)
    
    # write the dataframe to tsv:
    df.to_csv(path, sep="\t", index=False)



# defining folder with text files to search for place names 
folder = "articles"  


# defining and loading the gazetteer from the tsv file, having place names and alternate names 
path = "gazetteers/geonames_gaza_selection.tsv"
# open and read the file
with open(path, encoding="utf-8") as file:
    data = file.read()

# building a dictionary to store regex patterns for each place (names and count matces)
patterns = {}

# spliting the gazetteer data into rows
rows = data.split("\n")

# start from second row to skip the header line in the gazetteer
for row in rows[1:]:
    columns = row.split("\t") # each column in tsv is separated by tabs 
    asciiname = columns[0] # first column has name for the place


    # skip rows that don't have at least 6 columns (to avoid processing error)    
    if len(columns) < 6:
        continue

    asciiname = columns[0]  # use ascii name of place as main reference
    # initialize the list with the place name
    name_variants = [asciiname]


    # get the alternate names from the 6th column which is counted as 5, if present
    alternate_names = columns[5].strip()

    
    if alternate_names:
        # spliting alternate names with a comma and getting list of name variants
        alternate_list = alternate_names.split(",")
        # looping through each alternate name in the list
        for alternate in alternate_list:
            # removinng whitspace from the alternate name
            alternate = alternate.strip()
            # adding alternate name to the list, if present 
            if alternate:
                name_variants.append(alternate)

    # escape special characters in each name variant so they don't break the regex
    name_variants = [re.escape(name) for name in name_variants]
    # create a pattern that will match any of the name variants in the text
    # word boundaries (\b) ensure we match full words only (not partial matches)
    regex_pattern = r"\b("+"|".join(name_variants) + r")\b"
    
    # store the pattern and set initial match count to 0 for this place
    # this will help us track how often the place is mentioned
    patterns[asciiname] = {"pattern": regex_pattern, "count":0}

    


# building dictionary which stores how many times each place name was mentioned per month 
mentions_per_month = {}

# setting the starting date of the war in Gaza to filter articles
war_start_date = "2023-10-07"

# loop through each file in the folder to check for place name mentions:
for filename in os.listdir(folder):
    # get the article's date from its filename (format is YYYY-MM-DD_)
    date_str = filename.split("_")[0]

    # only analyze articles from the start of the war onward
    if date_str < war_start_date:
        continue
    
    

# build the file path to the current articles:
    file_path = os.path.join(folder, filename)        

    # read the article content to search for place names
    with open(file_path, encoding="utf-8") as file:
        text = file.read()
        

    # loop through each place to search for matches in the text:
    for place in patterns:
        pattern = patterns[place]["pattern"] # get regex pattern for current place 
        matches = re.findall(pattern, text, re.IGNORECASE) # find all mentions, ignoring case 
        count = len(matches) # total mentions of the place in this article
        
        # add the number of times the place was found to the total frequency:
        patterns[place]["count"] += count
        
        # get the article’s month for grouping results
        month_str = date_str[:7]
        

        # initialize place and month in mentions_per_month dictionary if not done already
        if place not in mentions_per_month:
            # empty dictionary if place is not found
            mentions_per_month[place] = {}
        # prepare count for the month if not already there in the dictionary 
        if month_str not in mentions_per_month[place]:
            # if month is not found, place the month count to 0
            mentions_per_month[place][month_str] = 0

        # add the new matches on the place names to the number of times it was mentioned that month     
        mentions_per_month[place][month_str] += count
          


# print the final dictionary that shows how many times each place was mentioned each month

# loop through each place in the mentions_per-month dictionary
for place in mentions_per_month:
    if patterns[place]["count"] == 0:
        continue  # skip places with zero mentions

    print(f'"{place}": {{')
   
    # get the list of all months when this place names were mentioned
    month_list = list(mentions_per_month[place].keys())

    # loop through each month to print the corresponding mention count
    for month in month_list:
        count = mentions_per_month[place][month] # retrieve count for the current month

        # display the output with a comma unless it's the last month to keep formatting clean 
        if month != month_list[-1]:
            print(f'    "{month}": {count},')
        else:
            print(f'    "{month}": {count}')

    # close the dictionary block for this place and print the output
    print("},")

# prepare the data (mentions_per_month dictionary) as a list of rows for exporting to a file
rows = []

# loop through each place again to prepare structured data for export 
for place in mentions_per_month:
    if patterns[place]["count"] == 0:
        continue  # skip exporting places with zero mentions

    # loop through each month and find the number of times the place is mentioned 
    for month in mentions_per_month[place]:
        count = mentions_per_month[place][month]

        # Store the data in (place, month, count) format (rows list)
        rows.append((place, month, count))

# export the collected data to a TSV file for further analysis or sharing        
write_tsv(rows, ["placename","month", "count"], "regex_counts.tsv")
