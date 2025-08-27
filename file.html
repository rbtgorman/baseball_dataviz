import requests
import pandas as pd

url = "https://www.ballparkpal.com/Park-Factors.php"

# Spoof a real browser (important to avoid 403)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
res = requests.get(url, headers=headers)
res.raise_for_status()

# Extract tables
tables = pd.read_html(res.text)

# The Park Factors table should be the first
df = tables[0]

print(df.head())
df.to_csv("park_factors.csv", index=False)

