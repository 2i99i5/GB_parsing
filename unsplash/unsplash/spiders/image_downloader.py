import scrapy


class ImageDownloaderSpider(scrapy.Spider):
    name = "image_downloader"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com"]

    def parse(self, response):
        pass
