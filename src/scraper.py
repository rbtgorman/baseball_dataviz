import pandas as pd

def fetch_fangraphs_park_factors(season=2024):
    url = f"https://www.fangraphs.com/guts.aspx?type=pf&season={season}&teamid=0&dh=0&sort=8,1&csv=1"
    df = pd.read_csv(url)
    return df

if __name__ == "__main__":
    df = fetch_fangraphs_park_factors(2024)
    print(df.head())
    df.to_csv("../data/park_factors.csv", index=False)

