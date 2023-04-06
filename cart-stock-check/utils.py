import requests
from bs4 import BeautifulSoup
from lxml import etree
from lxml.etree import _Element

import yaml
from dataclasses import dataclass


@dataclass
class configElement:
    url: str
    source: str
    message: str
    is_xpath: bool
    tags: list[str]

@dataclass


class Selector:
    def __init__(self, url: str) -> None:
        self.URL = url

        self.HEADERS = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
            "Accept-Language": "en-US, en;q=0.5",
        }

        self.soup = None | BeautifulSoup

        self.source()

    def source(self):
        if self.soup != None | BeautifulSoup:
            return
        r = requests.get(self.URL, headers=self.HEADERS)
        if r.status_code >= 400:
            raise Exception(f"status: {r.status_code}\nmessage: {r.text}")
        soup = BeautifulSoup(r.content, "lxml")
        self.soup = soup

    def get_xpath(self, xpath: str = ""):
        dom: list[_Element] = etree.HTML(str(self.soup)).xpath(xpath)
        return dom


def configFile(name: str):
    with open(name, "r") as f:
        yml = yaml.load(f.read(), Loader=yaml.SafeLoader)
        return [configElement(**i) for i in yml]


def scrapper(config_file: str = "config.yml"):
    cfg = configFile(config_file)
    data = []
    for item in cfg:
        s = Selector(url=item.url)
        message_match = False
        if item.is_xpath == True:
            content = s.get_xpath(item.source)
        else:
            content = s.soup.select(item.source)

        if content != []:
            cont_txt = content[0].text
        else:
            data.append({})
            continue

        if cont_txt == item.message:
            message_match = True

        data.append({"url": item.url, "content": cont_txt, "match": message_match, "tags": item.tags})

    return data
