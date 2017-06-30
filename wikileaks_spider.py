import urllib3
import re
from time import sleep

from send_invoice import send_invoice

i = 0

def crawl_site(url):
    global i
    if url.lower().endswith(".pdf"):
        i += 1
        print(str(i) + "      " + url)
        send_invoice(url)
        sleep(0.55)
        return
    try:
        http = urllib3.PoolManager()
        r = http.request('Get', url)
        site = r.data.decode('utf-8')
        urls = re.findall('<a href="?\'?([^"\'>]*)', site)
        for new_url in urls:
            if "/.." not in (url + new_url):
                crawl_site(url + new_url)
    except:
        print("ERROR " + str(url))


#crawl_site("https://wikileaks.org/sony/docs/03_03/")
#crawl_site("https://wikileaks.org/sony/docs/03_02/")
#crawl_site("https://wikileaks.org/sony/docs/01/")
# NOT crawl_site("https://wikileaks.org/sony/docs/02/")
# NOT crawl_site("https://wikileaks.org/sony/docs/03/")
# NOT crawl_site("https://wikileaks.org/sony/docs/07/")
# NOT crawl_site("https://file.wikileaks.org/file")

