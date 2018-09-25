import scrapy


class getPage(scrapy.Spider):
    name = 'getPage'

    start_urls = ['http://lab.scrapyd.cn']

    def parse(self, response):
        infos = response.css('div.quote')

        for info in infos:
            text = info.css('.text::text').extract_first()
            author = info.css('.author::text').extract_first()
            tag = info.css('.tags .tag::text').extract()
            tags = ','.join(tag)

            fileName = '%s-语录.txt' % author

            with open(fileName,'a+') as f:
                f.write(text)
                f.write('\n')
                f.write('标签：' + tags)
                f.write('\n------------\n')
                f.close()

        next_page = response.css('li.next a::attr(href)').extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)

            yield scrapy.Request(next_page,callback=self.parse)

