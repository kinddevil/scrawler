#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc :
"""
from coindata.items import CoindataItem
import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["163.com", "sina.com"]
    start_urls = [
        "http://www.163.com/",
        "http://www.sina.com/"
    ]

    def parse(self, response):
        print "parse..."
        # print response.body

        # yield scrapy.Request("https://www.infoq.com", meta={'item_1': "item"}, callback=self.parse_article)
        # yield scrapy.Request("http://paike.zhikuxuan.com", callback=self.parse_article)

        for sel in response.xpath('//a'):
            print sel, "sel..."
            print(sel.attrib['href'])
            item = CoindataItem()

            # item['title'] = sel.xpath('h3/a/text()')[0].extract()
            # item['link'] = sel.xpath('h3/a/@href')[0].extract()
            # url = response.urljoin(item['link'])
            # item['desc'] = sel.xpath('div[@class="mob-sub"]/text()')[0].extract()
            # print("result...",item['title'],item['link'],item['desc'])

            item['title'] = "title2"
            item['link'] = "link"
            item['desc'] = "desc"
            yield item

            # yield scrapy.Request(sel.attrib['href'], callback=self.parse_article)


    def parse_article(self, response):
        # detail = response.xpath('//div[@class="article-wrap"]')
        item = CoindataItem()

        # item['title'] = detail.xpath('h1/text()')[0].extract()
        # item['link'] = response.url
        # item['posttime'] = detail.xpath(
        #     'div[@class="article-author"]/span[@class="article-time"]/text()')[0].extract()
        # print(item['title'],item['link'],item['posttime'])

        item['title'] = "title2"
        item['link'] = "link"
        item['desc'] = "desc"

        yield item
