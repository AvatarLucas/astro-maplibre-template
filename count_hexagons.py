import json

# Load the GeoJSON file
file_path = "hexagon-data.geojson"  # Update the path if needed
with open(file_path, "r") as file:
    geojson_data = json.load(file)

# Count the number of features (hexagons)
num_hexagons = len(geojson_data["features"])
print(f"Number of hexagons: {num_hexagons}")