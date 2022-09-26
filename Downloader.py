from asyncio import ensure_future, gather
from aiohttp import ClientSession
from utils import check_path
from os import system
from VGS import vgs

import os


class Downloader:

    def __init__(self, url: str) -> None:
        self.url = os.path.join(url, "voicelines")
        self.__downloaded = 0
        check_path(self.url)
            
    async def get_oggs(self, session: ClientSession, url: str, path_file: str) -> None:
        async with session.get(url) as resp:
            with open(path_file, "wb") as o:
                o.write(await resp.read())
                self.__downloaded += 1

    async def download(self, pack: dict) -> None:
        name_god = list(pack.keys())[0]
        path_god = os.path.join(self.url, name_god.lower().replace(" ", "_"))
        check_path(path_god)
        async with ClientSession() as session:
            for skin_name in pack[name_god].keys():
                if pack[name_god][skin_name]:
                    downloaded = 0
                    path_skin = os.path.join(path_god, skin_name.lower().replace(" ", "_"))
                    check_path(path_skin)
                    num_file_downloadable = len(pack[name_god][skin_name])
                    num_file_in_memory = sum([len(files) for r, d, files in os.walk(path_skin)])
                    num_file_downloadable -= num_file_in_memory
                    if num_file_downloadable:
                        tasks = []
                        self.__downloaded = 0
                        for vgs_ in pack[name_god][skin_name]:
                            vgss = vgs(vgs_)
                            if 'https://static.wikia.nocookie.net' in vgss:
                                return vgs_
                            path_vgs = os.path.join(path_skin, vgss)
                            check_path(path_vgs)
                            path_file = os.path.join(path_vgs, vgs_.split('/')[7])
                            if not os.path.exists(path_file):
                                tasks.append(ensure_future(self.get_oggs(session, vgs_, path_file)))
                        await gather(*tasks)
                        print("{} [{}] ~ {}/{} voicelines scaricate.".format(name_god.capitalize(), skin_name, self.__downloaded, num_file_downloadable))
                    else:
                        print("{} [{}] ~ Gia' scaricato.".format(name_god.capitalize(), skin_name))
                else:
                    print("{} [{}] ~ Non trovato.".format(name_god.capitalize(), skin_name))
        input("\n\nPremi invio per continuare... ")
