import scrapy

start_url = "https://divan.ru/category/svet"

class Spider(scrapy.Spider):
    name = "home_exercise"
    allowed_domains = ["https://divan.ru"]
    start_urls = [start_url]

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            yield {
                'name':     divan.css('div.lsooF span::text').get(),
                'price':    divan.css('div.pY3d2 span::text').get(),
                'url':      f"{start_url}/{divan.css('a').attrib['href']}"
            }
