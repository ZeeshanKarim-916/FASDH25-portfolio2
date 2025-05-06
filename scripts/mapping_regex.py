# Import required libraries                      #codes taken from slide 10.1
import pandas as pd  # For data manipulation
import plotly.express as px  # For interactive visualizations
import kaleido  # For saving static images

# Load the gazetteer file with coordinates of places
coordinates_path = "../gazetteers/geonames_gaza_selection.tsv"
coordinates_df = pd.read_csv(coordinates_path, sep="\t") #codes taken from 10.1

# Load regex counts per place per month
counts_path = "../outputs/regex_counts.tsv"
counts_df = pd.read_csv(counts_path, sep="\t")

# Print the column names of both dataframes to check for compatibility
print("Coordinates DF Columns:", coordinates_df.columns)
print("Counts DF Columns:", counts_df.columns)

# Rename 'placename' to 'asciiname' in counts_df for consistency in merging
counts_df = counts_df.rename(columns={'placename': 'asciiname'})

# Merge the dataframes on the common 'asciiname' column
merge_df = pd.merge(coordinates_df, counts_df, on="asciiname")

# Check the merged dataframe to ensure the merge was successful
print(merge_df)

# 1. Create the animated map showing mentions per place over different months
fig = px.scatter_geo(merge_df, 
                     lat="latitude", 
                     lon="longitude", 
                     size="count", 
                     hover_name="asciiname", 
                     animation_frame="month", 
                     color="count", 
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
        rivercolor="deepskyblue",  # Changed river color to DeepskyBlue for clarity
        lonaxis=dict(range=[34.2, 34.6]),  # Focused longitude range around Gaza
    lataxis=dict(range=[31.2, 31.6])
    )
)
# Display the animated map
fig.show()

# Save the interactive animated map as an HTML file
fig.write_html("regex_map.html")


# 2. Create the static map (snapshot of the latest month) using the same data but without animation   #code help taken from slide 10.1
fig_static = px.scatter_map(merge_df, 
                            lat="latitude", 
                            lon="longitude", 
                            hover_name="asciiname", 
                            color="count", 
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
