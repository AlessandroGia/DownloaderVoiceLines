from bs4 import BeautifulSoup as bs
from aiohttp import ClientSession
from requests import get

import sys
import os

def check_permission(path: str) -> bool:
    ''' Check if a directory can be updated
    '''
    return os.access(path, os.X_OK | os.W_OK)

def check_path(path: str) -> None:
    ''' Create directory if path doesn't exists
    '''
    if not os.path.exists(path):
            os.mkdir(path)

async def a_get_bs(url: str) -> bs:
    ''' Get url's html istance, courutine
    '''
    async with ClientSession() as session:
        async with session.get(url) as resp:
            r = await resp.text()
            return bs(r, "html.parser")

def get_bs(url: str) -> bs:
    ''' Get url's html istance
    '''
    return bs(get(url).text, "html.parser")

def clear() -> None:
    ''' Clear the terminal
    '''
    os.system('cls' if os.name == 'nt' else 'clear')

def exit() -> None:
    ''' Exit from the script
    '''
    clear()
    sys.exit(0)