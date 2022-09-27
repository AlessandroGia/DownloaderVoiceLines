from exceptions.input_exceptions import GodNotFound, OptionNotFound, PathNotFound, Exit
from smite_wiki import SmiteWiki
from asyncio import run
from utils import clear

import os


class UI:

    def __init__(self) -> None:
        url = self.__get_url_directory()
        self.__smitewiki = SmiteWiki(url)

    @staticmethod
    def __write_on_file(data: str) -> None:
        with open("path_directory.bin", "wb") as file:
            file.write(data.encode())

    @staticmethod
    def __read_from_file() -> str:
        with open("path_directory.bin", "rb") as file:
            return file.read().decode()

    @staticmethod
    def __input_option() -> int:
        option = int(input("1. Default\n2. Skins\n3 Entrambi\n"))
        if not 1 <= option <= 3:
            raise OptionNotFound
        if option == 8:
            raise Exit
        clear()
        return option

    def __input_god(self) -> str:
        choice = input("Inserisci il god: ").lower().strip()
        if not choice in self.__smitewiki.gods():
            print("God inesistente!")
            raise GodNotFound
        elif choice == "exit":
            raise Exit
        return choice

    def __change_path(self) -> str:
        path = ""
        while not path:
            path = input("Inserisci il percorso: ")
            if not os.path.exists(path):
                print("percorso inesistente!")
                path = ""
            self.__write_on_file(path)
        return path

    def __get_url_directory(self) -> str:
        path = ""
        if os.path.exists("path_directory.bin"):
            path = self.__read_from_file()
        if path:
            choice = input("Usare questo percorso: " + path + " S/N ")
            if choice.lower() == "s":
                return path
            elif choice.lower() == 'n':
                return self.__change_path()
            else:
                pass
        else:
            return self.__change_path()

    async def start(self) -> None:

        clear()

        while True:
            try: god = self.__input_god()
            except GodNotFound: continue
            except Exit: return None
            else: break

        while True:
            try: option = self.__input_option()
            except OptionNotFound: continue
            except ValueError: continue
            except Exit: return None
            else: break

        if option == 1:
            await self.__smitewiki.voice_god(god)
        elif option == 2:
            await self.__smitewiki.voice_skins_god(god)
        elif option == 3:
            await self.__smitewiki.voice_god(god)
            await self.__smitewiki.voice_skins_god(god)
            


if __name__ == '__main__':
    run(UI().start())
