import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "8714251"))
    API_HASH = os.environ.get("API_HASH", "50c97a11b622575c5b9441b1062f601a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5276474965:AAFGJNgQEWJH1qQ8RlHBNAM9e3aJH7ke18c")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOG0BuxbW5PElazMuhK6xZtidhvlbusQdzxLKD0vziLhhiKqwzN5t6DIK_AEbe7fdkSlkM0RxJlVjj0bNBmeGUDlIJpFiolEWB1vra0Sqhn77Owg6xhnibD2qBU4m6anb7hVxtFnaLnX6vPixTYXftI__RWG-W09iDS8eP76LZfipGMIuRIWiytnEUIH7K4W17TvbjdpG4_QIzC0emWsu5E0PFfqiGIB8yqZFWKRkNqk3gHUg2YzrXNbSf4BGPdjnnCZaHsRgIS9Q2ub5oOlUxBfMmFiDZ1Uij6z-Tx9zFlxnEcQS23wmgU4fR7QLSFHuK3vH4UGCNXsWedOQBuB32SQwTzc=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "BoaHancock_Robot")
    SUPPORT = os.environ.get("SUPPORT", "BoaHancock_Support")
    CHANNEL = os.environ.get("CHANNEL", "boa_updates")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
