

import requests
from bs4 import BeautifulSoup

def scrape_quotes(limit_to_100=True):
    base_url = "https://quotes.toscrape.com/page/"
    page_num = 1
    scraped_links = 0
    
    while True:
        if limit_to_100 and scraped_links >= 100:
            break

        url = f"{base_url}{page_num}/"
        response = requests.get(url)
        
        if response.status_code != 200:
            print("No more pages to scrape.")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all("div", class_="quote")
        
        for quote in quotes:
            if limit_to_100 and scraped_links >= 100:
                break
            
            quote_text = quote.find("span", class_="text").text
            author = quote.find("small", class_="author").text
            print(f"Quote: {quote_text}\nAuthor: {author}\n")
            
            scraped_links += 1

        page_num += 1

# Set the boolean parameter to limit the number of pages to 100
scrape_quotes(True)
