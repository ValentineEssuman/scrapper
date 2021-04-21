import scrapy


class ImagesSpider(scrapy.Spider):
    name = "images"
    start_urls = [
        'https://hdqwalls.com/latest-wallpapers'
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'images-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

    # def parse(self, response):
    #     for quote in response.css('img'):
    #         yield {
    #             'image': quote.css('s').get(),
    #             'author': quote.css('span small::text').get(),
    #             'tags': quote.css('div.tags a.tag::text').getall(),
    #         }

    #     next_page = response.css('ul.nav a::attr(href)').get()
    #     if next_page is not None or '#':
    #         yield response.follow(next_page, callback=self.parse)