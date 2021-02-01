# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/600.8.9 (KHTML, like Gecko)'
class AmazondataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_rate = scrapy.Field()
    product_link = scrapy.Field()

class AmazonReviewItem(scrapy.Item):
    product_name = scrapy.Field()
    customer_name = scrapy.Field()
    customer_review_star = scrapy.Field()
    customer_review_title = scrapy.Field()
    review_date = scrapy.Field()
    customer_review = scrapy.Field()
