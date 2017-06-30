import urllib3
import json


def send_invoice(url):
    data = json.dumps({"url": url})
    http = urllib3.PoolManager()
    r = http.request('POST', 'http://34.251.41.213:5000/url',
                     body=data,
                     headers={'Content-Type': 'application/json', 'Authorization': 'secret_key romanjevsechno'})
    print(r.data)


def get_positives():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.251.41.213:5000/url/positives',
                     headers={'Authorization': 'secret_key romanjevsechno'})
    to_return = json.loads(r.data.decode('utf-8'))
    return to_return


def get_negatives():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://34.251.41.213:5000/url/negatives',
                     headers={'Authorization': 'secret_key romanjevsechno'})
    to_return = json.loads(r.data.decode('utf-8'))
    return to_return

#send_invoice("www.ms.mff.cuni.cz/~prochas7/test.pdf")
#positives = get_positives()
#negatives = get_negatives()
#print(positives)
#print(negatives)
