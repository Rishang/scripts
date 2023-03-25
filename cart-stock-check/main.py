from rich import print as pprint
from utils import scrapper

data = scrapper(config_file="config.yml")

pprint(data)
