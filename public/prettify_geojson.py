import json

# Input and output file paths
input_file = "hexagon-data.geojson"
output_file = "hexagon-data-pretty.geojson"

# Read the existing GeoJSON file
with open(input_file, "r") as file:
    data = json.load(file)

# Write the prettified JSON to a new file
with open(output_file, "w") as file:
    json.dump(data, file, indent=2)

print(f"Prettified GeoJSON saved to {output_file}")