import scrapy
from ..items import AmazonReviewItem
class amazonSpider(scrapy.Spider):
    name="reviews"
    count =20
    start_urls =["https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A2811119011%2Cn%3A2407749011&dc&qid=1612127415&rnid=2811119011&ref=sr_nr_n_2"]

    #def start_requests(self):      
        #for url in urls:
        #   yield scrapy.Request(url=url,callback=self.parse)
    
    def parse(self, response):
        #userReviewPageUrl = response.xpath("//a[@data-hook='see-all-reviews-link-foot']/@href").get()  
        #product_link=response.xpath("//h2[@class]/a[@class='a-link-normal a-text-normal']/@href").get()
        for product in response.xpath("//h2[@class]/a[@class='a-link-normal a-text-normal']/@href"):
            yield scrapy.Request(url= response.urljoin(product.get()),callback=self.praseProductPage)
        nextPage = response.xpath("//li[@class='a-last']/a/@href").get()
        if nextPage != None:
            response.follow(response.urljoin(nextPage),self.parse)

    def praseProductPage(self,response):
        review_view = response.xpath("//div[@id='cr-pagination-footer-0']/a[@data-hook='see-all-reviews-link-foot']/@href").get()
        if review_view != None:
            yield scrapy.Request(url=response.urljoin(review_view),callback = self.praseUserReview)
        

        #else:
            #response.follow(response.urljoin(nextPage),self.parse)
        
    def praseUserReview(self,response):

        items = AmazonReviewItem()
        product_title = response.xpath("//h1[@class='a-size-large a-text-ellipsis']/a[@data-hook='product-link']/text()").getall()
        customer_name = response.xpath("//div[@class='a-profile-content']/span[@class='a-profile-name']/text()").getall()
        customer_review_star = response.xpath("//div[@class='a-row']/a[@class='a-link-normal']/@title").getall()
        customer_review_title = response.xpath("//div[@class='a-row']/a[@data-hook='review-title']/span/text()").getall()
        review_date = response.xpath("//div[@class='a-section celwidget']/span[@data-hook='review-date']/text()").getall()
        customer_review = response.xpath("//div[@class='a-row a-spacing-small review-data']/span[@data-hook='review-body']/span/.").getall()

        items['product_name'] = product_title
        items['customer_name'] = customer_name
        items['customer_review_star'] = customer_review_star
        items['customer_review_title'] = customer_review_title
        items['review_date'] = review_date
        items['customer_review'] = customer_review
        
        yield items
        
        next_page = response.xpath("//li[@class='a-last']/a/@href").get()
        if next_page != None:
            response.follow(response.urljoin(next_page),self.praseUserReview)
        ##print()

    def loadUserReviewPage(self,response):
        userReviewPageUrl = response.xpath("//a[@data-hook='see-all-reviews-link-foot']/@href").get()
        if userReviewPageUrl is not None:
            return response.urljoin(userReviewPageUrl)
            #next_page = response.urljoin(userReviewPageUrl)
            #yield scrapy.Request(next_page, callback=self.parse)

    def prase_userReview(self, response):
        items = AmazonReviewItem()
        product_name = response.xpath("//div[@class='a-row product-title']/h1[@class='a-size-large a-text-ellipsis']/a/text()").getall()
        customer_name = response.xpath("//div[@class='a-profile-content']/span[@class='a-profile-name']/text()").getall()
        customer_review_star = response.xpath("//div[@class='a-row']/a[@class='a-link-normal']/@title").getall()
        customer_review_title = response.xpath("//div[@class='a-row']/a[@data-hook='review-title']/span/text()").getall()
        review_date = response.xpath("//div[@class='a-section celwidget']/span[@data-hook='review-date']/text()").getall()
        customer_review = response.xpath("//div[@class='a-row a-spacing-small review-data']/span[@data-hook='review-body']/span/.").getall()

        #items['product_name'] = product_name
        #items['product_rate'] = product_rate
        #items['product_link'] = product_link

        items['product_name'] = product_name
        items['customer_name'] = customer_name
        items['customer_review_star'] = customer_review_star
        items['customer_review_title'] = customer_review_title
        items['review_date'] = review_date
        items['customer_review'] = customer_review
        
        yield items

        nextPage =response.xpath("//li[@class='a-last']/a/@href").get()  
        if nextPage is not None:
                     yield response.follow(nextPage,callback=self.parse)
