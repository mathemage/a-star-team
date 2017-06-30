import urllib.parse as urlparse


def get_image_url(url):
    par = urlparse.parse_qs(urlparse.urlparse(url).query)
    return par["r"][0]


image_url = get_image_url(
    "http://www.bing.com/cr?IG=2F502957E52E4CABADB7E838A57D4DAA&CID=1F90AFA61C1C693221B4A5171DBA68AE&rd=1&h=iyncBwLen_AfCVD4j71VNV3o8NDqj7tWEq8MZne5t_Q&v=1&r=http%3a%2f%2f3.bp.blogspot.com%2f_DJEIRrK4tl4%2fTDxAtvvqhNI%2fAAAAAAAAFnc%2f5PePA9BGUQM%2fs1600%2finvoice%252Bnew.PNG&p=DevEx,5008.1")
print(image_url)
