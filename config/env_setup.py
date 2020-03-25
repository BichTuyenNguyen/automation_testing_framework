import os


class EnvSetup:
    SITE = os.getenv('SITE', 'https://unsplash.com')
    API = os.getenv('API', 'https://unsplash.com/napi')
    TOKEN = os.getenv('TOKEN', '42ef72d98b48573570f34df9496bdfc643607580f0246152413601e1bd2d5a04')
    SELENIUM_TIMEOUT_SECONDS = 60
