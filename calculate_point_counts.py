import pandas as pd
import geojson
from shapely.geometry import Point
from shapely.strtree import STRtree

# Load CSV file
data = pd.read_csv("LongLat_KnownBurials.csv")

# Create Shapely Point objects for each row
points = [Point(row['lng'], row['lat']) for _, row in data.iterrows()]

# Use an STRtree for spatial indexing
tree = STRtree(points)

# Define a radius (1 meter in degrees; approximate conversion)
radius_degrees = 1 / 111_139  # Convert meters to degrees

# Count neighbors within the radius for each point
counts = []
for point in points:
    neighbors = tree.query(point.buffer(radius_degrees))  # Points within the radius
    counts.append(len(neighbors))

# Add the counts to the data
data['count'] = counts

# Create GeoJSON features
features = []
for _, row in data.iterrows():
    features.append(
        geojson.Feature(
            geometry=geojson.Point((row['lng'], row['lat'])),
            properties={"count": row['count']}
        )
    )

# Create GeoJSON FeatureCollection
feature_collection = geojson.FeatureCollection(features)

# Save to a GeoJSON file
output_file = "hexagon-data.geojson"
with open(output_file, "w") as f:
    geojson.dump(feature_collection, f)

print(f"GeoJSON file created with counts: {output_file}")