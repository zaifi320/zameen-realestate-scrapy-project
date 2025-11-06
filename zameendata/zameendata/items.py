# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ZameenItem(scrapy.Item):
    Title = scrapy.Field()
    Location = scrapy.Field()
    Price = scrapy.Field()
    Beds = scrapy.Field()
    Baths = scrapy.Field()
    Area = scrapy.Field()
    Details_URL = scrapy.Field()
    Property_ID = scrapy.Field()
    Latitude = scrapy.Field()
    Longitude = scrapy.Field()
    Province = scrapy.Field()
    City = scrapy.Field()
    Type = scrapy.Field()
    Purpose = scrapy.Field()
    Mobile_Number = scrapy.Field()
    Contact_Name = scrapy.Field()
    Agency_Name = scrapy.Field()

