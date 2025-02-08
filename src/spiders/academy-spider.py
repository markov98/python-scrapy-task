import scrapy

class AcademySpider(scrapy.Spider):
    name = 'academy'
    start_urls = ['https://www.academy.com/p/nike-womens-court-legacy-next-nature-shoes']

    def parse(self, response):
        name = response.css('h1.productTitle--FWmyK::text').get()
        price_str = response.css('span.pricing.nowPrice.lg::text').get()
        color = response.css('span.swatchName--KWu4Q::text').get()
        available_colors = response.css('div#swatch-drawer-content button::attr(aria-label)').re(r'Color (.+)')

        reviews_count_str = response.css('button.ratingCount.linkBtn.focusable.smallLink::text').get()
        reviews_score_str = response.css('span.ratingAvg.textCaption::text').get()

        # Handle potential None values
        name = name.rstrip()
        price = float(price_str.replace('$', ''))

        reviews_count = int(reviews_count_str.replace('(', '').replace(')', '')) if reviews_count_str else 0
        reviews_score = float(reviews_score_str) if reviews_score_str else 0.0

        yield {
            'name': name,
            "price": price,
            "colour": color,
            "availableColours": available_colors,
            "reviews_count": reviews_count,
            "reviews_score": reviews_score
        }
