import scrapy
import json
import urllib
from ..items import ZameenItem

class ZameenSpider(scrapy.Spider):
    name = "zameen2"
    allowed_domains = ["zameen.com"]
    start_url = "https://www.zameen.com/Homes/Rawalpindi-41-"

    params = {}
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    custom_settings = {
        "DOWNLOAD_DELAY": 0.05,
        "AUTOTHROTTLE_ENABLED": True,
        "AUTOTHROTTLE_START_DELAY": 0.05,
        "AUTOTHROTTLE_MAX_DELAY": 1,
        "AUTOTHROTTLE_TARGET_CONCURRENCY": 8,  # -->req per domain
        "CONCURRENT_REQUESTS": 32,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 16,
    }

    def start_requests(self):
        base_urls = {
            'Buy': ("https://www.zameen.com/Homes/Rawalpindi-41-", 210),
            'Rent': ("https://www.zameen.com/Rentals/Rawalpindi-41-", 130)
        }

        for purpose, (base_url, total_pages) in base_urls.items():
            self.logger.info(f"📄 {purpose}: Scraping {total_pages} pages.")
            for page in range(1, total_pages + 1):
                next_page = f"{base_url}{page}.html?" + urllib.parse.urlencode(self.params)
                yield scrapy.Request(
                    url=next_page,
                    headers=self.headers,
                    callback=self.parse,
                    cb_kwargs={'purpose': purpose}
                )

    def parse(self, response, purpose=None, property_type=None):
        items = []
        listings = response.css('li[role="article"][aria-label="Listing"]')

        if not listings:
            self.logger.warning("⚠️ No listings found on this page.")
        
        for listing in listings:
            item = ZameenItem()
            item['Title'] = listing.css('h2[aria-label="Title"]::text').get()
            item['Location'] = listing.css('div[aria-label="Location"]::text').get()
            item['Price'] = listing.css('span[aria-label="Price"]::text').get()
            item['Beds'] = listing.css('span[aria-label="Beds"]::text').get()
            item['Baths'] = listing.css('span[aria-label="Baths"]::text').get()
            item['Area'] = listing.css('span[aria-label="Area"] *::text').get()
            item['Details_URL'] = 'https://www.zameen.com' + listing.css('a::attr(href)').get()
            item['Purpose'] = purpose
            items.append(item)
            #yield item

        try:
            script_data = ''.join([
                s.get() for s in response.css('script::text')
                if 'window.state =' in s.get()
            ])

            json_text = script_data.split('window.state = ')[-1].split('}};')[0] + '}}'
            json_data = json.loads(json_text)
            hits = json_data['algolia']['content']['hits']

            for i, hit in enumerate(hits):
                if i >= len(items):
                    continue

                item = items[i]
                item['Property_ID'] = hit.get('id')
                item['Latitude'] = hit.get('geography', {}).get('lat')
                item['Longitude'] = hit.get('geography', {}).get('lng')
                item['Province'] = hit.get('location', [{}])[1].get('name', 'N/A')
                item['City'] = hit.get('location', [{}])[2].get('name', 'N/A')
                item['Type'] = hit.get('category', [{}])[1].get('name', 'N/A')
                item['Purpose'] = hit.get('purpose', 'N/A')
                item['Price'] = hit.get('price', 'N/A')

                phone_info = hit.get('phoneNumber', {})
                mobile_numbers = phone_info.get('mobileNumbers', [])
                item['Mobile_Number'] = mobile_numbers[0] if mobile_numbers else 'N/A'
                item['Contact_Name'] = hit.get('contactName', 'N/A')
                item['Agency_Name'] = hit.get('agency', {}).get('name', 'N/A')

                #yield item

        except Exception as e:
            self.logger.warning(f"Error parsing JSON: {e}")
        for item in items:
            yield item
