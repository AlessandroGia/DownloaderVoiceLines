from VGS import vgs

import os
import requests


class Downloader:

    def __init__(self, url: str) -> None:
        self.url = os.path.join(url, "voicelines")
        if not os.path.exists(self.url):
            os.mkdir(self.url)

    @staticmethod
    def __printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█',
                         printEnd="\r"):

        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
        if iteration == total:
            print()

    def download(self, pack: dict) -> None:

        nameGod = list(pack.keys())[0]
        pathGod = os.path.join(self.url, nameGod.lower().replace(" ", "_"))

        if not os.path.exists(pathGod):
            os.mkdir(pathGod)

        for skinName in pack[nameGod].keys():

            if pack[nameGod][skinName]:

                scaricati = 0
                pathSkin = os.path.join(pathGod, skinName.lower().replace(" ", "_"))

                if not os.path.exists(pathSkin):
                    os.mkdir(pathSkin)

                numFileScaricabili = len(pack[nameGod][skinName])
                numFilePresentiInMemoria = sum([len(files) for r, d, files in os.walk(pathSkin)])
                numFileScaricabili -= numFilePresentiInMemoria

                if numFileScaricabili:

                    for vgs_ in pack[nameGod][skinName]:
                        vgss = vgs(vgs_)
                        if 'https://static.wikia.nocookie.net' in vgss:
                            return vgs_
                        pathVgs = os.path.join(pathSkin, vgss)

                        if not os.path.exists(pathVgs):
                            os.mkdir(pathVgs)
                        pathFile = os.path.join(pathVgs, vgs_.split('/')[7])

                        if not os.path.exists(pathFile):
                            if scaricati == 0:
                                self.__printProgressBar(scaricati, numFileScaricabili, prefix=nameGod.capitalize() + " - " + skinName.replace('_', ' ') + ' / Voicepacks:',
                                                        suffix='Completato', length=50)
                            r = requests.get(vgs_)
                            with open(pathFile, "wb") as o:
                                o.write(r.content)
                                scaricati += 1
                                self.__printProgressBar(scaricati, numFileScaricabili, prefix=nameGod.capitalize() + " - " + skinName.replace('_', ' ') + ' / Voicepacks:',
                                                 suffix='Completato', length=50)
                    print('Scaricati - ' + str(scaricati) + "/" + str(numFileScaricabili))
                else:
                    print(nameGod.capitalize() + " - " + skinName, " / Gia' scaricato")
            else:
                print(nameGod.capitalize() + " - " + skinName, " / Non trovato")
            print("\t-------------- ")

        input("\nPremi invio per continuare...")


