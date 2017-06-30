import urllib3
import urllib
import json

def bing_search(query, search_type):
    #search_type: Web, Image, News, Video
    key= "54ba345aee514ecfa21f45b83d1474cc"
    http = urllib3.PoolManager()
    url = 'https://api.cognitive.microsoft.com/bing/v5.0/images/search?q='+query+'&count=50&savesearch=Off&offset=0'
    request = http.request('GET', url, headers = {'Ocp-Apim-Subscription-Key': key})
    response_data = request.data
    json_result = json.loads(response_data.decode('utf-8'))
    return json_result['value']
