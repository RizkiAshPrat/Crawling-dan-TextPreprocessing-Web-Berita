import scrapy
import json


class Berita(scrapy.Spider):
    name = "berita"

    file_json = open("linkBerita.json")
    start_urls = json.loads(file_json.read())
    urls = []

    for i in range(len(start_urls)):
        b = start_urls[i]['url']
        urls.append(b)
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):
        for berita in response.xpath('//*[@id="main-container"]/div[2]'):
            yield {
                'Judul': berita.xpath('div/div[1]/article/header/h1/text()').get(),
                'Konten': berita.xpath('//*[@id="main-container"]/div[2]/div/div[1]/article/div/text()').extract()
            }