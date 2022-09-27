from asyncio import get_event_loop
from utils import get_bs, a_get_bs
from downloader import Downloader


class SmiteWiki:

    def __init__(self, url: str) -> None:
        
        self.__ulgods = get_bs("https://smite.fandom.com/wiki/God_voicelines").find("h2").next_sibling.next_sibling # <ul> ..... </ul>
        self.__downloader = Downloader(url)
        self.__gods = []
        self.__num_gods = 0
        self.__update_list_gods()

    async def __links(self, link: str) -> list([str, str]):
        voices_links = []
        content = await a_get_bs("https://smite.fandom.com/" + link)
        h1 = content.find("h1").text.replace("voicelines", "").strip()
        if h1.lower() in self.__gods:
            skin_name = "default"
        else:
            skin_name = h1
        for x in content.findAll("a"):
            if 'https://static.wikia.nocookie.net' in str(x.get('href')):
                if not (".png" in str(x.get('href')).lower() or
                        ".jpg" in str(x.get('href')).lower() or
                        ".jpeg" in str(x.get('href')).lower()):
                    voices_links.append(str(x.get('href')))
        return skin_name, voices_links

    def __update_list_gods(self) -> None:
        self.__num_gods = len(self.__ulgods.find_all("li"))
        for ligods in self.__ulgods.find_all("li"):
            self.__gods.append(
                ligods.a.get("title")[:-11].lower())  # rimuoviamo " voicelines" es. "Susano voicelines" => "Susano"

    async def voice_god(self, god_name: str) -> None:
        links_god = {god_name: {}}
        for ligods in self.__ulgods.find_all("li"):
            if god_name in ligods.a.get("title").lower():
                linkgod = ligods.a.get("href")
        skinName, links = await self.__links(linkgod)
        links_god[god_name][skinName] = links
        await self.__downloader.download(links_god)
        #print(linksGod)
        return None

    async def voice_skins_god(self, god_name: str) -> None:
        wiki = await a_get_bs("https://smite.fandom.com/wiki/Skin_voicelines")
        god = god_name.replace(" ", "_") + "_skins"
        link_skins = []
        _link_skins = {god_name: {}}
        for h2 in wiki.find_all("h2")[1:-1]:
            if god == h2.span.get("id").lower():
                ul = h2.next_sibling.next_sibling
        for li in ul.find_all("li"):
            link_skins.append(li.a.get("href"))
        for link in link_skins:
            skinName, links = await self.__links(link)
            _link_skins[god_name][skinName] = links
        await self.__downloader.download(_link_skins)
        return None

    def gods(self) -> list:
        if len(self.__ulgods.find_all("li")) != self.__num_gods:
            self.__update_list_gods()
        return self.__gods
