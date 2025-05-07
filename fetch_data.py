import requests
import json

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Save to a file
    with open("countries_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print("Data fetched successfully!")
else:
    print("Failed to fetch data, status code:", response.status_code)
