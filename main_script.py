import convertor
import get_image_address
import invoice_crawl
counter = 0
for link in invoice_crawl.bing_search("invoice", "image"):
    print(counter)
    url = get_image_address.get_image_url(link['contentUrl'])
    convertor.url_to_pdf(url)
    counter += 1

