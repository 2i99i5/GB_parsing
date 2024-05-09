import scrapy


class ImageDownloaderSpider(scrapy.Spider):
    name = "image_downloader"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com"]



# ссылки на страницы: '//figure/div/div/a[@itemprop="contentUrl"]'
# изображение: '//div[@class="WxXog"]/img'
# автор: '//div[@class="TeuLI"]/a/text()'
# описание: '//h1'

    def parse(self, response):
        # Используем XPath для извлечения URL изображений
        for image in response.xpath('//figure/div/div/a[@itemprop="contentUrl"]/@href').extract():
            yield scrapy.Request(response.urljoin(image), self.parse_image)

    def parse_image(self, response):
        for image in response.xpath('//div[@class="WxXog"]/img'):
            image_url = image.xpath('@src').extract_first()
            yield scrapy.Request(response.urljoin(image_url), self.save_image)

    # Сохраняем изображение в папку images
    def save_image(self, response):
        filename = response.url.split('/')[-1]
        # Сохраняем изображение в папку images
        with open(f'images/{filename}', 'wb') as f:
            f.write(response.body)

    # # Сохраняем изображение в папку images
    # def save_image(self, response):
    #     filename = response.url.split
    #     with open(f'images/{filename}', 'wb') as f:
    #         f.write(response.body)
