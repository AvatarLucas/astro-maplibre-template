import json

# Load the GeoJSON file
with open("cemetery_polygons.geojson", "r") as file:
    data = json.load(file)

# Correct the structure of each feature
for feature in data["features"]:
    # Ensure 'id' is moved from properties to the top level
    feature["id"] = feature["properties"].pop("id", None)

# Save the updated GeoJSON file
with open("cemetery_polygons_corrected.geojson", "w") as file:
    json.dump(data, file, indent=4)

print("GeoJSON successfully updated: 'id' moved to the top level.")
