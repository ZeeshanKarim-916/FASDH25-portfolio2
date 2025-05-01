'''This is your starting script for today's Python class.

This script contains the code we wrote last week
to count the number of times each place in Gaza
is mentioned in our corpus.

Now, we want to store this count into a tsv file.

I have written a function (write csv) to do this -
but it has some mistakes in it.

Please fix the mistakes and call the function
to write the 

'''
import re
import os

# fix this function!

define write tsv(data)
    """This function converts a dictionary to a tsv file.

    It takes three arguments:
        data (dict): the dictionary
        column_list (list): a list of column names
        path (str): the path to which the tsv file will be written
    """
    import pandas as pd
    # turn the dictionary into a list of (key, value) tuples (this is correct):
    items = list(data.items())
    # create a dataframe from the items list (this is correct):
    df = pd.DataFrame.from_records(items, columns=column_list, index=False)
    # write the dataframe to tsv:
df.to_csv(path, sep="\t")
break


# define which folder to use:
# NB: these are different articles than in the previous weeks
folder = "aljazeera_articles"  

# define the patterns we want to search:

# load the gazetteer from the tsv file:
path = "gazetteers/geonames_gaza_selection.tsv"
with open(path, encoding="utf-8") as file:
    data = file.read()

# build a dictionary of patterns from the place names in the first column:
patterns = {}
rows = data.split("\n")
for row in rows[1:]:
    columns = row.split("\t")
    name = columns[0]
    patterns[name] = 0

# count the number of times each pattern is found in the entire folder:
for filename in os.listdir(folder):
    # build the file path:
    file_path = f"{folder}/{filename}"
    #print(f"The path to the article is: {file_path}")

    # load the article (text file) into Python:
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    # find all the occurences of the patterns in the text:
    for pattern in patterns:
        matches = re.findall(pattern, text)
        n_matches = len(matches)
        # add the number of times it was found to the total frequency:
        patterns[pattern] += n_matches

# print the frequency of each pattern:
for pattern in patterns:
    count = patterns[pattern]
    if count >= 1:
        print(f"found {pattern} {count} times")

# call the function to write your tsv file:
columns = ["asciiname", "frequency"]
tsv_filename = "frequencies.tsv"
