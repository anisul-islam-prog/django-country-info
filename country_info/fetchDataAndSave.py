import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "country_info.settings")  # Adjust project name
django.setup()

from countries.models import Country
import requests

def fetch_and_store_data():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)

    if response.status_code == 200:
        countries = response.json()

        for country in countries:
            Country.objects.create(
                name=country.get("name", {}),
                cca2=country.get("cca2", ""),
                cca3=country.get("cca3", ""),
                ccn3=country.get("ccn3", ""),
                independent=country.get("independent", False),
                status=country.get("status", ""),
                unMember=country.get("unMember", False),
                currencies=country.get("currencies", {}),
                capital=country.get("capital", []),
                region=country.get("region", ""),
                subregion=country.get("subregion", ""),
                languages=country.get("languages", {}),
                translations=country.get("translations", {}),
                latlng=country.get("latlng", []),
                landlocked=country.get("landlocked", False),
                borders=country.get("borders", []),
                area=country.get("area", 0),
                demonyms=country.get("demonyms", {}),
                flag=country.get("flag", ""),
                maps=country.get("maps", {}),
                population=country.get("population", 0),
                gini=country.get("gini", {}),
                timezones=country.get("timezones", []),
                continents=country.get("continents", []),
                flags=country.get("flags", {}),
                coatOfArms=country.get("coatOfArms", {}),
                startOfWeek=country.get("startOfWeek", ""),
                capitalInfo=country.get("capitalInfo", {}),
                postalCode=country.get("postalCode", {})
            )
        print("All country data stored successfully!")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    fetch_and_store_data()