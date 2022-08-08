from bs4 import BeautifulSoup as bs
from Downloader import Downloader

import requests


class SmiteWiki:

    def __init__(self, url: str) -> None:
        r = requests.get("https://smite.fandom.com/wiki/God_voicelines")
        contenutoGods = bs(r.text, "html.parser")
        self.ulgods = contenutoGods.find("h2").next_sibling.next_sibling  # <ul> ..... </ul>
        self.dwnld = Downloader(url)
        self.__gods = []
        self.__numGods = 0
        self.__updateListGods()

    def voiceGod(self, godName: str) -> None:
        linksGod = {}
        linksGod[godName] = {}

        for ligods in self.ulgods.find_all("li"):
            if godName in ligods.a.get("title").lower():
                linkgod = ligods.a.get("href")

        skinName, links = self.__links(linkgod)
        linksGod[godName][skinName] = links
        self.dwnld.download(linksGod)
        #print(linksGod)
        return None

    def voiceSkinsGod(self, godName: str) -> None:

        r = requests.get("https://smite.fandom.com/wiki/Skin_voicelines")
        wiki = bs(r.text, "html.parser")

        god = godName.replace(" ", "_")
        god += "_skins"

        linkSkins = []
        linksSkins = {}
        linksSkins[godName] = {}

        for h2 in wiki.find_all("h2")[1:-1]:
            if god == h2.span.get("id").lower():
                ul = h2.next_sibling.next_sibling

        for li in ul.find_all("li"):
            linkSkins.append(li.a.get("href"))

        for link in linkSkins:
            skinName, links = self.__links(link)
            linksSkins[godName][skinName] = links

        self.dwnld.download(linksSkins)
        return None

    def __links(self, link: str) -> [str, str]:

        voicesLinks = []

        r = requests.get("https://smite.fandom.com/" + link)
        contenuto = bs(r.text, "html.parser")

        h1 = contenuto.find("h1").text.replace("voicelines", "").strip()
        if h1.lower() in self.__gods:
            skin_name = "default"
        else:
            skin_name = h1

        for x in contenuto.findAll("a"):
            if 'https://static.wikia.nocookie.net' in str(x.get('href')):
                if not (".png" in str(x.get('href')).lower() or
                        ".jpg" in str(x.get('href')).lower() or
                        ".jpeg" in str(x.get('href')).lower()):
                    voicesLinks.append(str(x.get('href')))
        return skin_name, voicesLinks

    def __updateListGods(self) -> None:
        self.__numGods = len(self.ulgods.find_all("li"))
        for ligods in self.ulgods.find_all("li"):
            self.__gods.append(
                ligods.a.get("title")[:-11].lower())  # rimuoviamo " voicelines" es. "Susano voicelines" => "Susano"

    def gods(self) -> list:
        if len(self.ulgods.find_all("li")) != self.__numGods:
            self.__updateListGods()
        return self.__gods
