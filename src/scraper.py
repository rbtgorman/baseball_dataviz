import requests
import pandas as pd

def fetch_park_factors():
    url = "https://www.ballparkpal.com/Park-Factors.php"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()

    tables = pd.read_html(res.text)
    df = tables[0]
    return df

if __name__ == "__main__":
    df = fetch_park_factors()
    df.to_csv("../data/park_factors.csv", index=False)
    print("✅ Park factors saved to data/park_factors.csv")
