from selenium import webdriver


class Browser:

    @staticmethod
    def connection():
        return webdriver.Chrome('./resource/chromedriver')

