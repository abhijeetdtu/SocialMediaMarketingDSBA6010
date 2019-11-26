from bs4 import BeautifulSoup
import scrapy
from scrapy import Request

class AmazonSpider(scrapy.Spider):
    name = 'Amazon'
    #https://www.amazon.com/s?k=hair+dye&page=15&qid=1571720207
    #https://www.amazon.com/s?k=hair+dye&ref=nb_sb_noss_2
    start_urls = ['https://www.amazon.com/s?k=hair+dye&page=25&qid=1571720207']
    totalPageCount = 20
    pageCounter = 0

    custom_settings = {
        'DOWNLOAD_DELAY' : 30,
        'CONCURRENT_REQUESTS' : 1,
        'CONCURRENT_REQUESTS_PER_DOMAIN' : 1,
        'DOWNLOAD_TIMEOUT' : 300,
        'USER_AGENT' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }

    def AbsUrl(self,url):
        return "https://www.amazon.com{}".format(url)

    def parse(self, response):
        if AmazonSpider.pageCounter > AmazonSpider.totalPageCount:
            return
        else:
            AmazonSpider.pageCounter += 1

        for i,div in enumerate(response.css(".s-result-list > div")):
            if "data-asin" in div.attrib:
                #print(div.attrib["data-asin"] , div)
                img =  div.css(".s-image")
                link = div.xpath("descendant::span[contains(@data-component-type , 's-product-image')]/a").attrib["href"]
                absLink = self.AbsUrl(link)
                stars = div.xpath("descendant-or-self::span[contains(@aria-label , 'stars')]")
                totalRatings = stars.xpath("following-sibling::span[1]").attrib["aria-label"]
                price = div.css(".a-price-whole::text").get() + "."+ div.css(".a-price-fraction::text").get()
                yield {
                "infoType":"base"
                ,'title': img.attrib["alt"]
                , "link" : absLink
                ,'stars':stars.attrib["aria-label"]
                , "totalRatings" : totalRatings
                , "price" : price}

                yield Request(url=absLink, callback=self.productDetails)

        for next_page in response.css('li.a-last > a'):
            yield response.follow(next_page, self.parse)

    def productDetails(self,response):
        colorList = response.css("img.imgSwatch")
        colors = [li.attrib["alt"] for li in colorList]
        detailsLi = response.css("#detail-bullets > table")
        weight = detailsLi.xpath("descendant::li/text()").re(r";(.+)ounces")
        bestSeller = response.xpath("//a[contains(@href , 'bestseller')]/parent::*")
        bestSellingCriteria = bestSeller.xpath(".//a[contains(@href , 'bestseller')]/text()").extract()
        ranks =  bestSeller.xpath("text()").re("#([\d,]+)")
        productDescription = "/n".join(response.xpath("//div[@id='productDescription']//p/text()").extract())
        yield {
        "infoType" : "additional"
        ,"colors": colors,
        "weight" : weight,
        "url" : response.request.url,
        "bestSelling" : {
            "criteria" : bestSellingCriteria,
            "ranks"  :ranks
        },
        "description" : productDescription
        }
