# a bot that watches my youtube videos. Input video name and how long it should watch for.

from selenium import webdriver
from time import sleep
PATH = '' # enter path of chromedriver
CHANNEL_URL = '' # enter channel URL

class Bot():
    def __init__(self):
        self.browser = webdriver.Chrome(PATH)
        self.__home()
    
    def __home(self):
        self.browser.get(CHANNEL_URL)
        sleep(2)

    def __videoPage(self):
        self.browser.get(CHANNEL_URL + '/videos')
        sleep(2)

    def __videoID(self, elementNumber):
        self.ids = self.browser.find_elements_by_id('thumbnail')
        return self.ids[elementNumber]

    def watchVideo(self, videoNumber, watchTime):
        self.videoNumber = videoNumber
        self.watchTime = watchTime
        # self.__home()
        self.__videoPage()
        thumbnailElem = self.__videoID(self.videoNumber)
        thumbnailElem.click()
        sleep(self.watchTime)

myBot = Bot()
for i in range(23):
    myBot.watchVideo(0, 2)
