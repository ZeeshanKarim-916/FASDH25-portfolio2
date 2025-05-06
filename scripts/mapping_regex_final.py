# Import required libraries
import pandas as pd  # For data manipulation
import plotly.express as px  # For interactive visualizations
import kaleido

# Load the gazetteer file with coordinates of places
coordinates_path = "../gazetteers/NER_gazetteer.tsv"
coordinates_df = pd.read_csv(coordinates_path, sep="\t")

# Load regex counts per place per month
counts_path = "../outputs/ner_counts.tsv"
counts_df = pd.read_csv(counts_path, sep="\t")

# Print the column names of both dataframes to check for compatibility
print("Coordinates DF Columns:", coordinates_df.columns)
print("Counts DF Columns:", counts_df.columns)

#merging the two dataframes on the common column "asciiname"
merge_df=pd.merge(coordinates_df, counts_df, on="Place")

# Check the merged dataframe to ensure the merge was successful
print(merge_df)

# Convert Latitude and Longitude columns to numeric (if not already)
# The errors='coerce' argument converts problematic values to NaN
merge_df['Latitude'] = pd.to_numeric(merge_df['Latitude'], errors='coerce')
merge_df['Longitude'] = pd.to_numeric(merge_df['Longitude'], errors='coerce')

# Optional: Check for any NaN values after conversion

print(merge_df[merge_df['Latitude'].isnull() | merge_df['Longitude'].isnull()])


# 1. Create the animated map showing mentions per place over different months
fig = px.scatter_geo(merge_df, 
                     lat="Latitude", 
                     lon="Longitude", 
                     size="Count", 
                     hover_name="Place",  
                     color="Count", 
                     color_continuous_scale=px.colors.sequential.Plasma,  # Color scale
                     projection="natural earth")  # Flat map

# Customize the layout and appearance of the animated map
fig.update_layout(
    title="Regex Mentions Over Time",  # Added title to the map
    title_font_size=22,  # Increased font size for title
    geo=dict(
        showland=True, 
        landcolor="lightgray",  # Lighter land color for contrast
        showocean=True, 
        oceancolor="lightblue",  # Light blue for ocean
        showrivers=True, 
        rivercolor="deepskyblue"  # Changed river color to DeepskyBlue for clarity
    )
)

# Display the animated map
fig.show()

# Save the interactive animated map as an HTML file
fig.write_html("regex_map.html")


# 2. Create the static map (snapshot of the latest month) using the same data but without animation
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

# Show the customized static map with the new settings
fig_static.show()

# Save the static version of the map as a PNG image
fig_static.write_image("regex_map.png", scale=2)  # Higher scale for better resolution
