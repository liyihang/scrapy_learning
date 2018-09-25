import scrapy

class getMore(scrapy.Spider):
    name = 'getMore '
    start_urls = [
        'http://lab.scrapyd.cn'
    ]

    def parse(self, response):
        # get all tags and authors
        infos = response.css('div.quote')

        # foreach the info in infos
        for info in infos:
            text = info.css('.text::text').extract_first()
            author = info.css('.author::text').extract_first()
            tag = info.css('.tags .tag::text').extract()
            tags = ','.join(tag)
            fileName = '%s-语录.txt' % author
            with open(fileName,'a+') as f:
                f.write(text)
                f.write('\n')
                f.write('标签：'+tags)
                f.write('\n------------\n')
                f.close()



