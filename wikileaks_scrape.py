import re
from time import sleep

from send_invoice import send_invoice


def get_wikileaks_list():
    with open("wiki_leaks2.html") as file:
        i = 0
        for line in file:
            i += 1
            try:
                urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', line)
                url = urls[0]
                print(str(i)+":    "+url)
                send_invoice(url)
                sleep(0.6)
            except:
                print("EXCEPTION")


get_wikileaks_list()
