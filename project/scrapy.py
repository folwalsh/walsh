import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']
    
    # Boolean parameter to limit the number of pages
    LIMIT_PAGES = True
    page_count = 0

    def parse(self, response):
        # Increment the page count
        self.page_count += 1
        
        # Scrape quotes and authors
        for quote in response.css('div.quote'):
            yield {
                'quote': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }
        
        # Follow pagination link
        next_page = response.css('li.next a::attr(href)').get()
        
        # Check if the LIMIT_PAGES parameter is True and if the page count is less than or equal to 100
        if next_page is not None and (not self.LIMIT_PAGES or (self.LIMIT_PAGES and self.page_count < 100)):
            yield response.follow(next_page, self.parse)
