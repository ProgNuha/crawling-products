import scrapy
from ..items import ProductsECommerceItem

class ProductsSpider(scrapy.Spider):
    name = 'products'
    number_product = 48
    separator = 'n/'

    urls = [
        # 'https://berrybenka.com/clothing/outwear/women/0',
        # 'https://berrybenka.com/clothing/dresses/women/0',
        # 'https://berrybenka.com/clothing/bottoms/women/0',
        'https://berrybenka.com/clothing/tops/women/0'
    ]

    def start_requests(self):
        for url in ProductsSpider.urls:

            yield scrapy.Request(url=url, callback = self.parse)

    def parse(self, response):

        items = ProductsECommerceItem()

        products = response.css('#li-catalog')

        for product in products:
            items['title'] = product.css('h1::text').get()
            items['price'] = product.css('.discount::text').get()
            items['image_source'] = product.css('.catalog-image').css('img::attr(src)').get()
            items['page_url'] =  product.css('a::attr(href)').get()

            yield items
        
        next_page = response.css('.right a::attr(href)').get()
        current_url = str(response.request.url)
        current_url = current_url.split(ProductsSpider.separator,1)
        
        if next_page is not None:
            next_url = current_url[0] + ProductsSpider.separator + str(ProductsSpider.number_product)
            yield response.follow(next_url, callback = self.parse)
        
        ProductsSpider.number_product += 48
