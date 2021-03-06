import scrapy
import requests
from parsel import Selector
import csv
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.revzilla.com/faq',
    ]

    def parse(self, response):
        questions = response.xpath('//div[@class="wysiwyg__content"]/section/h2/text()').getall()
        answers = response.xpath('//div[@class="wysiwyg__content"]/section/p/text()').getall()
        links = response.selector.css("div.wysiwyg__content p a").xpath('@href').getall() 
        yield {
            'Questions': questions,
            'Links'     : links,
            'Answers':answers,

        }
        with open('revzilla.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerows(zip(questions, links,answers))
        



