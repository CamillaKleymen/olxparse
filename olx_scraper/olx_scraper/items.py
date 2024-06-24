import scrapy

class OlxApartmentItem(scrapy.Item):
    Заголовок = scrapy.Field()
    Цена = scrapy.Field()
    Район = scrapy.Field()