# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
from pymongo import MongoClient


class CoindataPipeline(object):

    def __init__(self):

      host = settings['MONGODB_HOST']
      port = settings['MONGODB_PORT']
      dbName = settings['MONGODB_DBNAME']
      self.db = MongoClient(host=host, port=port)[dbName]

      # url = settings['MONGODB_URL']
      # dbname = settings['MONGODB_DOCNAME']
      # self.db = MongoClient(url)[dbname]

    def process_item(self, item, spider):
      self.db['test'].insert(item.__dict__)
      return item
