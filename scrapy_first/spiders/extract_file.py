import scrapy


class ItemSpider(scrapy.Spider):
    name = 'ExtractF'
    start_urls = [
        'http://lab.scrapyd.cn'
    ]

    def parse(self, response):
        label = response.css('div.quote')[0]
        text = label.css('.text::text').extract_first()
        author = label.css('.author::text').extract_first()
        tag = label.css('.tags .tag::text').extract()
        tags = ','.join(tag)

        fileName = '%s-语录.txt' % author
        f = open(fileName, "a+")
        f.write(text)
        f.write('\n')
        f.write('标签：' + tags)
        f.close()
