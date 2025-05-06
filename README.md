# FASDH25-portfolio2
A repository for students' portfolios for mini-project 2
#  Mini Project 2: Visualizing Place Names in News Articles
This mini project focuses on identifying and visualizing place names from a collection of Al Jazeera news articles about the Gaza war. Two techniques are used for extracting place names: Gazetteer with Regular Expressions (Regex) and Named Entity Recognition (NER). The aim is to track how place names are mentioned over time, visualize their frequency, and compare the accuracy and coverage of both methods.

#  Task 2A: Use gazetteer and regex to extract places in Gaza from the corpus
In this task (2A), we work specifically on using a gazetteer and regex patterns to extract place names and their variant spellings from a text corpus. The process also includes comparing results from before and after the conflict began on October 7, 2023.
## Objective of Task 2A: Gazetteer and Regex-based Place Name Extraction
The goal is to:
	Use a gazetteer (a geographic dictionary) to identify place names in Gaza.
	Expand name recognition by including alternate spellings using regular expressions.
	Count the number of mentions per month in articles from October 7, 2023, onwards.
## Project Directory Overview
FASDH25-portfolio2/
│
├── articles/                     # Contains article text files named by date and ID
│
├── gazetteers/
│   ├── geonames_gaza_selection.tsv  # TSV file with place names and alternate names
│   ├── countries/                   # Additional country-level gazetteers
│   ├── NER gazetteer/              # Gazetteer used for NER comparisons
│   └── readme/
│
├── Scripts/
│   ├── regex_script_final.py       # Python script to perform regex extraction
│   └── regex_counts.tsv            # Output file with monthly place name counts
│
├── .gitignore
├── build_gazetteer/
├── frequencies/
├── NER counts/
└── readme.md
## Requirements
To run the script successfully, ensure you have:
### Python and Libraries:
	 re – for regular expressions
	 os – for navigating directories
	 pandas – for data handling and TSV export
## Git for Version Control:
	git add .
	git commit -m "message"
	git pull
	git push
## How the Script Works
### Loading and Preparing Data
	The script begins by importing required libraries and defining a helper function write_tsv() to export output in a clean tabular format using pandas.
	It reads the geonames_gaza_selection.tsv gazetteer, extracting both primary names and alternate names from the 6th column.
	Whitespace is stripped, and a regex pattern is created for each place using | (OR operator) to match multiple variants. I used name variant in my code. 
	These patterns are stored in a dictionary for efficient matching.
### Processing Articles
	The script loops through each file in the articles/ folder.
	Only articles dated October 7, 2023, or later are considered.
#### For each article:
	The date is extracted from the filename.
	The article content is read.
	All compiled regex patterns are used to match place names regardless of capitalization (IGNORECASE).
	Mentions are counted and stored in a dictionary by place name and month (YYYY-MM).
### Generating Output
	The script prints a summary of how many times each place was mentioned by month.
	Results are stored as a list of tuples: (place_name, yyyy-mm, count).
	This list is exported using the write_tsv() function into a file named regex_counts.tsv. I saved this in our repository and then i pushed it to online repository GitHub. 
## Sanity Check After Execution
After running the script, I verified that:
	The output file regex_counts.tsv has correct and complete data.
	All expected place names are present (compare with gazetteer).
	Spelling variants were matched accurately (review and improve regex patterns as needed).

## Task 3: Create a gazetteer for the NER places
### Geocoding Place Names from NER Output
This section of the project involved geocoding place names extracted using Named Entity Recognition (NER). The goal was to create a gazetteer file (`NER_gazetteer.tsv`) containing latitude and longitude coordinates for each place name found in the `ner_counts.tsv` file. Where no coordinates could be found through automated means, they were manually added.
### Script Description
The script (`build_gazetteer.py`) performs the following tasks:
	Reads the `ner_counts.tsv` file and extracts all place names.
	Uses the GeoNames API to retrieve latitude and longitude coordinates.
	For place names where coordinates cannot be automatically retrieved, 'NA' is used.
	These NA values were then manually checked and coordinates were added manually using Google.
	The final gazetteer file is saved as `NER_gazetteer.tsv` inside the `gazetteer/` folder.

### Place Names with Manually Added Coordinates
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
### Note on Filtering Non-Place Names
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
