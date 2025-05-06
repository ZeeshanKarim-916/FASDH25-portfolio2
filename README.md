
# FASDH25-portfolio2
A repository for students' portfolios for mini-project 2
##  Mini Project 2: Visualizing Place Names in News Articles
This mini project focuses on identifying and visualizing place names from a collection of Al Jazeera news articles about the Gaza war. Two techniques are used for extracting place names: Gazetteer with Regular Expressions (Regex) and Named Entity Recognition (NER). The aim is to track how place names are mentioned over time, visualize their frequency, and compare the accuracy and coverage of both methods.

## Project Directory Overview
FASDH25-portfolio2/
|
├── articles/                       # Contains article text files named by date and ID
|
├── gazetteers/
│   ├── geonames_gaza_selection.tsv   # TSV file with place names and alternate names
│   ├── countries/                    # Country-level gazetteers
│   └── readme/                       # Documentation related to gazetteers
|
├── Scripts/
│   ├── regex_script_final.py         # Python script for regex-based extraction
│   ├── Mapping_NER/                  # Scripts for mapping NER results
│   ├── maping regex/                 # Scripts related to regex mapping
│   ├── Gaza_NER2_Ali_Didar_Zeeshan/  # NER processing scripts by different contributors
│   └── build_gazetteer/              # Scripts for building gazetteers for NER
|
├── AI Documentations/
│   ├── AI_documentation_didar_ali.docx       # AI conversation documentation by Didar Ali
│   ├── AI_documentation_ali_hasnain.docx     # AI conversation documentation by Ali Hasnain
│   └── AI_documentation_Zeeshan.docx         # AI conversation documentation by Zeeshan
|
├── Outputs/
│   ├── regex_counts.tsv              # Monthly place name counts from regex extraction
│   ├── NER.gazetteers.tsv            # NER-based place name counts
|
├── Maps/
│   ├── regex_map.html                # Interactive map of regex results
│   ├── regex.map.png                 # Static image map of regex results
│   ├── NER.map.html                  # Interactive map of NER results
│   └── NER.map.png                   # Static image map of NER results
|
├── .gitignore                        # Git ignore file to exclude unnecessary files
└── readme.md                         # Project documentation (this file)

## Fork and Clone the Portfolio Folder

### Objective:
To set up a collaborative workspace by forking the main project repository and cloning it locally on our systems.

### Steps We Followed:
One group member forked the main portfolio repository from:
https://github.com/OpenITI/FASDH25-portfolio2

All other group members cloned this forked repository to their local machines by:
	Accessing the forked repository on GitHub.
	Clicking the green `Code` button and copying the HTTPS URL.
	Opening Git Bash / Terminal.
	Moving into the desired folder (e.g. `Downloads`) using:

cd Downloads
Cloning the repository using:  
git clone < Our repository_link>
This provided each group member with a local working copy synced to our group’s GitHub repository.


##  Task 2A: Use gazetteer and regex to extract places in Gaza from the corpus
In this task (2A), we work specifically on using a gazetteer and regex patterns to extract place names and their variant spellings from a text corpus. The process also includes comparing results from before and after the conflict began on October 7, 2023.
### Objective of Task 2A: Gazetteer and Regex-based Place Name Extraction
The goal is to:
	Use a gazetteer (a geographic dictionary) to identify place names in Gaza.
	Expand name recognition by including alternate spellings using regular expressions.
	Count the number of mentions per month in articles from October 7, 2023, onwards.
### Requirements
To run the script successfully, ensure you have:
#### Python and Libraries:
	 re – for regular expressions
	 os – for navigating directories
	 pandas – for data handling and TSV export
#### Git for Version Control:
	git add .
	git commit -m "message"
	git pull
	git push
### How the Script Works
#### Loading and Preparing Data
	The script begins by importing required libraries and defining a helper function write_tsv() to export output in a clean tabular format using pandas.
	It reads the geonames_gaza_selection.tsv gazetteer, extracting both primary names and alternate names from the 6th column.
	Whitespace is stripped, and a regex pattern is created for each place using | (OR operator) to match multiple variants. I used name variant in my code. 
	These patterns are stored in a dictionary for efficient matching.
#### Processing Articles
	The script loops through each file in the articles/ folder.
	Only articles dated October 7, 2023, or later are considered.
#### For each article:
	The date is extracted from the filename.
	The article content is read.
	All compiled regex patterns are used to match place names regardless of capitalization (IGNORECASE).
	Mentions are counted and stored in a dictionary by place name and month (YYYY-MM).
#### Generating Output
	The script prints a summary of how many times each place was mentioned by month.
	Results are stored as a list of tuples: (place_name, yyyy-mm, count).
	This list is exported using the write_tsv() function into a file named regex_counts.tsv. I saved this in our repository and then i pushed it to online repository GitHub. 
### Sanity Check After Execution
After running the script, I verified that:
	The output file regex_counts.tsv has correct and complete data.
	All expected place names are present (compare with gazetteer).
	Spelling variants were matched accurately (review and improve regex patterns as needed).


## 2B:Extract Place Names using Stanza

### Objective:
To apply Named Entity Recognition (NER) using Stanza and extract all place names from articles written specifically in January 2024.

### Process:
#### Created a copy of the class Colab notebook and renamed it:
Adapted the script to:
    Use the corpus folder inside our forked repository instead of the session folder.
    Apply a code to filter articles written in January 2024 based on their metadata.
    Extract only place names using Stanza’s NER pipeline.
    Count the frequency of each place name.

#### Cleaned the NER results:
    Identified and merged duplicate entries.
    For example:
    Added the count for `"Gaza's"` to `"Gaza"`.
    Removed unnecessary variants from the dictionary.

### Exported the cleaned data into a tab-separated values (TSV) file:
with columns: `placename` | `count`.
Downloaded the final notebook as a `.ipynb` file and added it to our repository.

### Exported the cleaned data into a tab-separated values (TSV) file:
with columns: `placename` | `count`.
Downloaded the final notebook as a `.ipynb` file and added it to our repository.


### Task 3: Create a gazetteer for the NER places
#### Geocoding Place Names from NER Output
This section of the project involved geocoding place names extracted using Named Entity Recognition (NER). The goal was to create a gazetteer file (`NER_gazetteer.tsv`) containing latitude and longitude coordinates for each place name found in the `ner_counts.tsv` file. Where no coordinates could be found through automated means, they were manually added.
#### Script Description
The script (`build_gazetteer.py`) performs the following tasks:
	Reads the `ner_counts.tsv` file and extracts all place names.
	Uses the GeoNames API to retrieve latitude and longitude coordinates.
	For place names where coordinates cannot be automatically retrieved, 'NA' is used.
	These NA values were then manually checked and coordinates were added manually using Google.
	The final gazetteer file is saved as `NER_gazetteer.tsv` inside the `gazetteer/` folder.

#### Place Names with Manually Added Coordinates
The following place names could not be resolved automatically and required manual coordinate lookup:
•	alDabshah
•	alTawil
•	alKhader
•	Africa4Palestine
•	RedSea
•	Houthis
•	IsraelPalestine
•	MirandaCleland
•	Netanyahu
•	Shujayea
•	alMazraa
•	Rmeish
•	zarahsultana
•	Margaliot
•	Mazzeh
•	Dabbouch
•	alSaftawi
•	Farhana
•	Abudaqa
•	AlAqsa
•	alFukhari
•	Benarasiyaa
•	SistanBaluchestan
•	alFawakhir
•	Balakhiyah
•	Ahmadiyyah Zawiya
•	majedalansari
•	Nairoukh
•	Shawawra
•	NaksBilal
•	Houthi
•	alAhli
•	Zawayda
•	Philadelphi
•	MoTaz
•	azaizamotaz9
•	AlFukhari
•	alKarama
•	October7
•	Dahiyeh
•	alArouri
•	carogennez
•	Thameen Darby
•	Nakba Layer
•	Mercator
•	AsiaPacific
•	QFFD
•	Jawwal
•	alNasser
•	alMawasi
•	alKatiba
•	RepJayapal
•	RepCori
•	BasedMikeLee
•	BosniaHerzegovina
•	Palestine_UN
•	adoniaayebare
•	Ansarallah
•	Hebrew
•	Supernova
•	Taalbaya
•	alWalaja
•	alMahatta
•	alMazraa Asharqiya
•	alMughraqa
•	alMaghazi
•	Bahaa
•	Pashias
•	alTanf
•	alJiftli
•	alShifa
•	Rawaa
#### Note on Filtering Non-Place Names
Some names in the `ner_counts.tsv` file were not valid place names (e.g., organizations, people, events, or hashtags). These were removed during the manual filtering process using spreadsheet filter options. Examples include: Africa4Palestine, Netanyahu, QFFD, October7, etc.

## Task 4A: Mapping Regex-Extracted Place Names

### Objective

In this task, I aimed to visualize the frequency of place names extracted using regular expressions. The extracted data was stored in `regex_counts.tsv`, and my goal was to map these place names using Plotly Express on an interactive, animated map — one frame for each month. Additionally, I saved both an interactive HTML version and a static PNG image of the map.

### Data Preparation

To begin with, I imported the place name frequency data from `regex_counts.tsv` and the coordinate data from the gazetteer file `geonames_gaza_selection.tsv`. I noticed that the place name column in the frequency data was labeled `placename`, while the gazetteer used `asciiname`. To make the merge possible, I renamed the `placename` column to `asciiname` in the counts DataFrame. After that, I merged both datasets on this common column to associate each place name with its geographic coordinates.

### Creating the Animated Map

For the animated map, I used Plotly Express’s `scatter_geo` function. I plotted each place using its latitude and longitude, and mapped the size and color of each point to the frequency of mentions (`count`). I animated the map using the `animation_frame` parameter set to the `month` column, allowing the viewer to see how mentions of different places changed over time.

I chose the "natural earth" projection because it gives a flat, clear view of the Gaza region without unnecessary distortion. I also customized the land and ocean colors — using light gray and light blue, respectively — to ensure the map was easy to read. The animated map was saved as `regex_map.html`.

####  I Chose This Visualization
I experimented with a few different color scales and projection types. After some testing, I chose the `Plasma` color scale because it shows a nice gradient between low and high values, making the frequency differences very clear. I also tried other projections but felt that "natural earth" best suited the geographic scale of this task.

The animation adds a temporal dimension that is very helpful — viewers can easily see how mentions change month by month, which wouldn’t be possible in a static format. That’s why I decided that animation was the most effective way to present this data.

### Creating the Static Map

In addition to the animated map, I created a static version using `scatter_map`. I customized the layout with the `carto-positron` background for a clean, high-contrast look. I also fine-tuned the map by adjusting features like coastlines, rivers, land, and ocean colors to make geographic elements clearer. This static map was saved as `regex_map.png`.

While this map doesn’t show changes over time, it’s still useful for quick insights or for use in presentations or reports where interactivity isn’t possible.

### Final Outputs

- `regex_map.html`: This is the interactive animated map showing monthly frequency of regex-extracted place names.
- `regex_map.png`: This is the static version of the map, useful for printed or static viewing formats.

##  4B. Map the NER-Extracted Placenames

### Objective:
To visualize the frequency of extracted place names on a map using Plotly Express and the corresponding coordinates from our gazetteer file.
### Process:
    Used the 'ner_counts.tsv' file created in Step 2.
    Referenced the 'NER_gazetteer.tsv' file containing the geographical coordinates for each place name.
    Plotted the data using 'Plotly Express' to create:
    An interactive HTML map:
    ner_map.html
    A static image map:
    ner_map.png

These visualizations provide an intuitive, spatial understanding of the distribution and frequency of places mentioned in the selected articles.

##  Finalizing the Portfolio Folder
To ensure our repository was clean, organized, and submission-ready, we finalized the following checklist:

### Required Files:
	`README.md` (this documentation)
	`regex_counts.tsv`
	`regex_script_final.py`
	`Gaza_NER2_<our_group_name>.ipynb`
	`NER_gazetteer.tsv`
	`build_gazetteer.py` (or `build_gazetteer.ipynb`)
	`regex_map.html`
	`regex_map.png`
	`ner_map.html`
	`ner_map.png`
	-`AI_documentation_<your_name>.docx` (for each group member)


## Advantages and Disadvantages of Regex and Gazetteer:
### Regex and Gazetteer Approach
#### Advantages:
One of the advantages of Regex is its high Precision. Regex when used with a gazetteer, is very helpful in accurately matching specific place names. This is very helpful for targeted regions (e.g., Gaza) where a list of cities, towns, and localities is available. Another advantage of Regex is its predictability and reliability. Since regex follows fixed rules, it always gives us the same results for the same input. This makes it great for tracking changes over time or comparing data across different periods. In addition, it is very quick and easy to use. It doesn’t need any heavy machine learning setups, it runs fast and  doesn’t need much computing power. It works in almost any programming environment.
#### Disadvantages:
Along with advantages, it has certain disadvantages as well. It is limited outside Gazetteers. It helps identify entities that are included in the list. It will not include any new or unexpected place names outside the list. Secondly, it usually misunderstood the Meaning of words. Regex works like a strict pattern-matcher. It doesn’t understand how a word is being used. So, if a news article like “Gaza has become a symbol of resistance,” regex might still identify “Gaza” as a location, even though it's being used more metaphorically. This can lead to results that seem accurate on the surface, but they usually miss the deeper meaning of the text. 
Finally, it can’t tell the difference between people and places. Regex doesn’t differentiate between people and places.  For example, if “Jordan” refers to a country or a person, it considers it a matching word and adds it to the list. We also figured it out in our project that it considers names like “Netanyahu” as the names of places. So, unless we manually clean the data or add extra rules, we might end up mixing up places with people, which might mess up our results.
 
### Named Entity Recognition (NER)
#### Advantages 
NER is a powerful tool, and it understands the context, unlike simple pattern matching.
NER is smart enough to figure out how a word is being used. It looks at the surrounding text to decide if something is a place, a person, or something else entirely. That means it’s much better at picking up on the meaning behind words and making more accurate guesses. Unlike regex, it can spot new or unfamiliar place names. 
One of the big advantages of NER is that it doesn’t rely on a fixed list. So even if a place name is rare, newly mentioned in the news, or completely unfamiliar, NER  can still catch it. This makes it great for scanning global content or fast-moving updates like breaking news. Finally, it can work well on bigger data. Once it is up and running, it can handle huge amounts of text, without much extra work from our side. This makes it a great option when we are dealing with large datasets or need to process lots of content quickly and efficiently.
#### Disadvantages
In contrast, it also has certain disadvantages. It doesn’t always work the same everywhere. NER models are usually trained in general types of text, so when we use them on more specialized content, like local news or conflict reports, they might not perform as well. To get better results, we need to retrain the model with examples from that specific kind of writing, which can be time-consuming and requires technical skills and labeled data. In addition to this, NER models, especially the advanced ones, are very powerful and resource-intensive. They need computing power to run like powerful servers or GPUs. For someone working with limited resources or on a smaller project, it can be very difficult. Finally, NER models often struggle with texts that are unstructured, informal, or messy, such as social media posts or field reports. This often leads to false positives.
## Image of final Maps
! [image(FASDH25-portfolio2/maps/regex_map.html)]
! [image(FASDH25-portfolio2/maps/ner_map.png)]
! [image(FASDH25-portfolio2/maps/ner_map.html)]
! [image(FASDH25-portfolio2/maps/regex_map.png)]

## Compare the January 2024 maps generated from the regex- and NER data
The two maps, one generated through Named Entity Recognition (NER) and the other via regex-based extraction, offer complementary but different perspectives on the geographic distribution of place mentions in January 2024.
The NER map presents a broad global view. It captures place names mentioned across various regions using machine learning techniques that rely on contextual understanding. This map shows a wide geographical spread, with notable concentrations in Europe, the Middle East, South Asia, and North America. The highest concentration of mentions appears in the Levant region, particularly around Gaza, which is highlighted with a bright yellow hotspot. This suggests that, in the source texts, Gaza and its surrounding areas were among the most frequently discussed places globally in January 2024. However, the NER approach tends to identify general place names such as countries or major cities and often lacks granularity when it comes to smaller or less prominent localities.
In contrast, the regex-based map takes a highly localized approach, focusing specifically on the Gaza Strip. It uses predefined patterns, and name lists to extract specific city and town names like Gaza, Rafah, Khan Younis, and others. This map reveals an extremely dense clustering of place mentions within the Gaza region, with much higher counts (color scale reaching over 4500) compared to the NER map. While this method excels at offering a fine-grained view of a particular region, it does not account for broader global mentions and is restricted to places included in the regex patterns. Its precision and specificity make it valuable for tracking localized narratives, especially in the context of conflicts or humanitarian crises.
Methodologically, the NER approach leverages the semantic context of language. It captures a wider array of mentions, including potentially novel or ambiguous place names. However, it may also result in false positives or overlooking obscure locations. The regex approach, by contrast, is rule-based and reliable for capturing predefined terms but lacks the flexibility to identify unexpected mentions or variations in spelling and grammar.
Concluding, the NER map offers a macro-level analysis, showing how Gaza features in a global discourse, while the regex map delivers a micro-level view. It emphasizes specific localities within Gaza. Together, they provide a fuller picture, one highlighting global attention and the other detailing the local specificity of that focus.

## Self-critical analysis
The project extracts and visualizes place names on map from news articles but there are few weaknesses and areas that could be improved if we had more time.
First, it’s the accuracy of the Regex method. This method sometimes matches wrong or non-related words because it’s working relies on pattern, not on the context. This often leads to false positives.
Secondly, the place names extracted using NER could not be geocoded directly. They had to be manually looked up and took a lot of time. Some names were not real places but names of institutions, people, organizations etc., were included in the NER results, they also had to be removed manually.
If we had more time these could have been done more efficiently with better and cleaner codes and more filtering of the data which would have eventually led better interactive maps.


