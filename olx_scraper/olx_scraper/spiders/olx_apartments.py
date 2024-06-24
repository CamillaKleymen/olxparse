import scrapy

class OlxApartmentsSpider(scrapy.Spider):
    name = 'olx_apartments'
    allowed_domains = ['www.olx.uz']
    start_urls = ['https://www.olx.uz/nedvizhimost/kvartiry/']

    def parse(self, response):
        apartments = response.css('div.css-1apmciz')
        
        for apartment in apartments:
            item = {
                'Заголовок': apartment.css('h6.css-16v5mdi::text').get(),
                'Цена': apartment.css('p.css-tyui9s::text').get(),
                'Район': apartment.css('p.css-1a4brun::text').get()
            }
            yield item

        # Проверяем, есть ли следующая страница
        next_page = response.css('a[data-testid="pagination-forward"]::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)