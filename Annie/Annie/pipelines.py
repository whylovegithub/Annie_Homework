# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv


class AnniePipeline(object):

    def __init__(self):
        # setting the filename
        self.f = open("githubtrending2.csv","wb")
        # setting propper headers for the csv 
        self.filednames = ["pname","stargazer","forks","contributors"]
        # setting as DictWriter, the 1st para is sepcific file that u want to write,
        # the 2nd one is the headers u want to write(I think it should be conclued in the Item)
        self.writer = csv.DictWriter(self.f,fieldnames=self.filednames)
        # it is just a 1 time job so it should be done at the initial
        # cuz process_item(self, item, spider) run several times.
        self.writer.writeheader()

    def process_item(self, item, spider):
        # write down a row, data from the item pulled from the responses.
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.f.close