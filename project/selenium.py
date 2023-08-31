from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def scrape_quotes(limit_pages=True):
    # Initialize Selenium WebDriver
    driver = webdriver.Chrome(executable_path= "C:\Users\folwa\OneDrive\Desktop\WEBSCRAP PROJECT\chromedriver.exe")
    
    # Initialize variables
    base_url = "https://quotes.toscrape.com/page/"
    page_num = 1
    all_quotes = []
    
    while True:
        # Navigate to the page
        driver.get(f"{base_url}{page_num}/")
        
        # Find quotes and authors
        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        
        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text
            all_quotes.append({"quote": text, "author": author})
        
        # Check if there's a next page
        try:
            next_button = driver.find_element(By.LINK_TEXT, "Next")
        except:
            print("No more pages.")
            break
        
        # Check if page limit is reached
        if limit_pages and page_num >= 100:
            print("Reached page limit.")
            break
        
        # Go to the next page
        next_button.click()
        page_num += 1
        time.sleep(2)  # Sleep to avoid rate-limiting
    
    # Close the driver
    driver.quit()
    
    return all_quotes

# Run the function
if __name__ == "__main__":
    scraped_data = scrape_quotes()
    print(scraped_data)
