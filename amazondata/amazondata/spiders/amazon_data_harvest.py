import scrapy
from ..items import AmazondataItem
class amazonSpider(scrapy.Spider):
    name="amazondata"
    page_number =2
    
    def start_requests(self):
        urls =['https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A2811119011%2Cn%3A2407749011&dc&qid=1612019324&rnid=2811119011&ref=sr_nr_n_2']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    
    def parse(self, response):
        items = AmazondataItem()

        product_name = response.xpath("//span[@class='a-size-medium a-color-base a-text-normal']/text()").getall()
        product_rate = response.xpath("//div[@class='a-row a-size-small']/span/span[@class='a-declarative']/a[@class='a-popover-trigger a-declarative']/i/span[@class='a-icon-alt']/text()").getall()
        product_link = response.xpath("//h2[@class]/a[@class='a-link-normal a-text-normal']/@href").getall()

        items['product_name'] = product_name
        items['product_rate'] = product_rate
        items['product_link'] = product_link
        
        yield items
        nextPage ='https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A2811119011%2Cn%3A2407749011&dc&page='+str(amazonSpider.page_number)+'&qid=1612019328&rnid=2811119011&ref=sr_pg_2'
        if amazonSpider.page_number <=200:
            amazonSpider.page_number+=1
            yield response.follow(nextPage, callback = self.parse)