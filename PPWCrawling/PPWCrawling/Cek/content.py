import scrapy
import json

class Pta(scrapy.Spider):
    name = "pta"
    file_json = open("t.json")
    start_urls = json.loads(file_json.read())
    urls = []

    for i in range(len(start_urls)):
        if start_urls[i]['url'] == None:
            pass
        else:
            b = start_urls[i]['url']
            urls.append(b + '?showpage=all')
    # print(urls)
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url = url, callback = self.parse)
        
    def parse(self, response):
        # print(response.url)
        yield {
            'Judul':response.css('body > section > div > div.section-detail-center > article > h1::text').get(),
            'Penulis':response.css('body > section > div > div.section-detail-center > article > div.auth-detail > a::text').get(),
            'Kategori':response.css('body > section > div > div.sin-breadcrumb.sin-clearfix > ul > li:nth-child(2) > a::text').get(),
            'Contents':response.css('body > section > div > div.section-detail-center > article > div.desc-artikel-detail.vidy-embed::text').extract()
        }
        # next_page = response.css('li.next a::attr(href)').get()
#         if next_page is not None:
#             next_page = response.urljoin(next_page)
#             yield scrapy.Request(next_page, callback=self.parse)