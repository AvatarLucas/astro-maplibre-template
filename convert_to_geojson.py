import csv
import geojson
from shapely.geometry import Point, mapping

def csv_to_geojson(input_csv, output_geojson):
    features = []
    with open(input_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lng = float(row['lng'])
            lat = float(row['lat'])
            # Create a point geometry for each row
            point = Point(lng, lat)
            feature = geojson.Feature(geometry=mapping(point), properties={})
            features.append(feature)

    # Create a FeatureCollection
    feature_collection = geojson.FeatureCollection(features)

    # Write to the GeoJSON output file
    with open(output_geojson, 'w') as geojsonfile:
        geojson.dump(feature_collection, geojsonfile, indent=2)

# Input CSV and output GeoJSON file paths
csv_file = "LongLat_KnownBurials.csv"
output_file = "hexagon-data.geojson"

# Convert CSV to GeoJSON
csv_to_geojson(csv_file, output_file)
print(f"GeoJSON file created at {output_file}")