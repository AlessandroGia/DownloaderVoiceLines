from exceptions.input_exceptions import GodNotFound, OptionNotFound, PathNotFound, Exit
from smite_wiki import SmiteWiki
from asyncio import run
from utils import clear, exit

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
        if not option or option == 8:
            raise Exit
        elif not 1 <= option <= 3:
            raise OptionNotFound
        clear()
        return option

    def __input_god(self) -> str:
        choice = input("Inserisci il god: ").lower().strip()
        if not choice or choice == "exit":
            raise Exit
        elif not choice in self.__smitewiki.gods():
            print("God inesistente!")
            raise GodNotFound
        return choice

    def __choice_path(self, path: str) -> str:
        choice = input("Usare questo percorso:\n\t{} ~ S/N ".format(path)).lower().strip()
        if not choice or choice == "exit":
            raise Exit
        elif choice == 's':
            return path
        elif choice == 'n':
            while True:
                try: return self.__change_path()
                except PathNotFound: continue
                except Exit: exit()
        else:
            raise OptionNotFound

        
    def __change_path(self) -> str:
        path = input("Inserisci il percorso: ")
        if not path:
            raise Exit
        if not os.path.exists(path):
            print("percorso inesistente!")
            raise PathNotFound
        self.__write_on_file(path)
        return path

    def __get_url_directory(self) -> str:
        path = self.__read_from_file() if os.path.exists("path_directory.bin") else None
        if path:
            while True:
                try: return self.__choice_path(path)
                except OptionNotFound: continue
                except Exit: exit()
        else:
            while True:
                try: return self.__change_path()
                except PathNotFound: continue
                except Exit: exit()

    async def start(self) -> None:

        while True:

            clear()

            while True:
                try: god = self.__input_god()
                except GodNotFound: continue
                except Exit: exit()
                else: break

            clear()

            while True:
                try: option = self.__input_option()
                except OptionNotFound: continue
                except ValueError: continue
                except Exit: exit()
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
