import scrapy
from ..items import ProductsECommerceItem

class ProductsSpider(scrapy.Spider):
    name = 'products'
    number_product = 48
    start_urls = [
        # 'https://berrybenka.com/clothing/outwear/women'
        # 'https://berrybenka.com/clothing/dresses/women'
        # 'https://berrybenka.com/clothing/bottoms/women'
        'https://berrybenka.com/clothing/tops/women'
    ]

    def parse(self, response):

        products = ProductsECommerceItem()

        items = response.css('#li-catalog')

        for item in items:
            title = item.css('h1::text').get()
            price = item.css('.discount::text').get()
            image_source = item.css('.catalog-image').css('img::attr(src)').get()
            page_url = item.css('a::attr(href)').get()
            
            products['title'] = title
            products['price'] = price
            products['image_source'] = image_source
            products['page_url'] = page_url

            yield products
        
        next_page = response.css('.right a::attr(href)').get()
        next_url = 'https://berrybenka.com/clothing/tops/women/' + str(ProductsSpider.number_product)

        if next_page is not None:
            yield response.follow(next_url, callback = self.parse)
        
        ProductsSpider.number_product += 48
