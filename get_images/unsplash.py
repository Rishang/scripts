import requests
import json
import random
import asyncio
import aiohttp


class Unsplash:

    API = "https://unsplash.com/napi"

    # landscape | portrait | squarish
    orientation = "landscape"
    
    # max 29
    per_page = 29
    
    __orientation_q = f"orientation={orientation}"
    __per_page_q = f"per_page={per_page}"
    
    random = None

    # for officl api
    TOKEN = ""
    total = int()
    total_pages = int()

    def __init__(self):
        pass 
        

    def query(self, search=None, page: int = 1, random_img: bool = False):

        if search is not None:
            
            if type(search) is list:
                q = [
                    f"{self.API}/search/photos?query={s}&page={page}&" + self.__orientation_q
                    for s in search
                ]

                loop = asyncio.new_event_loop()
                tmp_data = loop.run_until_complete(self._multi_query(q))

                r_img: list = []
                for d in tmp_data:
                    tmp = json.loads(d)
                    r_img = r_img + tmp.get('results')
                del tmp_data

                if len(r_img) != 0 and random_img == True:

                    self.random = random.choice(r_img)
                    return random.choice(r_img)

                return r_img
        else:
            return False

        query = self.API + f"/search/photos?query={search}&page={page}&" + self.__orientation_q
        data = json.loads(requests.get(query).text)
        if "errors" in data.keys():
            print(data)

        self.total = data["total"]
        self.total_pages = data["total_pages"]

        if len(data["results"]) != 0 and random_img == True:

            self.random = random.choice(data["results"])
            return random.choice(data["results"])

        return data["results"] or None

    def any(self):

        query = (
            f"{self.API}/photos?{self.__per_page_q}&page=1&"
            + self.__orientation_q
        )
        data = json.loads(requests.get(query).text)
        self.random = random.choice(data)
        return random.choice(data)

    async def _multi_query(self, q: list):

        async with aiohttp.ClientSession() as session:
            d = []
            for i in q:
                async with session.get(i) as response:

                    print("Status:", response.status)
                    html = await response.text()
                    d.append(html)
        return d
