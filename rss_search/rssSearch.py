import re
import requests
from bs4 import BeautifulSoup

class RssSearch:

    response: dict = {}

    def __init__(self, url:str):

        self.url = url
        self.soup = BeautifulSoup(requests.get(url).text, 'lxml')
        if self.valid_rss() == False:
            self._scrap_rss_url()

    def valid_rss(self):

        if re.search(r"<\?xml .+?>", self.soup.text):
            return True
        else:
            return False


    def _scrap_rss_url(self):    
        
        rss_url_list = self.soup.findAll(
            attrs={
                "type": [
                # "application/atom+xml",
                "application/rss+xml"
            ]}
        )
        if len(rss_url_list) != 0:
            self.response["rss_url"] = rss_url_list
        else:
            return False
