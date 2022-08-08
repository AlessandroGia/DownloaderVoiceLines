from SmiteWiki import SmiteWiki

import time
import os


class UI:

    def __init__(self) -> None:
        url = self.__get_url_directory()
        self.smitewiki = SmiteWiki(url)

    @staticmethod
    def __write_on_file(data: str) -> None:
        with open("path_directory.bin", "wb") as file:
            file.write(data.encode())

    @staticmethod
    def __read_from_file() -> str:
        with open("path_directory.bin", "rb") as file:
            return file.read().decode()

    @staticmethod
    def __input_choice() -> int:
        while True:
            choice = int(input("1. Default\n2. Skins\n3. Entrambi\n8. Esci\n"))
            if 1 <= choice <= 3:
                break
        os.system("cls")
        return choice

    def __get_url_directory(self) -> str:
        path = ""
        if os.path.exists("path_directory.bin"):
            path = self.__read_from_file()
        if path:
            choice = input("Usare questo percorso: " + path + " S/N")
            if choice.lower() == "s":
                return path
            elif choice.lower() == 'n':
                return self.__change_path()
            else:
                pass
        else:
            return self.__change_path()

    def __change_path(self) -> str:
        path = ""
        while not path:
            path = input("Inserisci il percorso: ")
            if not os.path.exists(path):
                print("percorso inesistente!")
                path = ""
            self.__write_on_file(path)
        return path

    def start(self) -> None:
        choice = 0
        while choice != 8:
            os.system("cls")
            god = self.__input_god()
            choice = self.__input_choice()

            if choice == 1:
                self.smitewiki.voiceGod(god)
            elif choice == 2:
                self.smitewiki.voiceSkinsGod(god)
            elif choice == 3:
                self.smitewiki.voiceGod(god)
                self.smitewiki.voiceSkinsGod(god)
            elif choice == 8:
                continue

            time.sleep(2)

    def __input_god(self) -> str:
        while True:
            god = input("Inserisci il god: ").lower()
            if god in self.smitewiki.gods():
                break
            print("god inesistente")
        os.system("cls")
        return god


if __name__ == '__main__':
    UI().start()
