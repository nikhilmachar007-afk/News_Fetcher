from api import fetch_news
from config import COUNTRIES, LANGUAGES
from storage import add_bookmarks, show_bookmarks
import time
def fetchNews():
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


    for number, i in enumerate(news, start=1):
        print(f"{number}. {i.get('title')}")
        print()
        print(f"  - {i.get('description')}")
        print()
        print(f"Source: {i.get('source_name')}")
        print(f"Published: {i.get('pubDate')}")
        print(f"Click link to see full article: {i.get('link')}")
        print("\n"+"="*90+"\n")

    while True:
        choice=input("Do you wanna bookmark favourites (y/n): ").strip().lower()
        if choice=="y":
            try:
                Bookmark_art=input("Enter the articles numbers to bookmark (1,2,3,...,n): ").strip().split(",")
            except ValueError:
                print("Invalid Input. Please enter comma separated article numbers. As demostrated through example.")
            for i in Bookmark_art:
                try:
                    j=int(i)-1
                except ValueError:
                    print("Invlid input.")
                add_bookmarks(news[j].get("source_name"),news[j].get("title"),news[j].get("link"))
            print("Bookmarks added successfully.")
            break
        elif choice=="n":
            break
        else:
            print("Invalid input. please try again.")

print("\n--------------------------NEWS FETCHER--------------------------")
print("Fetch news based on Category, Country, Language and Add Bookmarks.")
print("===================================================================")

while True:
    try:
        choice=int(input("1. Fetch news.\n2.Show Bookmarks.\n3.Quit\n Enter your choice: "))
        if choice==1:
            fetchNews()
            break
        elif choice==2:
            show_bookmarks()
            break
        elif choice==3:
            print("Closing News Feature...",end="\r")
            time.sleep(1)
            print("Closed."," "*50)
            break
        else:
            print("Invlid input. Please enter valid choice.")
    except ValueError:
        print("Invalid input. Try again.")
        continue