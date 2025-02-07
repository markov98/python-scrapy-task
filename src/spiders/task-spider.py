import scrapy

class AcademySpider(scrapy.Spider):
    name = 'academy'
    start_urls = ['https://www.academy.com/p/nike-womens-court-legacy-next-nature-shoes']

    def parse(self, response):
        product_name = response.css('h1.productTitle--FWmyK::text').get()


        yield {
            'name': product_name,
        }
