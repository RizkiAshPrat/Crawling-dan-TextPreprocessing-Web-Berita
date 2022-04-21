import scrapy


class Link(scrapy.Spider):
    name = "link"
    start_urls = []

    for i in range(1,10):
        start_urls.append('https://pta.trunojoyo.ac.id/c_search/byprod/10/'+str(i))

    def parse(self, response):
        for page in range(1,6):
            for jurnal in response.xpath('//*[@id="content_journal"]/ul/li['+str(page)+']'):
                yield {
                    'Link': jurnal.xpath('div[3]/a/@href').get()
                }