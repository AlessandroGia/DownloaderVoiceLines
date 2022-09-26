from bs4 import BeautifulSoup as bs
from requests import get

import os


def check_path(path: str) -> None:
    ''' Create directory if path doesn't exists
    '''
    if not os.path.exists(path):
            os.mkdir(path)

def get_bs(url: str) -> bs:
    ''' Get url's html istance
    '''
    return bs(get(url).text, "html.parser")
