from api import fetch_news
from config import COUNTRIES, LANGUAGES


print("---------------------NEWS FETCHER---------------------")
print("Fetch news according to Category, Country and Language")
print("======================================================")
while True:
    try:
        category=input("Category (eg: sports/business/technology..): ").strip().lower()
        country=input("Country (eg: india/US/france..): ").strip().lower()
        language=input("Language (eg: english/hindi/kannada..): ").strip().lower()
        news=fetch_news(category,COUNTRIES[country],LANGUAGES[language])
        break
    except KeyError:
        print("===========================================================================")
        print("\nInvalid input. Please enter valid input as demonstrated through examples.\n")
        print("===========================================================================")
        continue

print("\n---------------EXCLUSIVE NEWS HEADLINES---------------")
print("\n"+"="*90+"\n")


for i in news:
    print(i.get('title'))
    print()
    print(f"  -{i.get('description')}")
    print()
    print(f"Source: {i.get('source_name')}")
    print(f"Published: {i.get('pubDate')}")
    print(f"Click link to see full article: {i.get('link')}")
    print("\n"+"="*90+"\n")
