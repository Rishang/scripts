#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import re
import dateutil
from fake_useragent import UserAgent
import click


def find_data(html):

    soup = BeautifulSoup(html, "lxml")

    href_flag = False
    h3_flag = False

    title = ""
    domain = ""
    url = ""
    description = ""

    elements = soup.find("div")
    count = 0

    if elements == None:
        return

    remove_str = r"\\u\w+|\n|\xa0..."

    for element in elements:
        # print(element)
        try:
            if href_flag == False:
                href = element.find("a")
                if href != -1:
<<<<<<< HEAD
                    href = href.get("href").split("url?q=")[-1]
                    domain = href.split("/")[2]
                    url = href.split("&sa=")[0]
=======
                    href = re.search(r'http.+', href.get("href"))[0]
                    # ignore url parameters 
                    url = re.sub(r'&(ved|sa)=.+','', href)
                    domain = url.split("/")[2]
>>>>>>> 7a882a50a77e2012a998b033a59aa47ef4c0fac6
                    href_flag = True

            if h3_flag == False:
                h3 = element.find("h3")
                if type(h3) != int or h3 != None:
                    title = re.sub(remove_str, "", h3.text)
                    h3_flag = True

            if count == 2:

                for span in element.find_all("span"):
                    span.decompose()

                d_text = [i for i in element.strings]

                description = re.sub(remove_str, "", d_text[0])
            count = count + 1
        except:
            return False

    return {"title": title, "domain": domain, "url": url, "description": description}


def google_search(query, p=0, type_=""):

    userAgent = UserAgent()
    if p > 1:
        p = (p * 10) - 10

    # search types
    types = {
        "news": "nws",
        "video": "vid",
<<<<<<< HEAD
        "book": "bks",
=======
        "book": "bks"
>>>>>>> 7a882a50a77e2012a998b033a59aa47ef4c0fac6
    }

    if type_.lower() in types:
        type_ = types[type_]
    else:
        type_ = ""

    search = f"https://www.google.com/search?q={query.replace(' ','+')}&start={p}&tbm={type_}"
    headers = {"user-agent": userAgent.random}

    data = requests.get(search, headers=headers)
    soup = BeautifulSoup(data.text, "lxml")

    f = []
    for result in range(0, 25):
        block = soup.select(f"#main > div:nth-child({result})")
        if len(block) != 0:
            block_next = block[0].next_element
            d = find_data(str(block_next))
            if d:
                f.append(d)

    return {
        "type": (type_ == "" and "all") or type_,
        "query": query,
        "search_url": search,
        "results": f,
        "result_count": len(f),
        "page": p,
        "headers": headers,
        "status_code": data.status_code,
    }


@click.group()
def cli():
    pass


@cli.command("search")
@click.option("-q")
@click.option("-p", default=0)
@click.option("-type", default="")
def cli_search(q, type: str, p):
    import json

    result = google_search(query=q, type_=type, p=p)
    print(json.dumps(result, indent=2))


cli()
