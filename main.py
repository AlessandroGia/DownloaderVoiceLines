from exceptions.input_exceptions import GodNotFound, OptionNotFound, PathNotFound, Exit
from utils import clear, exit, check_permission
from const import FOLDER, PATH_FILE
from smite_wiki import SmiteWiki
from asyncio import run

import os


class UI:

    def __init__(self) -> None:
        url = self.__get_url_directory()
        self.__smitewiki = SmiteWiki(url)

    @staticmethod
    def __write_on_file(data: str) -> None:
        with open(PATH_FILE, "wb") as file:
            file.write(data.encode())

    @staticmethod
    def __read_from_file() -> str:
        with open(PATH_FILE, "rb") as file:
            return file.read().decode()

    @staticmethod
    def __input_option() -> int:
        option = int(input("1. Default\n2. Skins\n3. Entrambi\n"))
        if not option or option == 8:
            raise Exit
        elif not 1 <= option <= 3:
            raise OptionNotFound
        clear()
        return option

    def __input_god(self) -> str:
        choice = input("God: ").lower().strip()
        if not choice or choice == "exit":
            raise Exit
        elif not choice in self.__smitewiki.gods():
            print("God inesistente!")
            raise GodNotFound
        return choice

    def __choice_path(self, path: str) -> str:
        clear()
        choice = input("Usare questo percorso:\n\t{} ~ S/N ".format(os.path.join(path, FOLDER))).lower().strip()
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

    def __check_path(self, path: str) -> str:
        path = os.path.join(*list(filter(None, path.split(os.sep))))
        if not os.name == "nt": path = os.sep + path
        print(path)
        if os.path.exists(path):
            if not check_permission(path):
                raise PathNotFound
            while True:
                if FOLDER == path.split(os.sep)[-1]:
                    path = os.path.join(*path.split(os.sep)[:-1])
                    if not os.name == "nt": path = os.sep + path
                    choice = input("Usare la cartella :\n\t(Gia' presente) {} ~ S/N ".format(os.path.join(path.split(os.sep)[-1], FOLDER))).lower().strip()
                elif FOLDER in os.listdir(path) and os.path.isdir(os.path.join(path, FOLDER)):
                    choice = input("Usare la cartella :\n\t(Gia' presente) {} ~ S/N ".format(os.path.join(path.split(os.sep)[-1], FOLDER))).lower().strip()
                else:
                    choice = input("Creare la cartella:\n\t{} ~ S/N ".format(os.path.join(path.split(os.sep)[-1], FOLDER))).lower().strip()
                if not choice or choice == "exit": raise Exit
                elif choice == "s": return path
                elif choice == "n": raise PathNotFound
                else: continue
        else:
            raise PathNotFound

    def __change_path(self) -> str:
        clear()
        path = input("Percorso per la cartella: ")
        if not path:
            raise Exit
        try: path = self.__check_path(path)
        except Exit: exit()
        except PathNotFound: raise PathNotFound
        self.__write_on_file(path)
        return path

    def __get_url_directory(self) -> str:
        path = self.__read_from_file() if os.path.exists(PATH_FILE) else None
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
            print("Scaricando...\n")
            if option == 1:
                await self.__smitewiki.voice_god(god)
            elif option == 2:
                await self.__smitewiki.voice_skins_god(god)
            elif option == 3:
                await self.__smitewiki.voice_god(god)
                await self.__smitewiki.voice_skins_god(god)


if __name__ == '__main__':
    run(UI().start())
