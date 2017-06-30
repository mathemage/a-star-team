import convertor
import get_image_address
import invoice_crawl

for link in invoice_crawl.bing_search("invoice", "image"):
    url = get_image_address.get_image_url(link['contentUrl'])
    convertor.url_to_pdf(url)

