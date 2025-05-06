import pandas as pd  # For data manipulation   #code taken from slide 10.1
import plotly.express as px  # For interactive visualizations
import kaleido  # For saving figures as images

# Load the gazetteer file with coordinates of places
coordinates_path = "C:/Users/Admin/Downloads/FASDH25-portfolio2/gazetteers/NER_gazetteer.tsv"
coordinates_df = pd.read_csv(coordinates_path, sep="\t")  #code taken from slide 10.1

# Load NER counts for January 2024 (ner_counts.tsv)
counts_path = "C:/Users/Admin/Downloads/FASDH25-portfolio2/outputs/ner_counts.tsv"
counts_df = pd.read_csv(counts_path, sep="\t")  #code taken from slides 10.1

# Inspect the columns and first few rows to understand the structure
print(counts_df.columns)
print(counts_df.head())

# Check if there's a date column and extract month if it exists
if 'date' in counts_df.columns:
    counts_df['date'] = pd.to_datetime(counts_df['date'], errors='coerce')  # Convert to datetime format
    counts_df['month'] = counts_df['date'].dt.to_period('M')  # Extract month as 'YYYY-MM'
    counts_jan_2024 = counts_df[counts_df['month'] == "2024-01"]
else:
    # If there's no date column, we may proceed with all data, assuming it already corresponds to January 2024
    counts_jan_2024 = counts_df

# Merge the two dataframes on the common column "Place"
merge_df = pd.merge(coordinates_df, counts_jan_2024, on="Place")

# Convert Latitude and Longitude columns to numeric (if not already)   #Code taken from slides 10.1
merge_df['Latitude'] = pd.to_numeric(merge_df['Latitude'], errors='coerce')
merge_df['Longitude'] = pd.to_numeric(merge_df['Longitude'], errors='coerce')

# Create the map showing mentions per place for January 2024 # Code help taken from slides 10.1
fig = px.scatter_geo(merge_df, 
                     lat="Latitude", 
                     lon="Longitude", 
                     size="Count",  # Size of the markers corresponds to frequency
                     hover_name="Place",  # Hover text shows place name
                     color="Count",  # Color intensity corresponds to frequency
                     color_continuous_scale=px.colors.sequential.Plasma,  # Color scale
                     projection="natural earth")  # Flat map

# Customize the layout and appearance of the map
fig.update_layout(
    title="NER Extracted Place Names in January 2024",  # Title of the map
    title_font_size=22,  # Font size for the title
    geo=dict(
        showland=True, 
        landcolor="lightgray",  # Lighter land color for contrast
        showocean=True, 
        oceancolor="lightblue",  # Light blue for ocean
        showrivers=True, 
        rivercolor="deepskyblue"  # Changed river color to DeepskyBlue for clarity
    )
)

# Display the interactive map
fig.show()

# Save the interactive map as an HTML file
fig.write_html("ner_map.html")

# Create a static map (snapshot of the NER data for January 2024) # code taken from slide 10.1
fig_static = px.scatter_map(merge_df, 
                            lat="Latitude", 
                            lon="Longitude", 
                            hover_name="Place", 
                            color="Count", 
                            color_continuous_scale=px.colors.sequential.Plasma)  # Color scale

# Customize the map layout with a light background style
fig_static.update_layout(map_style="carto-positron")  # Light background for better contrast

# Further customize the map with geographic features
fig_static.update_geos(
    projection_type="natural earth",  # Flat "natural earth" projection
    fitbounds="locations", 
    showcoastlines=True, coastlinecolor="DarkRed",  # Coastline color
    showland=True, landcolor="DarkGreen",  # Land color
    showocean=True, oceancolor="LightSeaGreen",  # Ocean color
    showlakes=False, lakecolor="RoyalBlue",  # Lakes hidden
    showrivers=True, rivercolor="RoyalBlue",  # River color
    showcountries=False, countrycolor="DarkSlateGray"  # Disabled country borders
)

# Show the static map with the new settings
fig_static.show()

# Save the static map as a PNG image
fig_static.write_image("ner_map.png", scale=2)  # Higher scale for better resolution
