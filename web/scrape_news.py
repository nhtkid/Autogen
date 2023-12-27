# filename: scrape_news.py

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

# Define the URLs of the news sources we want to scrape
news_sources = [
    "https://www.nytimes.com/",
    "https://www.washingtonpost.com/",
    "https://www.bbc.co.uk/news",
    "https://www.theguardian.com/international",
    "https://www.cnn.com/",
]

# Define the search terms
search_terms = ["OpenAI", "Sam Altman"]

# Define a list to store the news
news_list = []

# Loop through each news source
for source in news_sources:
    # Send a GET request to the news source
    response = requests.get(source)

    # Parse the HTML content of the page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the news articles on the page
    articles = soup.find_all('article')

    # Loop through each article
    for article in articles:
        # Find the headline and the link of the article
        headline = article.find('h2').get_text() if article.find('h2') else ''
        link = article.find('a')['href'] if article.find('a') else ''

        # Check if any of the search terms are in the headline
        if any(term in headline for term in search_terms):
            # Find the date of the article
            date = article.find('time')
            if date:
                date = date['datetime']
                date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z')
            else:
                date = datetime.now()

            # Add the headline, link, and date to the news list
            news_list.append((headline, link, date))

# Sort the news list by date
news_list.sort(key=lambda x: x[2])

# Print the news in bullet points
for news in news_list:
    print(f"* {news[0]} ({news[2]}): {news[1]}")