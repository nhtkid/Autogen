# filename: news_scraper.py

from newspaper import Article
import newspaper

def get_news(source_url):
    news_source = newspaper.build(source_url, memoize_articles=False)

    for article in news_source.articles:
        try:
            article.download()
            article.parse()
            print(f"Title: {article.title}\nURL: {article.url}\nPublished Date: {article.publish_date}\n---")
        except Exception as e:
            print(f"Error processing article: {article.url}")
            print(e)

get_news("https://www.nytimes.com/")