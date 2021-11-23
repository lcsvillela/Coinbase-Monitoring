import requests
from bs4 import BeautifulSoup
import os
from time import sleep
from playsound import playsound


class Coinbase:
    def __init__(self):
        self.__information = {}
        self.screen_clear()
        self.__initial = self.get_last()

    def get_last(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
        }
        url = "https://blog.coinbase.com/latest"
        response = requests.get(url, headers=headers)
        blogpage = response.content
        soup = BeautifulSoup(blogpage, "html.parser")
        self.__information["title"] = soup.find_all("h3")[0].get_text()
        self.__information["link"] = soup.find_all(
            class_="button button--smaller button--chromeless u-baseColor--buttonNormal"
        )[0]["href"]
        self.__information["date"] = soup.find_all("time")[0].get_text()

        self.show_information(self.__information)
        return self.__information

    def verify(self):
        sleep(30)
        title = self.get_last()

        if self.__initial["title"] == title["title"]:
            self.screen_clear()
            self.show_information(title)
        else:
            self.show_information(title, 1)

    def show_information(self, information, alert=0):
        print(information["title"])
        print(information["date"])
        print(information["link"])
        if alert == 1:
            playsound("audio.wav")
            print(
                """#############################
                   #############################
                   #############################"""
            )

    def screen_clear(self):
        os.system("clear")


coinbase = Coinbase()

while True is True:
    try:
        coinbase.verify()
    except requests.exceptions.Timeout or requests.exceptions.ConnectTimeout:
        print("Failed: trying in 10 seconds")
        sleep(10)
        coinbase.verify()
