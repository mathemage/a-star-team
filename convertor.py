import re
import os
import requests

def is_pdf(url):
    return re.match('.*\.pdf', url) is None

def url_to_pdf(url):
    in_file_name = re.sub('.*/', '', url)
    out_file_name = re.sub('\..*', '', in_file_name) + '.pdf'

    f = open(in_file_name, 'wb')
    f.write(requests.get(url).content)
    f.close

    os.system('convert ' + in_file_name + ' ' + out_file_name)
    os.system('rm ' + in_file_name)

    return out_file_name
