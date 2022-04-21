import scrapy

class Url(scrapy.Spider):
    name = "url"
    start_urls = []
    
    def __init__(self):
        url = 'https://tekno.sindonews.com/more/612/'
        for page in range(0, 120, ++20):
            self.start_urls.append(url + str(page))
        
    def parse(self, response):
        for page in range(1,23):
            for url in response.css('body > section > div > div.section-left'):
                yield {
                    'url' : url.css('div:nth-child('+ str(page) +') > div > div.title > a::attr(href)').get()
                } 
            # self.start_links.append(links)
        # print(self.start_links)