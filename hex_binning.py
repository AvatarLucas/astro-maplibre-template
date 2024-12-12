import pandas as pd
import geojson
import h3

# Step 1: Load your CSV file
data = pd.read_csv("LongLat_KnownBurials.csv")  # Replace with your actual CSV file
points = list(zip(data['lat'], data['lng']))  # Ensure columns are named 'lat' and 'lng'

# Step 2: Define resolution for hexagons
resolution = 13  # Adjust based on the required granularity (~4.2m hexagons)

# Step 3: Create hexagons for all points
data['hexagon'] = data.apply(lambda row: h3.latlng_to_cell(row['lat'], row['lng'], resolution), axis=1)

# Step 4: Count points in each hexagon
hex_counts = data['hexagon'].value_counts().reset_index()
hex_counts.columns = ['hexagon', 'count']

# Step 5: Generate GeoJSON features for each hexagon
features = []
for hex_id, count in zip(hex_counts['hexagon'], hex_counts['count']):
    # Get the hexagon boundary
    hex_boundary = h3.cell_to_boundary(hex_id)  # Returns list of (lat, lng) pairs
    # Convert to GeoJSON format (list of [lng, lat])
    geojson_boundary = [[lng, lat] for lat, lng in hex_boundary]
    # Close the polygon (GeoJSON requires the first and last coordinates to be the same)
    geojson_boundary.append(geojson_boundary[0])
    features.append(
        geojson.Feature(
            geometry=geojson.Polygon([geojson_boundary]),
            properties={"count": count}
        )
    )

# Step 6: Create GeoJSON FeatureCollection
feature_collection = geojson.FeatureCollection(features)

# Step 7: Save GeoJSON file
output_file = "hexagon-data.geojson"
with open(output_file, "w") as f:
    geojson.dump(feature_collection, f)

print(f"GeoJSON file created: {output_file}")
