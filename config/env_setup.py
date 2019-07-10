import os


class EnvSetUp:
    API = os.getenv('API', 'https://unsplash.com/napi')
    TOKEN = os.getenv('TOKEN', '91757b02ca25010990680ef1dd05a3045f76b42dabd09bdc4ff1f35289f4be31')
