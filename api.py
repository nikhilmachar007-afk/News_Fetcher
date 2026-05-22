import requests
from config import API_KEY, BASE_URL

def fetch_news(category, country, language):
    parameters={
        "apikey":API_KEY,
        "category":category,
        "country":country,
        "language":language
    }

    response=requests.get(BASE_URL,parameters)

    if response.status_code==200:
        json_results=response.json()
        return json_results["results"]
    else:
        print(f"Error: {response.status_code}")