import convertor
import get_image_address
import invoice_crawl
import occupations
import os
import send_invoice
from time import sleep
occ = load_occupations():

for oc in occ:
    counter = 0
    print(oc)
    for link in invoice_crawl.bing_search(oc+"invoice", "image"):
        print(counter)
        url = get_image_address.get_image_url(link['contentUrl'])
        filename = convertor.url_to_pdf(url)
        counter += 1
        os.system("mv "+filename + " ~/WWW/"+filename) 
        sleep(0.6)
        send_invoice.send_invoice("http://www.ms.mff.cuni.cz/~prochas7/"+filename)
