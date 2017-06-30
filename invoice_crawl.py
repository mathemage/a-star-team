import urllib3
import urllib
import json
#query = "invoice"
#req = urllib2.Request('https://api.cognitive.microsoft.com/bing/v5.0/search?q='+query+'&count=50&savesearch=Off&offset=0', headers = {'Accept' : 'application/xml'})

def bing_search(query, search_type):
    #search_type: Web, Image, News, Video
    key= "54ba345aee514ecfa21f45b83d1474cc"
    http = urllib3.PoolManager()
    #query = urllib.quote(query)
    # create credential for authentication
    user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
    url = 'https://api.cognitive.microsoft.com/bing/v5.0//search?q='+query+'&count=50&savesearch=Off&offset=0'
    request = http.request('GET', url, headers = {'Ocp-Apim-Subscription-Key': key})
    print(request.data)
    response_data = request.data
    json_result = json.loads(response_data.decode('utf-8'))
    return json_result['value']
    #'webpages'
