import scrapy
from ..items import ProductsECommerceItem

class ProductsSpider(scrapy.Spider):
    name = 'products'
    number_product = 48
    start_urls = [
        'https://berrybenka.com/clothing/outerwear/women'
    ]

    def parse(self, response):

        items = ProductsECommerceItem()

        products = response.css('#li-catalog')

        for product in products:
            title = product.css('h1::text').get()
            price = product.css('.discount::text').get()
            source_image = product.css('.catalog-image').css('img::attr(src)').get()
            link_url = product.css('a::attr(href)').get()
            
            items['title'] = title
            items['price'] = price
            items['source_image'] = source_image
            items['link_url'] = link_url

            yield items
        
        next_page = response.css('.right a::attr(href)').get()
        next_url = 'https://berrybenka.com/clothing/outerwear/women/' + str(ProductsSpider.number_product)

        if next_page is not None:
            yield response.follow(next_url, callback = self.parse)
        
        ProductsSpider.number_product += 48
