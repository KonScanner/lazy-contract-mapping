import scrapy


class LazyLabeler(scrapy.Spider):
    name = "contract_mappings"

    def __init__(self, urls=None, url: str = "", **kwargs):
        if urls:
            self.start_urls = urls
        self.start_urls = [url]
        super().__init__(**kwargs)

    def parse(self, response):
        yield {
            "titles": response.css("h1").css("span::text").extract(),
            "content": response.css("span::text").extract(),
        }
