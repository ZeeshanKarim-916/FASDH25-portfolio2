# Import required libraries
import pandas as pd  # For data manipulation
import plotly.express as px  # For interactive visualizations
import kaleido


# Load gazetteer file with coordinates of places
coordinates_path = "../gazetteers/geonames_gaza_selection.tsv"
coordinates_df = pd.read_csv(coordinates_path, sep="\t")

# Load regex counts per place per month
counts_path = "../outputs/regex_counts.tsv"
counts_df = pd.read_csv(counts_path, sep="\t")

print("Coordinates DF Columns:", coordinates_df.columns)
print("Counts DF Columns:", counts_df.columns)

# Rename 'placename' to 'asciiname' in counts_df
counts_df = counts_df.rename(columns={'placename': 'asciiname'})

# Now merge the dataframes
merge_df = pd.merge(coordinates_df, counts_df, on="asciiname")

# Check the merged dataframe
print(merge_df)

#merging the two dataframes on the common column "asciiname"
merge_df=pd.merge(coordinates_df, counts_df, on="asciiname")
print(merge_df)
## create a static map using frquency (count) as color
fig = px.scatter_map(merge_df, lat="latitude", lon="longitude", hover_name="asciiname", color="count", color_continuous_scale=px.colors.sequential.YlOrRd)
fig.update_layout(map_style="carto-darkmatter-nolabels")
fig.show()

# further customize the map with geographic features
fig.update_geos(
    projection_type="natural earth",
    fitbounds="locations",
    showcoastlines=True, coastlinecolor="RebeccaPurple",
    showland=True, landcolor="Green",
    showocean=True, oceancolor="LightBlue",
    showlakes=False, lakecolor="Blue",
    showrivers=True, rivercolor="Blue",
    showcountries=False, countrycolor="Brown"
)
# show the customized map 
fig.show()
# Save the static version of the map as PNG image
fig.write_image("regex_map.png", scale=2)

# create an animated map that shows mentions per place over different months
fig = px.scatter_geo(merge_df, lat="latitude", lon="longitude", size="count", hover_name="asciiname", animation_frame="month", color="count", color_continuous_scale=px.colors.sequential.YlOrRd,  projection="natural earth")

# customize the layout and appearance of the animated map
fig.update_layout(
    title="Regex Mentions Over Time",
    title_font_size=22,
    geo=dict(
        showland=True, landcolor="lightgreen",
        showocean=True, oceancolor="lightblue",
        showrivers=True, rivercolor="blue"
        )
    )
# show the animated map
fig.show()

# saves the interactive animated map as an  HTML file
fig.write_html("regex_map.html")
