import scrapy


class Link(scrapy.Spider):
    name = "link"
    start_urls = []

    for i in range(1,7):
        start_urls.append('https://www.antaranews.com/terkini/'+str(i))

    def parse(self, response):
        for page in range(1,18):
            for jurnal in response.xpath('//*[@id="main-container"]/div[2]/div/div[1]/article['+str(page)+']'):
                yield {
                    'url': jurnal.xpath('header/h3/a/@href').get(),
                    'label': jurnal.xpath('header/p/a/text()').get()
                }