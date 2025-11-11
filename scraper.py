import requests
import csv
URL = "https://newsapi.org/v2/top-headlines?country=us&apiKey=a1f278e97a06434c8b63036b6830b7c9"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get(URL, headers=headers)
response.raise_for_status()
data = response.json()
results = data["articles"]
title = [articles.get("title") for articles in results]
author = [articles.get("author") for articles in results]
date = [articles.get("publishedAt") for articles in results]
description = [articles.get("description") for articles in results]
with open("news.csv", mode= 'w') as csv_file: 
   csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
   csv_writer.writerow(["title", [title]])
   csv_writer.writerow(["author",[author]])
   csv_writer.writerow(["date",[date]])
   csv_writer.writerow(["description",[description]])
   print("Data written to news.csv")