import pandas as pd


data = {
    "Country": [
        "United States",
        "China",
        "India",
        "Japan",
        "Germany",
        "UK",
        "France",
        "Brazil",
        "Italy",
        "Canada",
    ],
    "Population_Millions": [
        331.0,
        1412.0,
        1380.0,
        125.8,
        83.2,
        67.2,
        67.4,
        212.6,
        59.5,
        38.0,
    ],
    "GDP_Per_Capita_USD": [
        65280,
        10500,
        1900,
        40250,
        46260,
        42330,
        40490,
        6790,
        31720,
        46190,
    ],
}


df = pd.DataFrame(data)


df.to_csv("country_data.csv")

print("CSV file 'country_data.csv' created")
