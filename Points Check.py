import pandas as pd
from collections import Counter

# Load the CSV file
data = pd.read_csv("LongLat_KnownBurials.csv")

# Summarize the counts
count_summary = Counter(data['count'])
print("Counts Summary:", count_summary)