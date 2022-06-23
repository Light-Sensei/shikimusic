import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "8714251"))
    API_HASH = os.environ.get("API_HASH", "50c97a11b622575c5b9441b1062f601a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5276474965:AAFGJNgQEWJH1qQ8RlHBNAM9e3aJH7ke18c")
    STRING_SESSION = os.environ.get("STRING_SESSION", ")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ShikimoriXrobot")
    SUPPORT = os.environ.get("SUPPORT", "ShikimoriXSupport")
    CHANNEL = os.environ.get("CHANNEL", "ShikimoriXUpdates")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/13e6b986e95d613905b42.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/3b626f0a8f33937378a14.jpg")
