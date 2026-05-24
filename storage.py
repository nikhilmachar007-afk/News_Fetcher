import csv
import os

def add_bookmarks(source,title,link):
    with open("bookmarks.csv","a",newline="") as f:
        writer=csv.writer(f)
        writer.writerow([source,title,link])


def show_bookmarks():
    if os.path.exists("bookmarks.csv"):
        with open("bookmarks.csv","r") as f:
            reader=csv.reader(f)
            print("\n=====================================================================================================")
            print("---------------------------------------BOOKMARKED ARTICLES---------------------------------------------")
            for row in reader:
                if len(row)==0:
                    continue
                print(f"Source: {row[0]} \n   Title: {row[1]} \n   Link: {row[2]}\n")
            print("=====================================================================================================\n")
    else:
        print("NO bookmarks added yet.")