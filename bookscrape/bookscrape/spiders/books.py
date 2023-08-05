import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        for item in response.css('article.product_pod'):
            yield {
                'Title':item.css('img.thumbnail::attr(alt)').get(),
                'price':item.css('p.price_color::text').get()
            }
