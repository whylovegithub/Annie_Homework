# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
from Annie.items import AnnieItem

class GithubSpider(scrapy.Spider):
    name = 'githubtrending'
    start_urls = [
        'https://github.com/trending/python?since=monthly&spoken_language_code=en',
    ]

    def parse(self, response):
        i=0
        for br in response.css('article.Box-row'):
            item = AnnieItem()
            pname = br.css('h1.h3.lh-condensed a::text').extract()
            stargazer = br.css('div.f6.text-gray.mt-2 a.muted-link.d-inline-block.mr-3::text').extract()
            forks = br.css('div.f6.text-gray.mt-2 a.muted-link.d-inline-block.mr-3::text').extract()
            contributors = br.css('div.f6.text-gray.mt-2 span a::attr(href)').extract()
            # print(pname)
            # print(stargazer)
            # print(forks[3].strip())
            s = ''
            for k in contributors:
                s = s+k.replace('/','')+" "
            # s=contributors[0].replace('/','')+" "+contributors[1].replace('/','')+" "+contributors[2].replace('/','')+" "+contributors[3].replace('/','')+" "+contributors[4].replace('/','')
            # print(s)
            item['pname'] = pname[2].encode('raw_unicode_escape').strip()
            item['stargazer'] = stargazer[1].encode('raw_unicode_escape').strip()
            item['forks'] = forks[3].encode('raw_unicode_escape').strip()
            item['contributors'] = s.encode('raw_unicode_escape')
            # 3. encode('raw_unicode_escape')和 decode('raw_unicode_escape')
            #   若某字符串的内容为bytes形式, 如 a = '\xe7\x8e\x8b\xe8\x80\x85\xe5\x86\x9c\xe8\x8d\xaf'
            #   可使用encode('raw_unicode_escape')将此str转化为bytes, 再decode为str
            #   可使用decode('raw_unicode_escape')输出内容为bytes形式的字符串
            i +=1
            if(i > 10) :break
            yield item
        