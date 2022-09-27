from asyncio import ensure_future, gather
from aiohttp import ClientSession
from utils import check_path
from vgs_parser import Vgs
from os import system

import os


class Downloader:

    def __init__(self, url: str) -> None:
        self.__path = os.path.join(url, "voicelines")
        self.__downloaded = 0
        check_path(self.__path)
            
    async def __get_oggs(self, session: ClientSession, url: str) -> None:
        async with session.get(url) as resp:
            with open(self.__url, "wb") as o:
                o.write(await resp.read())
                self.__downloaded += 1

    async def download(self, pack: dict) -> None:
        name_god = list(pack.keys())[0]
        self.__url = os.path.join(self.__path, name_god.lower().replace(" ", "_"))
        check_path(self.__url)
        async with ClientSession() as session:
            for skin_name in pack[name_god].keys():
                if pack[name_god][skin_name]:
                    downloaded = 0
                    self.__url = os.path.join(self.__url, skin_name.lower().replace(" ", "_"))
                    check_path(self.__url)
                    num_file_downloadable = len(pack[name_god][skin_name])
                    num_file_in_memory = sum([len(files) for r, d, files in os.walk(self.__url)])
                    num_file_downloadable -= num_file_in_memory
                    if num_file_downloadable:
                        tasks = []
                        self.__downloaded = 0
                        for vgs_ in pack[name_god][skin_name]:
                            vgss = Vgs(vgs_)
                            if 'https://static.wikia.nocookie.net' in vgss:
                                return vgs_
                            self.__url = os.path.join(self.__url, vgss)
                            check_path(self.__url)
                            self.__url = os.path.join(self.__url, vgs_.split('/')[7])
                            if not os.path.exists(self.__url):
                                tasks.append(ensure_future(self.__get_oggs(session, vgs_)))
                        await gather(*tasks)
                        print("{} [{}] ~ {}/{} voicelines scaricate.".format(name_god.capitalize(), skin_name, self.__downloaded, num_file_downloadable))
                    else:
                        print("{} [{}] ~ Gia' scaricato.".format(name_god.capitalize(), skin_name))
                else:
                    print("{} [{}] ~ Non trovato.".format(name_god.capitalize(), skin_name))
        input("\n\nPremi invio per continuare... ")
