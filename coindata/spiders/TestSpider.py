#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: sample
Desc :
"""
from coindata.items import CoindataItem
import scrapy
import random

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["163.com", "sina.com"]
    start_urls = [
        "http://www.163.com/",
        "http://www.sina.com/"
    ]
    ua_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    ]

    def parse(self, response):

        headers = {'User-Agent': random.choice(self.ua_list)}
        print("parse...")
        # print(response.body)

        # yield scrapy.Request("https://www.infoq.com", meta={'item_1': "item"}, callback=self.parse_article)
        # yield scrapy.Request("http://paike.zhikuxuan.com", callback=self.parse_article)

        for sel in response.xpath('//a'):
            print(sel, "sel...")
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

            # yield scrapy.Request(sel.attrib['href'], headers=headers, callback=self.parse_article)


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
