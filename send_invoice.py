import urllib3
import json


def send_invoice(url):
    data = json.dumps({"url": url})
    http = urllib3.PoolManager()
    r = http.request('POST', 'http://34.251.41.213:5000/url',
                     body=data,
                     headers={'Content-Type': 'application/json', 'Authorization': 'secret_key romanjevsechno'})
    print(r.data)


send_invoice("https://www.cca.edu/sites/default/files/pdf/08/word-to-pdf.pdf")